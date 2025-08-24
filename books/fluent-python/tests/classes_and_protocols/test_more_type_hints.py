"""
Unit test of more type hints

overloaded function signature
- `@overload`

`typing.TypedDict`

type casting
- `typing.cast()`

runtime access to type hints
- import time: `__annotations__`
- PEP 563
- `typing.get_type_hints`, `inspect.get_annotations`

generic types
- `typing.Generic`
- jargon
  - generic type: LottoBlower[T]
  - formatl type parameter: T
  - parameterized type: LottoBlower[int]
  - actual type parameter: int
- variance
- generic static protocol: example `SupportAbs`
"""
# pylint: skip-file


import unittest


class TestOverload(unittest.TestCase):
  def test_max(self) -> None:
    # see https://github.com/python/typeshed/issues/4051
    # mypy: disable-error-code="call-overload,type-var"
    # with self.assertRaises(TypeError) as cm:
    #   # Value of type variable "SupportsRichComparisonT" of "max" cannot be "int | None"Mypytype-var
    #   max([1, None])
    # self.assertTrue("'NoneType' object is not iterable", str(cm.exception))
    ...

  def test_mymax(self) -> None:
    from src.classes_and_protocols.mymax import mymax, SupportLessThan
    # Value of type variable "LT" of "mymax" cannot be "None"Mypytype-var
    # mymax([None])

    self.assertEqual(2, mymax([1, 2, -3]))
    self.assertEqual('Rust', mymax(['Go', 'Python', 'Rust']))

    # with key
    self.assertEqual(-3, mymax([1, 2, -3], key=abs))
    self.assertEqual('Python', mymax(['Go', 'Python', 'Rust'], key=len))

    # with default
    self.assertEqual(2, mymax([1, 2, -3], default=0))
    self.assertIsNone(mymax([], default=None))

    # with key, default
    self.assertEqual(-3, mymax([1, 2, -3], key=abs, default=None))
    # Argument "key" to "mymax" has incompatible type "Callable[[SupportsAbs[_T]], _T]"; expected "Callable[[object], Never]"Mypyarg-type
    # self.assertIsNone(mymax([], key=abs, default=None))


# mypy: disable-error-code="attr-defined,assignment, typeddict-unknown-key,misc"

class TestTypedDict(unittest.TestCase):
  def test_book(self) -> None:
    from src.classes_and_protocols.books import BookDict
    # constructor expected a dict
    book = BookDict(title='Programming Pearls',
                    authors=['Jon Bentley'],
                    isbn='0201657880',
                    pagecount=256)
    self.assertTrue(isinstance(book, dict))
    with self.assertRaises(AttributeError) as cm:
      # mypy: disable-error-code="attr-defined"
      # "BookDict" has no attribute "title"
      book.title
    self.assertEqual("'dict' object has no attribute 'title'",
                     str(cm.exception))
    self.assertEqual('Programming Pearls', book['title'])
    # the field type hint
    self.assertIsInstance(BookDict.__annotations__, dict)
    print(BookDict.__annotations__)

    # illegal operations
    authors = book['authors']
    # Incompatible types in assignment (expression has type "str", variable has type "list[str]")
    authors = 'Bob'
    # TypedDict "BookDict" has no key "weight"
    book['weight'] = 4.2
    # Key "title" of TypedDict "BookDict" cannot be deleted
    del book['title']
    print(book)


class TestGeneric(unittest.TestCase):
  def test_lotto_blower(self) -> None:
    from src.classes_and_protocols.tombola_generic import LottoBlower

    # No overload variant of "range" matches argument types "int", "float"
    # machine = LottoBlower[int](range(1, .2))

    machine = LottoBlower[int](range(1, 11))
    self.assertIsNotNone(machine.pick())
    self.assertIsNotNone(machine.inspect())

    # Argument 1 to "load" of "LottoBlower" has incompatible type "str"; expected "Iterable[int]"
    # machine.load('ABC')

  def test_generic_static_protocol(self) -> None:
    # SupportsAbs
    import math
    from typing import NamedTuple, SupportsAbs

    class Vector2d(NamedTuple):
      x: float
      y: float

      def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def is_unit(v: SupportsAbs[float]) -> bool:
      return math.isclose(abs(v), 1.0)

    self.assertTrue(issubclass(Vector2d, SupportsAbs))

    v0 = Vector2d(0, 1)
    sqrt2 = math.sqrt(2)
    v1 = Vector2d(sqrt2/2, sqrt2 / 2)
    v2 = Vector2d(1, 1)
    v3 = complex(.5, math.sqrt(3) / 2)
    v4 = 1
    self.assertTrue(is_unit(v0))
    self.assertTrue(is_unit(v1))
    self.assertFalse(is_unit(v2))
    self.assertTrue(is_unit(v3))
    self.assertTrue(is_unit(v4))

    # Protocol
    from typing import TypeVar, Protocol, runtime_checkable
    T_co = TypeVar('T_co', covariant=True)

    @runtime_checkable
    class RandomPicker(Protocol[T_co]):
      def pick(self) -> T_co: ...


class TestVariance(unittest.TestCase):
  def test_invariant(self) -> None:
    from src.classes_and_protocols.variance import Beverage, Juice, OrangeJuice, BeverageDispenser, install
    juice_dispenser = BeverageDispenser(Juice())
    install(juice_dispenser)

    beverage_dispenser = BeverageDispenser(Beverage())
    # Argument 1 to "install" has incompatible type "BeverageDispenser[Beverage]"; expected "BeverageDispenser[Juice]"
    # install(beverage_dispenser)

    # invariant
    orange_juice_dispenser = BeverageDispenser(OrangeJuice())
    # Argument 1 to "install" has incompatible type "BeverageDispenser[OrangeJuice]"; expected "BeverageDispenser[Juice]"
    # install(orange_juice_dispenser)

  def test_covariant(self) -> None:
    from src.classes_and_protocols.variance import BeverageDispenserCo, Beverage, Juice, OrangeJuice, install_co
    juice_dispenser = BeverageDispenserCo(Juice())
    install_co(juice_dispenser)
    orange_juice_dispenser = BeverageDispenserCo(OrangeJuice())
    install_co(orange_juice_dispenser)

    beverage_dispenser = BeverageDispenserCo(Beverage())
    # Argument 1 to "install_co" has incompatible type "BeverageDispenserCo[Beverage]"; expected "BeverageDispenserCo[Juice]"
    # install_co(beverage_dispenser)

  def test_contravirant(self) -> None:
    from src.classes_and_protocols.variance import TrashCan, Refuse, Biodegradable, Compostable, deploy
    bio_can: TrashCan[Biodegradable] = TrashCan()
    deploy(bio_can)
    trash_can: TrashCan[Refuse] = TrashCan()
    deploy(trash_can)

    compost_can: TrashCan[Compostable] = TrashCan()
    # Argument 1 to "deploy" has incompatible type "TrashCan[Compostable]"; expected "TrashCan[Biodegradable]"
    # deploy(compost_can)
