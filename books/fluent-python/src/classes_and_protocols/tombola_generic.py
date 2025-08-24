"""
Example of generic classes.
"""

# mypy: disable-error-code="override"

from collections.abc import Iterable
import random
from typing import Generic, Tuple, TypeVar, override

from .tombola_abc import Tombola


T = TypeVar('T')


class LottoBlower(Tombola, Generic[T]):
  """a generic Tombola"""

  def __init__(self, items: Iterable[T]) -> None:
    self._balls = list[T](items)

  @override
  def load(self, iterable: Iterable[T]) -> None:
    self._balls.extend(iterable)

  @override
  def pick(self) -> T:
    try:
      position = random.randrange(len(self._balls))
    except ValueError as e:
      raise LookupError('pick from empty LottoBlower') from e
    return self._balls.pop(position)

  @override
  def loaded(self) -> bool:
    return bool(self._balls)

  def inspect(self) -> Tuple[T, ...]:
    return tuple(self._balls)
