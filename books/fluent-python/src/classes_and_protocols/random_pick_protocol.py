"""
A static protocol similar to Tombol.
"""
# pylint: disable="too-few-public-methods"


import random
from typing import Iterable, Protocol, runtime_checkable, Any


@runtime_checkable
class RandomPicker(Protocol):
  """random picker protocol"""

  def pick(self) -> Any:
    """pick"""


class SimplePicker:
  """use to runtime check"""

  def __init__(self, items: Iterable) -> None:
    self._items = list(items)
    random.shuffle(self._items)

  def pick(self) -> Any:
    """pick"""
    return self._items.pop()


@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
  """extend static protocol"""

  def load(self, items: Iterable) -> None:
    """load"""
