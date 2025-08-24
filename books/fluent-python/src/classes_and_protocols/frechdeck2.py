"""
FrechDeck2: a subclass of collections.MutableSequence
"""

from collections import namedtuple, abc
from typing import Union, Any, override

Card2 = namedtuple('Card2', ['rank', 'suit'])


class FrenchDeck2(abc.MutableSequence):
  """Card Deck"""
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  # 黑桃, 方块, 梅花, 红心
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self) -> None:
    self._cards: list[Card2] = [Card2(rank, suit) for suit in self.suits
                                for rank in self.ranks]

  def __len__(self) -> int:
    return len(self._cards)

  @override
  def __getitem__(self, position: Union[int, slice]) -> Any:
    return self._cards[position]

  @override
  def __setitem__(self, positon: Union[int, slice], value: Any) -> None:
    self._cards[positon] = value

  @override
  def __delitem__(self, positon: Union[int, slice]) -> None:
    del self._cards[positon]

  @override
  def insert(self, index: int, value: Card2) -> None:
    self._cards.insert(index, value)
