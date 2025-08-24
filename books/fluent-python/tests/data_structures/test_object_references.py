"""
Unit test of object references, mutablity, recylcing.
"""

# pylint: skip-file

import unittest
import copy
import weakref


class Bus:
  def __init__(self, passengers=None):
    if passengers is None:
      self.passengers = []
    else:
      self.passengers = list(passengers)

  def pick(self, name):
    self.passengers.append(name)

  def drop(self, name):
    self.passengers.remove(name)


class TestObjectReference(unittest.TestCase):
  def test_identity_equality_alias(self):
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles  # alias
    self.assertTrue(lewis is charles)  # compare identity
    self.assertEqual(id(charles), id(lewis))
    lewis['balance'] = 950
    self.assertDictEqual({'name': 'Charles L. Dodgson',
                         'born': 1832, 'balance': 950}, charles)

    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    self.assertTrue(alex == charles)  # __eq__()
    self.assertTrue(alex is not charles)

  def test_tuple_relative_immutablity(self):
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    self.assertTupleEqual(t1, t2)
    self.assertTrue(t1 == t2)
    print(id(t1[-1]))  # 1882050344384
    t1[-1].append(99)
    print(id(t1[-1]))  # 1882050344384 - not changed
    self.assertFalse(t1 == t2)

  def test_copy(self):
    """copies are shallow by default"""
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)
    self.assertTrue(l1 == l2)
    self.assertFalse(l1 is l2)

    # copy: values, containers
    l1 = [3, [66, 55, 44], (7, 8, 9)]
    l2 = list(l1)  # shallow copy
    l1.append(100)  # no effect on l2!!!
    l1[1].remove(55)  # list: mutable, shared
    self.assertListEqual([3, [66, 44], (7, 8, 9), 100], l1)
    self.assertEqual([3, [66, 44], (7, 8, 9)], l2)
    l2[1] += [33, 22]  # list: mutable, shared
    l2[2] += (10, 11)  # tuple: immutable, create new tuple
    self.assertListEqual([3, [66, 44, 33, 22], (7, 8, 9), 100], l1)
    self.assertListEqual([3, [66, 44, 33, 22], (7, 8, 9, 10, 11)], l2)

  def test_deepcopy(self):
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)  # shallow copy
    bus3 = copy.deepcopy(bus1)  # deep copy
    # 1706729084336 1706729084480 1706729084576
    print(id(bus1), id(bus2), id(bus3))
    bus1.drop('Bill')
    self.assertListEqual(['Alice', 'Claire', 'David'], bus2.passengers)
    # 1706729135808 1706729135808 1706728633856
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
    self.assertListEqual(['Alice', 'Bill', 'Claire', 'David'], bus3.passengers)

  def test_cycle_reference(self):
    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)  # [10, 20, [[...], 30]]
    c = copy.deepcopy(a)
    print(c)  # [10, 20, [[...], 30]]

  def test_function(self):
    """parameter passing: call by sharing"""
    def f(a, b):
      a += b
      return a
    x, y = 1, 2
    f(x, y)
    self.assertEqual(1, x)
    self.assertEqual(2, y)

    a = [1, 2]
    b = [3, 4]
    f(a, b)
    self.assertListEqual([1, 2, 3, 4], a)
    self.assertListEqual([3, 4], b)

    a = (1, 2)
    b = (3, 4)
    f(a, b)
    self.assertTupleEqual((1, 2), a)
    self.assertTupleEqual((3, 4), b)

  def test_del(self):
    a = [1, 2]
    b = a
    del a  # delete refernce to a
    self.assertListEqual([1, 2], b)

  def test_weakref(self):
    s1 = {1, 2, 3}
    s2 = s1

    def bye():
      print('...like tears in the rain.')

    ender = weakref.finalize(s1, bye)  # register callback
    self.assertTrue(ender.alive)
    del s1
    self.assertTrue(ender.alive)
    s2 = 'spam'  # rebind s2 to make {1,2,3} unreachable
    self.assertFalse(ender.alive)

  def test_trick(self):
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    self.assertTrue(t1 is t2)
    t3 = t1[:]  # make a copy, but return reference to the same object
    self.assertTrue(t3 is t1)

    t1 = (1, 2, 3, 4)
    t2 = (1, 2, 3, 4)
    self.assertTrue(t2 is t1)  # !!!
    s1 = 'ABC'
    s2 = 'ABC'
    self.assertTrue(s1 is s2)  # interning
