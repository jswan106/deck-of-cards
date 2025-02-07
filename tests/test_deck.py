import unittest
from deck.card import Card
from deck.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        """Test that a deck is correctly initialized"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertIsInstance(deck.cards[0], Card)

    def test_deck_shuffle(self):
        """Test that a deck can be shuffled correctly"""
        deck = Deck()

        # Store the order before shuffling
        original_order = deck.cards[:]

        shuffle_return = deck.shuffle()
        self.assertIsNone(shuffle_return)

        # Store the order after shuffling
        shuffled_order = deck.cards[:]

        # Ensure the shuffled order is different from the original
        self.assertNotEqual(
            original_order, shuffled_order, "Shuffle did not change card order"
        )

        # Ensure all original cards are still present after shuffle
        self.assertCountEqual(
            original_order, shuffled_order, "Shuffle changed the set of cards"
        )

    def test_deck_deal_one_card(self):
        """Test that a deck can deal one card"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        top_card = deck.cards[-1]
        card = deck.deal_one_card()

        # Ensure exactly 1 card was dealt from the top of the deck (index 0)
        self.assertIsNotNone(card)
        self.assertEqual(card, top_card)
        self.assertEqual(len(deck.cards), 51)

        # Ensure that if the deck has no cards, no card will be dealt
        deck._cards = []
        self.assertEqual(len(deck.cards), 0)
        no_card = deck.deal_one_card()
        self.assertIsNone(no_card)

    def test_deck_final_requirements(self):
        """Test that the deck correctly fulfills the requirements of the project"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

        # Store the orders before and after shuffling
        original_order = deck.cards[:]
        deck.shuffle()
        shuffled_order = deck.cards[:]
        self.assertNotEqual(
            original_order, shuffled_order, "Shuffle did not change card order"
        )

        # Deal all cards in the deck
        result_cards = [deck.deal_one_card() for i in range(len(deck.cards))]
        self.assertEqual(len(result_cards), 52)

        # Reverse order of the shuffle_order list to match way the cards are dealt
        shuffled_order.reverse()
        self.assertEqual(
            shuffled_order, result_cards, "Cards were not dealt properly after shuffle"
        )
        none_card = deck.deal_one_card()
        self.assertIsNone(none_card)


if __name__ == "__main__":
    unittest.main()
