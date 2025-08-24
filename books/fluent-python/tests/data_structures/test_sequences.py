"""
Unit test of sequences.
"""

import array
import unittest
from collections import abc, deque

from src.common import fixed
from src.data_structures.lis import parse, _eval

# pylint: skip-file


class TestSequence(unittest.TestCase):
  def test_mutability(self):
    # immutable
    self.assertTrue(tuple, abc.Sequence)
    self.assertTrue(str, abc.Sequence)
    self.assertTrue(bytes, abc.Sequence)
    # mutable
    self.assertTrue(list, abc.MutableSequence)
    self.assertTrue(bytearray, abc.MutableSequence)
    self.assertTrue(array.array, abc.MutableSequence)
    self.assertTrue(deque, abc.MutableSequence)

  def test_subclass(self):
    # sequence is reversible
    self.assertTrue(abc.Sequence, abc.Reversible)
    # sequence is collection
    self.assertTrue(abc.Sequence, abc.Collection)
    # including mutable sequences
    self.assertTrue(abc.MutableSequence, abc.Sequence)

  def test_add_mul(self):
    l1 = [1, 2]
    l2 = [3, 4]
    self.assertListEqual([1, 2, 3, 4], l1 + l2)
    self.assertEqual([1, 2, 1, 2], l1 * 2)
    self.assertEqual([1, 2, 1, 2], 2 * l1)

    l3 = [5, 6]
    l3 += l1  # augmented assignment
    self.assertListEqual([5, 6, 1, 2], l3)


class TestList(unittest.TestCase):
  def test_list_comprehension(self):
    """listcomp: for tuples, arrays, other types of sequences"""
    symbols = '$¢£¥€¤'
    codes = []
    for symbol in symbols:
      codes.append(ord(symbol))  # ord: unicode point
    self.assertListEqual([ord(symbol) for symbol in symbols], codes)

    # compare with filter, map
    self.assertListEqual([ord(symbol) for symbol in symbols if ord(symbol) > 127],
                         list(filter(lambda c: c > 127, map(ord, symbols))))

    # cartesian product
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tishirts = []
    for color in colors:
      for size in sizes:
        tishirts.append((color, size))
    self.assertListEqual([(color, size) for color in colors for size in sizes],
                         tishirts)

  def test_sort(self):
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    self.assertListEqual(
        ['apple', 'banana', 'grape', 'raspberry'], sorted(fruits))
    self.assertListEqual(['grape', 'raspberry', 'apple', 'banana'], fruits)

    fruits.sort()  # sort in place
    self.assertListEqual(['apple', 'banana', 'grape', 'raspberry'], fruits)


class TestGeneratorExpression(unittest.TestCase):
  """genexps: yield items one by one"""

  def test_genexps(self):
    symbols = '$¢£¥€¤'
    self.assertTupleEqual((36, 162, 163, 165, 8364, 164),
                          tuple(ord(symbol) for symbol in symbols))
    self.assertSequenceEqual(array.array('I', [36, 162, 163, 165, 8364, 164]),
                             array.array('I', (ord(symbol) for symbol in symbols)))


class TestTuple(unittest.TestCase):
  def test_as_records(self):
    # Latitude and longitude of the Los Angeles International Airport
    lax_coordinates = (33.9425, -118.408056)
    # Data about Tokyo: name, year, population (thousands), population change (%), and area (km²)
    city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
    # (country_code, passport_number)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                    ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
      print("%s/%s" % passport)  # % undestand tuple
    for country, _ in traveler_ids:  # unpacking
      print(country)

  def test_as_immutable_list(self):
    tf = (10, 'alpha', (1, 2))  # tuple: (1,2)
    tm = (10, 'alpha', [1, 2])  # list: [1,2]
    self.assertTrue(fixed(tf))
    self.assertFalse(fixed(tm))

  def test_augmented_assignment(self):
    t = (1, 2, [30, 40])
    try:
      t[2] += [50, 60]
    except TypeError as e:
      # 'tuple' object does not support item assignment
      print(e)
    self.assertListEqual([30, 40, 50, 60], t[2])


class TestUnpacking(unittest.TestCase):
  """unpacking sequences and iterables"""

  def test_unpacking(self):
    # parallem assignment
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    self.assertAlmostEqual(latitude, 33.9425)

    # swap values
    a = 1
    b = 2
    a, b = b, a
    self.assertEqual(2, a)
    self.assertEqual(1, b)

    # *tuple
    t = (20, 8)
    quotient, remainder = divmod(*t)  # unpack tuples
    self.assertEqual(2, quotient)
    self.assertEqual(4, remainder)

  def test_grab_excess_items(self):
    # *: grab excess items
    a, b, *rest = range(5)
    self.assertEqual(0, a)
    self.assertEqual(1, b)
    self.assertListEqual([2, 3, 4], rest)
    *head, b, c, d = range(5)
    self.assertListEqual([0, 1], head)

  def test_unpacking_funcall(self):
    def fun(a, b, c, d, *rest):
      return a, b, c, d, rest
    self.assertTupleEqual((1, 2, 3, 4, (5, 6)),
                          fun(*[1, 2], 3, *range(4, 7)))

  def test_nested_unpacking(self):
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
      print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


class TestSequencePatternMatching(unittest.TestCase):
  """for: list, tuple, array.array, collections.deque, memoryview, range"""

  def test_pm(self):
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
      # match
      match record:
        # case: pattern, optional guard
        # case [name, _, _, (lat, lon)] if lon <= 0:
        # with type info
        # case [str(name), _, _, (float(lat), float(lon))] if lon <= 0:
        # *_: match any number of items. or use *extras
        case [str(name), *_, (float(lat), float(lon))] if lon <= 0:
          print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

  def test_lis(self):
    self.assertListEqual(['gcd', 18, 45], parse('(gcd 18 45)'))
    self.assertListEqual(['define', 'double', ['lambda', ['n'], ['*', 'n', 2]]],
                         parse('''
                               (define double
                                  (lambda (n)
                                      (* n 2)))
                         '''))


class TestSlicing(unittest.TestCase):
  """for: list, tuple, str, all sequence types
  s[a:b:c] with step c
  slice object: slice(a,b,c)
  """

  def test_slice(self):
    l = [10, 20, 30, 40, 50]
    self.assertListEqual([10, 20], l[:2])

    invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2    $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    line_items = invoice.split('\n')[2:]
    for item in line_items:
      print(item[UNIT_PRICE], item[DESCRIPTION])

  def test_assgin_to_slice(self):
    l = list(range(10))
    self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], l)
    l[2:5] = [20, 30]
    self.assertListEqual([0, 1, 20, 30, 5, 6, 7, 8, 9], l)
    del l[5:7]
    self.assertListEqual([0, 1, 20, 30, 5, 8, 9], l)
    l[3::2] = [11, 22]
    self.assertListEqual([0, 1, 20, 11, 5, 22, 9], l)
    l[2:5] = [100]
    self.assertListEqual([0, 1, 100, 22, 9], l)


class TestArray(unittest.TestCase):
  """sequence of numbers"""

  def test_large_array(self):
    from random import random
    floats = array.array('d', (random() for i in range(10**7)))
    with open('floats.bin', 'wb') as f:
      floats.tofile(f)
    floats2 = array.array('d')
    with open('floats.bin', 'rb') as f:
      floats2.fromfile(f, 10**7)
    self.assertEqual(floats, floats2)

    # clean up
    import os
    os.remove('floats.bin')


class TestMemoryView(unittest.TestCase):
  """a shared memory sequence type"""

  def test_6_bytes(self):
    octets = array.array('B', range(6))
    # memoryview
    m1 = memoryview(octets)
    # tolist
    self.assertListEqual([0, 1, 2, 3, 4, 5], m1.tolist())
    # cast
    m2 = m1.cast('B', [2, 3])
    self.assertListEqual([[0, 1, 2], [3, 4, 5]], m2.tolist())
    m3 = m1.cast('B', [3, 2])
    self.assertListEqual([[0, 1], [2, 3], [4, 5]], m3.tolist())

    # updates
    m2[1, 1] = 22
    m3[1, 1] = 33
    self.assertListEqual([0, 1, 2, 33, 22, 5], octets.tolist())

  def test_16_bit_integer(self):
    numbers = array.array('h', [-2, -1, 0, 1, 2])  # 16-bit signed integer
    memv = memoryview(numbers)
    self.assertEqual(5, len(memv))
    memv_oct = memv.cast('B')  # as 10 bytes
    print(memv_oct.tobytes())
    memv_oct[5] = 4  # assign to a byte
    print(memv_oct.tobytes())
    self.assertListEqual([-2, -1, 1024, 1, 2], numbers.tolist())


class TestNumPy(unittest.TestCase):
  def test_usage(self):
    import numpy as np
    a = np.arange(12)
    self.assertTrue(isinstance(a, np.ndarray))
    self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], a.tolist())
    self.assertTupleEqual((12,), a.shape)
    a.shape = 3, 4
    self.assertListEqual([[0, 1, 2, 3],
                          [4, 5, 6, 7],
                          [8, 9, 10, 11]], a.tolist())
    # indexing
    self.assertListEqual([8, 9, 10, 11], a[2].tolist())
    self.assertEqual(9, a[2, 1])
    self.assertListEqual([1, 5, 9], a[:, 1].tolist())


class TestQueue(unittest.TestCase):
  """
  deque
  queue: thread-safe SimpleQueue, Queue, LifoQueue, PriotiryQueue
  multiprocessing: unbounded SimpleQueue, bounded Queue, JoinableQueue
  asyncio: Queue, LifoQueue, PriorityQueue, JoinableQueu
  heapq
  """

  def test_deque(self):
    from collections import deque
    dq = deque(range(10), maxlen=10)
    self.assertSequenceEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dq)
    # rotate
    dq.rotate(3)
    self.assertSequenceEqual([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], dq)
    dq.rotate(-4)
    self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dq)
    # append
    dq.appendleft(-1)
    self.assertSequenceEqual([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], dq)
    # extend
    dq.extend([11, 22, 33])
    self.assertSequenceEqual([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], dq)
    dq.extendleft([10, 20, 30, 40])
    self.assertSequenceEqual([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], dq)
