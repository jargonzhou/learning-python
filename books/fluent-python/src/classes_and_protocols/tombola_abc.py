"""
Example ABC.
"""

# PEP 3119 – Introducing Abstract Base Classes
import abc
import random
from typing import Any, Iterable, Tuple, override


class Tombola(abc.ABC):  # define an ABC
  """Tombola"""
  @abc.abstractmethod
  def load(self, iterable: Iterable) -> None:
    """add items from an iterable"""

  @abc.abstractmethod
  def pick(self) -> Any:
    """remove item at randome, returning it.

    raise `LookupError` when empty."""

  def loaded(self) -> bool:
    """return `True` if there's at least 1 item, `False` otherwise."""
    return bool(self.inspect())

  def inspect(self) -> Tuple[Any]:
    """return a sorted tuple with items currently inside"""
    items = []
    while True:
      try:
        items.append(self.pick())
      except LookupError:
        break
    self.load(items)
    return tuple(items)


class BingoCage(Tombola):  # extend ABC class
  """BingoCage"""

  def __init__(self, items: list[Any]) -> None:
    self._randomizer = random.SystemRandom()
    self._items: list[Any] = []
    self.load(items)

  @override
  def load(self, iterable: Iterable[Any]) -> None:
    self._items.extend(iterable)
    self._randomizer.shuffle(self._items)

  @override
  def pick(self) -> Any:
    try:
      return self._items.pop()
    except IndexError as e:
      raise LookupError('pick from empty BingoCage') from e

  # extra methods
  def __call__(self) -> Any:
    self.pick()


class LottoBlower(Tombola):
  """LottoBlower"""

  def __init__(self, iterable: Iterable[Any]) -> None:
    self._balls = list(iterable)

  @override
  def load(self, iterable: Iterable[Any]) -> None:
    self._balls.extend(iterable)

  @override
  def pick(self) -> Any:
    try:
      position = random.randrange(len(self._balls))
    except ValueError as e:
      raise LookupError('pick from empty LottoBlower') from e
    return self._balls[position]

  @override
  def loaded(self) -> bool:
    return bool(self._balls)

  @override
  def inspect(self) -> Tuple[Any]:
    return tuple(self._balls)


@Tombola.register  # virtual subclass: extend list
class TomboList(list):
  """a virtual subclass of Tombola"""

  def pick(self) -> Any:
    """pick"""
    if self:
      position = random.randrange(len(self))
      return self.pop(position)
    raise LookupError('pop from empty TomboList')

  load = list.extend

  def loaded(self) -> bool:
    """loaded"""
    return bool(self)

  def inspect(self) -> Tuple[Any]:
    """inspect"""
    return tuple(self)
