"""
Vector.
- final version: P.378
"""

from __future__ import annotations

import array
import math
from typing import Any, Iterator, SupportsComplex, Union

# mypy: disable-error-code="call-overload"


class Vector2d:
  """Vector"""
  # support positional pattern matching
  __match_args__ = ('x', 'y')

  # for saving memory
  __slots__ = ('__x', '__y')

  # convert to/from bytes
  typecode = 'd'

  def __init__(self, x: float, y: float) -> None:  # float ???
    # convert to float
    # private attribute: store in __dict__
    # prefix _: protec attributes by convention
    self.__x: float = float(x)
    self.__y: float = float(y)

  @property  # read-only property
  def x(self) -> float:
    """x"""
    return self.__x

  @property
  def y(self) -> float:
    """y"""
    return self.__y

  def __iter__(self) -> Iterator[float]:
    # make unpacking work
    # use generator expression
    return (i for i in (self.x, self.y))

  def __repr__(self) -> str:
    class_name = type(self).__name__
    # pylint: disable=consider-using-f-string
    return '{}({!r}, {!r})'.format(class_name, *self)  # *self: __iter__

  def __str__(self) -> str:
    return str(tuple(self))

  def __bytes__(self) -> bytes:
    return bytes([ord(self.typecode)]) + bytes(array.array(self.typecode, self))

  def __eq__(self, other: Any) -> bool:
    # isinstance(other, Vector2d) and
    # use tuple to compare
    return tuple(self) == tuple(other)

  def __ne__(self, other: Any) -> bool:
    eq_result = self == other
    if eq_result is NotImplemented:
      return NotImplemented
    else:
      return not eq_result

  def __hash__(self) -> int:  # hashable
    return hash((self.x, self.y))  # immutable: read-only property

  def __abs__(self) -> float:
    return math.hypot(self.x, self.y)

  def __bool__(self) -> bool:
    # 0.0 => False
    return bool(abs(self))

  def __len__(self) -> int:
    return 2

  def angle(self) -> float:
    """angle"""
    return math.atan2(self.y, self.x)

  def __format__(self, fmt_spec: str = '') -> str:
    # for f-string, format(), str.format()
    if fmt_spec.endswith('p'):  # p for polar coordinates
      fmt_spec = fmt_spec[:-1]
      coords: Union[tuple[float, float], Vector2d] = (abs(self), self.angle())
      outer_fmt = '<{}, {}>'
    else:
      coords = self
      outer_fmt = '({}, {})'
    components = (format(c, fmt_spec) for c in coords)
    return outer_fmt.format(*components)

  @classmethod  # class method: the class as the first argument
  def frombytes(cls, octets: bytes) -> 'Vector2d':
    """alternative constructor"""
    _typecode = chr(octets[0])
    # use memoryview
    memv = memoryview(octets[1:]).cast(_typecode)
    return cls(*memv)

  # more
  # __int__: int()
  # __float__: float()
  # __complex__: complex()

  def __complex__(self) -> complex:
    """typing.SupportsComplex protocol"""
    return complex(self.x, self.y)

  # use: from __future__ import annotations
  # def fromcomplex(cls, datum: SupportsComplex) -> 'Vector2d':
  @classmethod
  def fromcomplex(cls, datum: SupportsComplex) -> Vector2d:
    """contruction from complex"""
    c = complex(datum)
    return cls(c.real, c.imag)


class Vector2dWithoutSlots:
  """Vector without slots"""
  # support positional pattern matching
  __match_args__ = ('x', 'y')

  # convert to/from bytes
  typecode = 'd'

  def __init__(self, x: float, y: float) -> None:  # float ???
    # convert to float
    # private attribute: store in __dict__
    # prefix _: protec attributes by convention
    self.__x: float = float(x)
    self.__y: float = float(y)

  @property  # read-only property
  def x(self) -> float:
    """x"""
    return self.__x

  @property
  def y(self) -> float:
    """y"""
    return self.__y

  def __iter__(self) -> Iterator[float]:
    # make unpacking work
    # use generator expression
    return (i for i in (self.x, self.y))

  def __repr__(self) -> str:
    class_name = type(self).__name__
    # pylint: disable=consider-using-f-string
    return '{}({!r}, {!r})'.format(class_name, *self)  # *self: __iter__

  def __str__(self) -> str:
    return str(tuple(self))

  def __bytes__(self) -> bytes:
    return bytes([ord(self.typecode)]) + bytes(array.array(self.typecode, self))

  def __eq__(self, other: object) -> bool:
    # use tuple to compare
    return isinstance(other, Vector2d) and tuple(self) == tuple(other)

  def __hash__(self) -> int:  # hashable
    return hash((self.x, self.y))  # immutable: read-only property

  def __abs__(self) -> float:
    return math.hypot(self.x, self.y)

  def __bool__(self) -> bool:
    # 0.0 => False
    return bool(abs(self))

  def angle(self) -> float:
    """angle"""
    return math.atan2(self.y, self.x)

  def __format__(self, fmt_spec: str = '') -> str:
    # for f-string, format(), str.format()
    if fmt_spec.endswith('p'):  # p for polar coordinates
      fmt_spec = fmt_spec[:-1]
      coords: Union[tuple[float, float], Vector2dWithoutSlots] = (
          abs(self), self.angle())
      outer_fmt = '<{}, {}>'
    else:
      coords = self
      outer_fmt = '({}, {})'
    components = (format(c, fmt_spec) for c in coords)
    return outer_fmt.format(*components)

  @classmethod  # class method: the class as the first argument
  def frombytes(cls, octets: bytes) -> 'Vector2dWithoutSlots':
    """alternative constructor"""
    _typecode = chr(octets[0])
    # use memoryview
    memv = memoryview(octets[1:]).cast(_typecode)
    return cls(*memv)

  # more
  # __int__: int()
  # __float__: float()
  # __complex__: complex()
