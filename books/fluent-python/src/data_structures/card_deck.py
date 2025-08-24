"""
1. The Python Data Model
A deck as a sequence of playing cards
"""

import collections
from typing import Iterator
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
  """Card Deck"""
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  # 黑桃, 方块, 梅花, 红心
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self) -> None:
    self._cards = [Card(rank, suit) for suit in self.suits
                   for rank in self.ranks]
    self.index = 0

  def __len__(self) -> int:
    return len(self._cards)

  def __getitem__(self, position: int) -> Card:
    return self._cards[position]

  # TODO: the __xxx__ protocols

  def __contains__(self, card: Card) -> bool:
    return card in self._cards

  def __iter__(self) -> 'FrenchDeck':
    return self

  def __next__(self) -> Card:
    try:
      item = self._cards[self.index]
    except IndexError as e:
      raise StopIteration(e) from e
    self.index += 1
    return item
