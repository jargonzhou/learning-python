"""
overloaded sum()
"""

from collections.abc import Iterable
import functools
import operator
from typing import Union, TypeVar, overload


T = TypeVar('T')
S = TypeVar('S')


@overload
def mysum(it: Iterable[T]) -> Union[T, int]: ...
@overload
def mysum(it: Iterable[T], /, start: S) -> Union[T, S]: ...

# mypy: disable-error-code="no-untyped-def"


def mysum(it, /, start=0):  # actual implementation: without type hint
  """mysum"""
  return functools.reduce(operator.add, it, start)
