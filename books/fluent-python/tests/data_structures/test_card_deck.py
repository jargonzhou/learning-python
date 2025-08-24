"""
Unit test of FrenchDeck
"""

# why need 'src' here???
from src.data_structures.card_deck import FrenchDeck, Card
import unittest

# pylint: skip-file


class TestFrenchDeck(unittest.TestCase):
  def setUp(self) -> None:
    self.deck = FrenchDeck()

  def test_len(self) -> None:
    self.assertEqual(52, len(self.deck))

  def test__get_item__(self) -> None:
    self.assertEqual(Card(rank='2', suit='spades'), self.deck[0])
    # self.assertListEqual([Card(rank='2', suit='spades'),
    #                       Card(rank='3', suit='spades'),
    #                       Card(rank='4', suit='spades')],
    #                      self.deck[:3])
    # iterable
    for card in self.deck:
      print(card)
    # __contains__
    self.assertTrue(Card('Q', 'hearts') in self.deck)

  def test_sort(self) -> None:
    # 黑桃 > 红心 > 方块 > 梅花
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    print(suit_values)

    def spades_high(card: Card) -> int:
      rank_value = FrenchDeck.ranks.index(card.rank)
      return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(self.deck, key=spades_high):
      print(card)
