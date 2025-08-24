"""
Unit test of type hints in functions.

PEP 484: a gradual type system - 一个渐进的类型系统

type checker:
- pytype: Google
- Pyright: Microsoft
- Pyre: Facebook
- Mypy

type annotations: typing module
- Any
- simple types and classes
- Optional, Union
- generic collections: including tuples, mappings
- abstract base classes
- generic iterables
- parameterized generics, TypeVar
- Protocls: staic ducking type
- Callable
- NoReturn
"""

import unittest
from typing import Callable, Mapping, NamedTuple, NoReturn, Optional, Any
from collections.abc import Iterable, Sequence

from src.data_structures.card_deck import FrenchDeck
from src.function_as_objects.birds import Bird, Duck, alert, alert_bird, alert_duck

# pylint: skip-file


def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
  if count == 1:
    return f'1 {singular}'
  count_str = str(count) if count else 'no'
  if not plural:
    plural = singular + 's'
  return f'{count_str} {plural}'


class TestTypeHint(unittest.TestCase):
  def test_show_count(self) -> None:
    self.assertEqual('2 childs', show_count(2, 'child'))
    self.assertEqual('2 children', show_count(2, 'child', 'children'))

  def test_type(self) -> None:
    daffy = Duck()
    alert(daffy)
    alert_duck(daffy)
    alert_bird(daffy)

    woody = Bird()
    try:
      alert(woody)
    except AttributeError as e:
      # 'Bird' object has no attribute 'quack'
      print(e)
    # Argument 1 to "alert_duck" has incompatible type "Bird"; expected "Duck"
    # try:
    #   alert_duck(woody)
    # except AttributeError as e:
    #   # 'Bird' object has no attribute 'quack'
    #   print(e)
    try:
      alert_bird(woody)
    except AttributeError as e:
      # 'Bird' object has no attribute 'quack'
      print(e)


class TestTypeAnnotation(unittest.TestCase):
  def test_any(self) -> None:
    def double(x: Any) -> Any:
      return x * 2

    # Unsupported operand types for * ("object" and "int")
    # def double2(x: object) -> object:
    #   return x * 2

  def test_simple_types_classes(self) -> None:
    deck = FrenchDeck()

  def test_optional_type(self) -> None:
    pass

  def test_union_type(self) -> None:
    pass

  def test_generic_collections(self) -> None:
    def tokenize(text: str) -> list[str]:
      return text.upper().split()

  def test_tutple_types(self) -> None:
    # as records
    def geohash(lat_lon: tuple[float, float]) -> str:
      return f'{lat_lon[0]} {lat_lon[1]}'

    # as records with named fields

    class Coordinate(NamedTuple):
      lat: float
      lon: float

    def geohash2(lat_lon: Coordinate) -> str:
      return f'({lat_lon.lat} {lat_lon.lon})'

    # as immutable sequences

    def columnize(sequence: Sequence[str], num_columns: int = 0) -> list[tuple[str, ...]]:
      return [tuple(sequence[i]) for i in range(num_columns)]

  def test_generic_mapping(self) -> None:
    import sys

    def name_index(start: int = 32, end: int = sys.maxunicode+1) -> dict[str, set[str]]:
      result: dict[str, set[str]] = {}
      return result

  def test_abstract_base_class(self) -> None:
    """
    collections.abc
    numbers
    """
    def name2hex(name: str, color_map: Mapping[str, int]) -> str:
      return ''

  def test_iterable(self) -> None:
    """
    Sequence
    Iterable
    """
    def fsum(seq: Iterable[float]) -> float:
      return 0.0

  def test_parameterized_generics(self) -> None:
    from typing import TypeVar
    T = TypeVar('T')

    def sample(population: Sequence[T], size: int) -> list[T]:
      if size < 1:
        raise ValueError('size must >= 1')
      result = list(population)
      return result[:size]

    # restricted TypeVar
    from decimal import Decimal
    from fractions import Fraction
    NumberT = TypeVar('NumberT', float, Decimal, Fraction)

    def mode(data: Iterable[NumberT]) -> NumberT:
      from collections import Counter
      pairs = Counter(data).most_common(1)
      if len(pairs) == 0:
        raise ValueError('empty data')
      return pairs[0][0]

    # bounded TypeVar
    from collections.abc import Hashable
    HashableT = TypeVar('HashableT', bound=Hashable)

    def mode2(data: Iterable[HashableT]) -> HashableT:
      from collections import Counter
      pairs = Counter(data).most_common(1)
      if len(pairs) == 0:
        raise ValueError('empty data')
      return pairs[0][0]

    # typing.AnyStr

  def test_static_protocols(self) -> None:
    from typing import Protocol, TypeVar

    class SupportsLessThan(Protocol):
      def __lt__(self, other: Any) -> bool:
        return False

    LT = TypeVar('LT', bound=SupportsLessThan)

    def top(series: Iterable[LT], length: int) -> list[LT]:
      return sorted(series, reverse=True)[:length]

  def test_callable(self) -> None:
    def repl(input_fn: Callable[[Any], str] = input) -> None:
      input()

    # there are variants in Python!!!

  def test_no_return(self) -> None:
    def _exit() -> NoReturn:
      exit()


class TestParameterAnnotaion(unittest.TestCase):
  def test_tag(self) -> None:
    def tag(name: str,
            /,
            *content: str,
            class_: Optional[str] = None,
            **attrs: str) -> str:
      return ''

    # PEP484 convention
    def tag2(__name: str, *content: str, class_: Optional[str] = None,
             **attrs: str) -> str:
      return ''
