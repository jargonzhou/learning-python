"""
overload max()
"""

# pylint: disable="too-few-public-methods"

from collections.abc import Callable, Iterable
from typing import Any, Protocol, TypeVar, Union, overload


class SupportLessThan(Protocol):
  """less than protocol"""

  def __lt__(self, other: Any) -> bool: ...


T = TypeVar('T')
LT = TypeVar('LT', bound=SupportLessThan)
DT = TypeVar('DT')
MISSING = object()

EMPTY_MSG = 'mymax() arg is an empty sequence'


# positional argument
@overload
def mymax(__arg1: LT, __arg2: LT, *args: LT,
          key: None = ...) -> LT: ...


@overload
def mymax(__arg1: T, __arg2: T, *args: T,
          key: Callable[[T], LT]) -> T: ...


# iterable
@overload
def mymax(__iterable: Iterable[LT], *,
          key: None = ...) -> LT: ...


@overload
def mymax(__iterable: Iterable[T], *,
          key: Callable[[T], LT]) -> T: ...

# with default


@overload
def mymax(__iterable: Iterable[LT], *,
          key: None = ...,  default: DT) -> Union[LT, DT]: ...


@overload
def mymax(__iterable: Iterable[T], *,
          key: Callable[[T], LT], default: DT) -> Union[T, DT]: ...


# mypy: disable-error-code="no-untyped-def"

def mymax(first, *args, key=None, default=MISSING):
  """mymax"""
  if args:
    series = args
    candidate = first
  else:
    series = iter(first)
    try:
      candidate = next(series)
    except StopIteration:
      if default is not MISSING:
        return default
      raise ValueError(EMPTY_MSG) from None

  if key is None:
    for current in series:
      if candidate < current:
        candidate = current
  else:
    candidate_key = key(candidate)
    for current in series:
      current_key = key(current)
      if candidate_key < current_key:
        candidate = current
        candidate_key = current_key
  return candidate
