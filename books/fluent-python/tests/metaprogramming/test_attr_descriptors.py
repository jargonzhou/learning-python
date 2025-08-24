"""
Unit test of attribute descriptors.

descriptors: for reusing same access logic in multiple attributes
- a class implementing dynamic protocol of __set__(), __get__(), __delete__()
  - `property` class
- Python functions are descriptors.

terms:
- descriptor class: ex `Quantity`
- managed class: ex `LineItem`
- descriptor instance: always class attribute of the managed class
- managed instance: ex `LineItem` instance
- storage attribute: the attribute in managed instance hold the value of a managed attribute for the instance: ex `LineItem` instance attribute `weight price`
- managed attribute: the public attribute in managed class that is handled by a descriptor instance, with values stored in storage attribute

__set_name__(): add to descriptor procotocl in Python 3.6
- called by type.__new__()

attribute access:
- read attribute through instance: return the attribute defined in instance
  - if no such attribute in instance: return the attribute in class
- assgin to attribute in instance: create attribute in instane, not affect the class
  
overriding V.S. non-overriding
- __set__() present: overrding descriptor.
- overriding descriptor: override attempts to assign to instance attribute
  - properties
- overriding descriptor without __get__: instance attribute shadows the descriptor, but only when reading
- non-overiding descriptor: instance attribute shadows the descriptor
  - methods
    - bounded method: __self__, __func__, __call__
  - @functools.cached_property
  - user defined functions: non-overrding descriptors
    - have a __get__ method, not implement __set__
- overwrite: assignment to class
    
descriptor docstring

overrding deletion: delete a managed attribute
- __delete__() in descriptor class
"""
# pylint: skip-file

from __future__ import annotations
from types import FunctionType, MethodType
import unittest


class TestDescriptor(unittest.TestCase):
  def test_quanity(self) -> None:
    from src.metaprogramming.descriptors import LineItem
    with self.assertRaises(ValueError) as cm:
      walnuts = LineItem('walnuts', 0, 10.00)
    self.assertEqual('weight must be > 0', str(cm.exception))

  def test_validated(self) -> None:
    from src.metaprogramming.descriptors import LineItem2
    with self.assertRaises(ValueError) as cm:
      walnuts = LineItem2('walnuts', 0, 10.00)
    self.assertEqual('weight must be > 0', str(cm.exception))

    with self.assertRaises(ValueError) as cm:
      walnuts = LineItem2('', 0, 10.00)
    self.assertEqual('description cannot be blank', str(cm.exception))


class TestOverrdingOrNonOverridingDescriptor(unittest.TestCase):
  def test_overrding_descriptor(self) -> None:
    from src.metaprogramming.descriptor_kind import Managed
    obj = Managed()
    obj.over
    # -> Overrding.__get__(<Overrding object>, <Managed object>, <class Managed>)
    Managed.over
    # -> Overrding.__get__(<Overrding object>, None, <class Managed>)
    obj.over = 7
    # -> Overrding.__set__(<Overrding object>, <Managed object>, 7)
    obj.over
    # -> Overrding.__get__(<Overrding object>, <Managed object>, <class Managed>)
    obj.__dict__['over'] = 8  # bypass descriptor
    self.assertDictEqual({'over': 8}, vars(obj))
    obj.over  # Managed.over descriptor still override reading obj.over
    # -> Overrding.__get__(<Overrding object>, <Managed object>, <class Managed>)

  def test_overrding_descriptor_without_get(self) -> None:
    from src.metaprogramming.descriptor_kind import Managed, OverridingNoGet
    obj = Managed()
    # no __get__, return the descriptor instance
    print(obj.over_no_get)
    # <src.metaprogramming.descriptor_kind.OverridingNoGet object at 0x00000213FB9E71D0>
    self.assertIsInstance(obj.over_no_get, OverridingNoGet)
    print(Managed.over_no_get)
    # <src.metaprogramming.descriptor_kind.OverridingNoGet object at 0x00000213FB9E71D0>
    self.assertIsInstance(Managed.over_no_get, OverridingNoGet)
    obj.over_no_get = 7
    # -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    print(obj.over_no_get)
    # <src.metaprogramming.descriptor_kind.OverridingNoGet object at 0x00000213FB9E71D0>
    self.assertIsInstance(obj.over_no_get, OverridingNoGet)
    obj.__dict__['over_no_get'] = 9
    # instance attribute 'over_no_get' shadow the descriptor, only for reading
    self.assertEqual(9, obj.over_no_get)
    obj.over_no_get = 7
    # -> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
    self.assertEqual(9, obj.over_no_get)

  def test_nonoveriding_descriptor(self) -> None:
    from src.metaprogramming.descriptor_kind import Managed
    obj = Managed()
    obj.non_over
    # -> NonOverrding.__get__(<NonOverrding object>, <Managed object>, <class Managed>)
    obj.non_over = 7  # no __set__
    self.assertEqual(7, obj.non_over)
    Managed.non_over
    # -> NonOverrding.__get__(<NonOverrding object>, None, <class Managed>)
    del obj.non_over
    obj.non_over  # hit class __get__
    # -> NonOverrding.__get__(<NonOverrding object>, <Managed object>, <class Managed>)

  def test_overwrite_descriptor(self) -> None:
    from src.metaprogramming.descriptor_kind import Managed
    obj = Managed()
    # through assignment to class
    Managed.over = 1  # type: ignore[assignment]
    Managed.over_no_get = 2  # type: ignore[assignment]
    Managed.non_over = 3  # type: ignore[assignment]
    self.assertTupleEqual((1, 2, 3),
                          (obj.over, obj.over_no_get, obj.non_over))

  def test_methods_are_nonoverrding_descriptor(self) -> None:
    from src.metaprogramming.descriptor_kind import Managed
    obj = Managed()
    print(obj.spam)  # a bound method object
    # <bound method Managed.spam of <src.metaprogramming.descriptor_kind.Managed object at 0x000001EE6A77F080>>
    print(Managed.spam)  # a function
    # <function Managed.spam at 0x000001EE7FB8E660>

    # shadow class attribute
    obj.spam = 7  # type: ignore[method-assign, assignment]
    self.assertEqual(7, obj.spam)

    import collections

    class Text(collections.UserString):
      def __repr__(self) -> str:
        return 'Text({!r})'.format(self.data)

      def reverse(self) -> Text:
        return self[::-1]

    word = Text('forward')
    self.assertEqual("Text('forward')", repr(word))
    # method call on class
    self.assertEqual("Text('drawkcab')", Text.reverse(Text('backwward')))
    self.assertEqual("Text('drawrof')", repr(word.reverse()))
    # function
    self.assertIsInstance(Text.reverse, FunctionType)
    # method
    self.assertIsInstance(word.reverse, MethodType)
    # __get__ with instance: bound method
    self.assertIsInstance(Text.reverse.__get__(word), MethodType)
    # __get__ without instance: function
    self.assertIsInstance(Text.reverse.__get__(None, Text), FunctionType)
    self.assertEqual("Text('forward')",
                     repr(word.reverse.__self__))  # type: ignore[attr-defined]
    self.assertIs(word.reverse.__func__,  # type: ignore[attr-defined]
                  Text.reverse)
