"""
Use typing.Protocl to define double
"""


# pylint: disable=too-few-public-methods

from typing import TypeVar, Protocol, runtime_checkable

T = TypeVar('T')


@runtime_checkable  # for isinstance/issubclass runtime check
class Repeatable(Protocol):
  """repeatable protocol"""

  def __mul__(self: T, repeat_count: int) -> T:
    pass


# type checker require actual type to implement Repeatable
RT = TypeVar('RT', bound=Repeatable)


def double(x: RT) -> RT:
  """the double function"""
  return x * 2
