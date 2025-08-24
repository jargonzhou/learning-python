"""
Unit test of inheritance

`super()`

subclassing built-in types

multiple inheeritance, mro(method resolution order)

mixin classes: only add or customize the behavior of child or sibling classes
- ABCs are mixins
- `http.server`: use `socketserver` ThreadingMixIn, ForkingMixin
- `django.views.generic.base`: TemplateResponseMixin
- `tkinter.ttk`: XView, YView, ...

coping with inheritance
- favor object composition over class inheritance
- understand why inheritance is used
- make interface explicit with ABCs: abc.ABC, typing.Protocol
- use explicit mixins for code reuse
- provide aggregate classes to users
- subclass only classes designed for subclassing
- avoid subclassing from concrete classes
"""

import collections
from typing import Any, OrderedDict
import unittest

# pylint: skip-file


class TestInheritance(unittest.TestCase):
  def test_super(self) -> None:
    class LastUpdatedOrderedDict(OrderedDict):
      """store items in the order they were last updated"""

      def __setitem__(self, key: Any, value: Any) -> None:
        super().__setitem__(key, value)
        self.move_to_end(key)

    class NotRecommeded(OrderedDict):
      """counter example"""

      def __setitem__(self, key: Any, value: Any) -> None:
        # not super()
        OrderedDict.__setitem__(self, key, value)
        self.move_to_end(key)


class TestSubclassingBuiltInTypes(unittest.TestCase):
  def test_tricky(self) -> None:
    class DoppelDict(dict):
      def __setitem__(self, key: Any, value: Any) -> None:
        super().__setitem__(key, [value] * 2)
    dd = DoppelDict(one=1)
    self.assertDictEqual({'one': 1}, dd)
    # [] operator call __setitem__
    dd['two'] = 2
    self.assertDictEqual({'one': 1, 'two': [2, 2]}, dd)
    # update: ignore __setitem__
    dd.update(three=3)
    self.assertDictEqual({'one': 1, 'two': [2, 2], 'three': 3}, dd)

    class AnswerDict(dict):
      def __getitem__(self, key: Any) -> Any:
        return 42
    ad = AnswerDict(a='foo')
    self.assertEqual(42, ad['a'])
    d: dict = {}
    # update: ignore __setitem__
    d.update(ad)
    self.assertEqual('foo', d['a'])

    class DoppelDict2(collections.UserDict):  # subclass UserDict
      def __setitem__(self, key: Any, value: Any) -> None:
        super().__setitem__(key, [value] * 2)
    dd2 = DoppelDict2(one=1)
    # not a dict
    self.assertFalse(isinstance(dd2, dict))
    self.assertEqual({'one': [1, 1]}, dd2)
    # [] operator call __setitem__
    dd2['two'] = 2
    self.assertEqual({'one': [1, 1], 'two': [2, 2]}, dd2)
    # update: call __setitem__
    dd2.update(three=3)
    self.assertEqual({'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}, dd2)


class TestMRO(unittest.TestCase):
  def test_diamond(self) -> None:
    from src.classes_and_protocols.diamond import Leaf
    leaf = Leaf()
    leaf.ping()
    # <instance of Leaf>.ping() in Leaf
    # <instance of Leaf>.ping() in A
    # <instance of Leaf>.ping() in B
    # <instance of Leaf>.ping() in Root
    print()
    leaf.pong()
    # <instance of Leaf>.pong() in A
    # <instance of Leaf>.pong() in B

    self.assertEqual("(<class 'src.classes_and_protocols.diamond.Leaf'>, <class 'src.classes_and_protocols.diamond.A'>, <class 'src.classes_and_protocols.diamond.B'>, <class 'src.classes_and_protocols.diamond.Root'>, <class 'object'>)",
                     str(Leaf.__mro__))

  def test_diamon2(self) -> None:
    from src.classes_and_protocols.diamond import U, LeafUA
    u = U()
    with self.assertRaises(AttributeError) as cm:
      u.ping()
      # <src.classes_and_protocols.diamond.U object at 0x000002263C166DB0>.ping() in U
    self.assertEqual("'super' object has no attribute 'ping'",
                     str(cm.exception))

    leaf = LeafUA()
    leaf.ping()
    # <instance of LeafUA > .ping() in LeafUA
    # <instance of LeafUA > .ping() in U
    # <instance of LeafUA > .ping() in A
    # <instance of LeafUA > .ping() in Root
    self.assertEqual("(<class 'src.classes_and_protocols.diamond.LeafUA'>, <class 'src.classes_and_protocols.diamond.U'>, <class 'src.classes_and_protocols.diamond.A'>, <class 'src.classes_and_protocols.diamond.Root'>, <class 'object'>)", str(LeafUA.__mro__))

    from src.classes_and_protocols.diamond import print_mro
    import tkinter
    print_mro(tkinter.Text)
    # Text, Widget, BaseWidget, Misc, Pack, Place, Grid, XView, YView, object


class TestMixinClasses(unittest.TestCase):
  def test_uppercase_mixin(self) -> None:
    from src.classes_and_protocols.mixin import UpperDict, UpperCounter
    d = UpperDict([('a', 'letter A'), (2, 'digit two')])
    self.assertListEqual(['A', 2], list(d.keys()))
    d['b'] = 'letter B'
    self.assertTrue('b' in d)
    self.assertEqual('letter A', d['a'])
    self.assertListEqual(['A', 2, 'B'], list(d.keys()))

    c = UpperCounter('BaNanA')
    self.assertListEqual([('A', 3), ('N', 2), ('B', 1)],
                         c.most_common())
