import unittest
from deck.card import Card, Rank, Suit


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        """Test that a card is correctly initialized."""
        card = Card(suit="Hearts", rank="Ace")
        self.assertEqual(card.suit.name, "Hearts")
        self.assertEqual(card.rank.name, "Ace")

        card2 = Card(suit=Suit.Clubs, rank=Rank.Four)
        self.assertEqual(card2.suit.name, "Clubs")
        self.assertEqual(card2.rank.name, "Four")

    def test_card_representation(self):
        """Test the string representation of a card."""
        card = Card("Spades", "King")
        self.assertEqual(str(card), "King of Spades")


if __name__ == "__main__":
    unittest.main()
