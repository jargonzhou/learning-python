"""
Unit test of interfaces, protocols, ABCs.

Python typing map
- (x) duck typing: default approach
- (x) goose typing: ABCs, runtime check, use `isinstance` - >= 2.6
- static typing: `typing`, use type hint, type checker - >= 3.5 PEP 484
- (x) static duck typing: `typing.Protocol`, Golang approach, use type hint, type checker - >= 3.8 PEP 544

protocols:
- an object protocol specifies methods which an object must provide to fulfill a role
- an informal interface: just implement part of the methods
- meaning in Python: closely related, but different
- kind:
  - dynamic protocol: implicit, defined by convention, supported by interpreter
  - static protocol: PEP 544, a `typing.Protocol` subclass, can be verified by static type checker
- example: sequence and iterable protocol

monkey patching: implementing a protocol at runtime
- dynamically change a module/class/function at runtime, to add feature or fix bugs

ABC(abstract base class): define explicit interfaces
- `collections.abc`
  - Iterable, Container, Sized
  - Collection
  - Sequence, Mapping, Set
  - MappingView
  - Iterator
  - Callable, Hashable
- `io`
- `numbers`
- example: Tombola, BingoCage, LotteryBlower, TomboList

static protocols
- `typing.Protocol`
- `@runtime_checkable`
- `typing.SupportsComplex`, `typing.SupportsFloat`
- `numbers` ABC: `Integral`, `Real`, `Complex`, `Number` - fine for runtime check
- numeric protocol: ex `typing.SupportsComplex` - fine for static typing
"""

import abc
from typing import TYPE_CHECKING, Any, Iterable, Union, override, reveal_type
import unittest
import collections

from numpy import isin

# pylint: skip-file
# mypy: disable-error-code="arg-type,index,union-attr,abstract"


class TestDuckTyping(unittest.TestCase):
  def test_monkey_patching(self) -> None:
    # shuffle deck
    from src.data_structures.card_deck import FrenchDeck, Card
    from random import shuffle
    deck = FrenchDeck()
    with self.assertRaises(TypeError) as cm:
      # mypy: disable-error-code="arg-type"
      shuffle(deck)
    self.assertEqual("'FrenchDeck' object does not support item assignment",
                     str(cm.exception))

    def set_card(deck: FrenchDeck, position: int, card: Card) -> None:
      deck._cards[position] = card

    # changing a class/module at runtime
    # mypy: disable-error-code="index"
    FrenchDeck.__setitem__ = set_card
    shuffle(deck)
    print(deck[:3])

  def test_fail_fast(self) -> None:
    def handle_str_or_iterable_of_str(
            input_filed_names: Union[str, Iterable[str]]) -> None:
      try:  # assume it's str
        # mypy: disable-error-code="union-attr"
        field_names = input_filed_names.replace(',', ' ').split()
      except AttributeError:
        pass
      # now it's a iterable of str
      field_names = tuple(input_filed_names)
      if not all(s.isidentifier() for s in field_names):
        raise ValueError('field_names must all be valid identifier')

    handle_str_or_iterable_of_str('a')
    handle_str_or_iterable_of_str(['a'])


class TestGooseTyping(unittest.TestCase):
  def test_ABC(self) -> None:
    from src.classes_and_protocols.tombola_abc import Tombola

    class Fake(Tombola):
      @override
      def pick(self) -> Any:
        return 13
    # mypy: disable-error-code="abstract"
    with self.assertRaises(TypeError) as cm:
      f = Fake()
    self.assertTrue(str(cm.exception).index(
        "Can't instantiate abstract class Fake") != -1)

  def test_virtual_subclass(self) -> None:
    # @XXX.register
    from src.classes_and_protocols.tombola_abc import Tombola, TomboList
    self.assertTrue(TomboList, Tombola)
    tl = TomboList(range(10))
    self.assertTrue(isinstance(tl, Tombola))

    # mro: method resolution order
    self.assertEqual("(<class 'src.classes_and_protocols.tombola_abc.TomboList'>, <class 'list'>, <class 'object'>)",
                     str(TomboList.__mro__))

  def test_structural_typing(self) -> None:
    # Sized: __subclasshook__ check attribute __len__
    class Struggle:
      def __len__(self) -> int:
        return 23
    self.assertTrue(isinstance(Struggle(), collections.abc.Sized))
    self.assertTrue(issubclass(Struggle, collections.abc.Sized))


class TestStaticProtocols(unittest.TestCase):
  def test_double(self) -> None:
    from src.classes_and_protocols.double_protocol import double, Repeatable
    d = double(1.0)
    self.assertAlmostEqual(2.0, d)

    # @runtime_checkable
    self.assertTrue(isinstance(d, Repeatable))
    self.assertTrue(issubclass(float, Repeatable))

  def test_runtime_checkable(self) -> None:
    # __complex__
    from typing import SupportsComplex
    import numpy as np
    c64 = np.complex64(3+4j)
    self.assertTrue(c64, complex)
    self.assertTrue(c64, SupportsComplex)

    c = complex(c64)
    self.assertTrue(isinstance(c, SupportsComplex))

    # Complex ABC
    import numbers
    self.assertTrue(isinstance(c64, numbers.Complex))
    self.assertTrue(isinstance(c, numbers.Complex))

    # __float__
    from typing import SupportsFloat
    import sys
    c = 3 + 4j
    print(sys.version)
    self.assertFalse(isinstance(c, SupportsFloat))  # True in Python 3.9

  def test_support_static_protocol(self) -> None:
    from src.classes_and_protocols.vector2d import Vector2d
    from typing import SupportsComplex, SupportsAbs
    v = Vector2d(3, 4)
    self.assertFalse(isinstance(v, complex))
    self.assertTrue(isinstance(v, SupportsComplex))
    self.assertTrue(isinstance(v, SupportsAbs))

  def test_random_pick(self) -> None:
    from src.classes_and_protocols.random_pick_protocol import RandomPicker, SimplePicker
    rp: RandomPicker = SimplePicker([1])
    self.assertTrue(isinstance(rp, RandomPicker))

    items = [1, 2]
    rp = SimplePicker(items=items)
    item = rp.pick()
    self.assertTrue(item in items)
    if TYPE_CHECKING:
      # output of Mypy: Revealed type is "Any"
      reveal_type(item)
    self.assertTrue(isinstance(item, int))
