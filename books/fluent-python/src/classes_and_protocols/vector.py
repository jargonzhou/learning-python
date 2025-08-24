"""
A multidimensional vector.
"""

from collections.abc import Sized, Iterable
from array import array
import functools
import itertools
import math
import operator
import reprlib
from typing import Any, Iterator, SupportsIndex, Union

# mypy: disable-error-code="call-overload"


class Vector:
  """Vector: an immutable flat sequence"""

  typecode = 'd'
  __match_args__ = ('x', 'y', 'z', 't')

  def __init__(self, components: Iterable[Any]) -> None:
    # array representation, protected
    self._components: array = array(self.typecode, components)

  def __iter__(self) -> Iterator[Any]:
    return iter(self._components)

  def __repr__(self) -> str:
    # limited length representation: ex array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])
    components = reprlib.repr(self._components)
    components = components[components.find('['):-1]
    return f'Vector({components})'

  def __str__(self) -> str:
    return str(tuple(self))

  def __bytes__(self) -> bytes:
    return bytes([ord(self.typecode)]) + bytes(self._components)

  # hashing, ==
  def __eq__(self, other: Any) -> bool:
    if isinstance(other, Vector):
      return len(self) == len(other) \
          and all(a == b for a, b in zip(self, other))
    else:
      return NotImplemented

  def __hash__(self) -> int:
    hashes = (hash(x) for x in self)
    return functools.reduce(operator.xor, hashes, 0)

  # operator overloading: abs(), -, +
  def __abs__(self) -> float:
    return math.hypot(*self)

  def __neg__(self) -> 'Vector':
    return Vector(-x for x in self)

  def __pos__(self) -> 'Vector':
    return Vector(self)

  # operator overloading: addition +
  def __add__(self, other: Any) -> 'Vector':
    try:
      pairs = itertools.zip_longest(self, other, fillvalue=0.0)
      return Vector(a + b for a, b in pairs)
    except TypeError:
      return NotImplemented

  def __radd__(self, other: Any) -> 'Vector':
    # Returning Any from function declared to return "Vector"
    # return self + other
    return self.__add__(other)

  # operator overloading: multiplication *
  def __mul__(self, scalar: Any) -> 'Vector':
    try:
      factor = float(scalar)
    except TypeError:
      return NotImplemented
    return Vector(n * factor for n in self)

  def __rmul__(self, scalar: Any) -> 'Vector':
    return self.__mul__(scalar)

  # operator overloading: @
  def __matmul__(self, other: Any) -> Any:
    if isinstance(other, Sized) and isinstance(other, Iterable):
      if len(self) == len(other):
        return sum(a * b for a, b in zip(self, other))
      else:
        raise ValueError('@ requires vectors of equal length')
    else:
      return NotImplemented

  def __rmatmul__(self, other: Any) -> Any:
    return self.__matmul__(other)

  def __bool__(self) -> bool:
    return bool(abs(self))

  # sequence protocol: __len__, __getitem__

  def __len__(self) -> int:
    return len(self._components)

  def __getitem__(self, key: Union[slice, SupportsIndex]) -> Any:
    if isinstance(key, slice):  # slice
      cls = type(self)
      return cls(self._components[key])
    index: int = operator.index(key)  # call __index__ method
    return self._components[index]

  # dynamic attributes

  def __getattr__(self, name: str) -> Any:
    cls = type(self)
    try:
      pos = cls.__match_args__.index(name)
    except ValueError:
      pos = -1
    if 0 <= pos < len(self._components):
      return self._components[pos]
    msg = f'{cls.__name__!r} object has no attribute {name!r}'
    raise AttributeError(msg)

  def __setattr__(self, name: str, value: Any) -> None:
    cls = type(self)
    if len(name) == 1:
      if name in cls.__match_args__:
        error = 'readonly attribute {attr_name!r}'
      elif name.islower():
        error = "can't set attributes 'a' to 'z' in {cls_name!r}"
      else:
        error = ''
      if error:
        msg = error.format(cls_name=cls.__name__, attr_name=name)
        raise AttributeError(msg)
    # for standard behavior
    super().__setattr__(name, value)

  def angle(self, n: int) -> float:
    """angle"""
    r = math.hypot(*self[n:])
    a = math.atan2(r, self[n-1])
    if (n == len(self) - 1) and (self[-1] < 0):
      return math.pi * 2 - a
    else:
      return a

  def angles(self) -> Iterable[float]:
    """angles"""
    return (self.angle(n) for n in range(1, len(self)))

  # formating

  def __format__(self, fmt_spec: str = '') -> str:
    if fmt_spec.endswith('h'):  # hyperspherical coordinates
      fmt_spec = fmt_spec[:-1]
      coords: Union[itertools.chain[float], 'Vector'] = itertools.chain(
          [abs(self)], self.angles())
      outer_fmt = '<{}>'
    else:
      coords = self
      outer_fmt = '({})'
    components = (format(c, fmt_spec) for c in coords)
    return outer_fmt.format(', '.join(components))

  @classmethod
  def frombytes(cls, octets: bytes) -> 'Vector':
    """class constructor"""
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(memv)
