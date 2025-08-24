"""
1. The Python Data Model
Two dimensional vector.
"""
# pylint: skip-file
import math


class Vector:
  def __init__(self, x: int = 0, y: int = 0) -> None:
    self.x = x
    self.y = y

  def __repr__(self) -> str:
    """repr: for console, debugger"""
    return f'Vector({self.x!r}, {self.y!r})'

  def __str__(self) -> str:
    """str: for print"""
    return f'Vector({self.x}, {self.y})'

  def __abs__(self) -> float:
    """abs"""
    return math.hypot(self.x, self.y)

  def __bool__(self) -> bool:
    """boolean value"""
    return bool(abs(self))

  def __add__(self, other: 'Vector') -> 'Vector':  # 'Vector': forward declaration reference
    """+"""                                        # https://github.com/microsoft/pylance-release/issues/2182
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)

  def __mul__(self, scalar: int) -> 'Vector':
    """*"""
    return Vector(self.x * scalar, self.y * scalar)

  def __eq__(self, other: object) -> bool:
    """=="""
    if isinstance(other, Vector):
      return self.x == other.x and self.y == other.y
    else:
      return False
