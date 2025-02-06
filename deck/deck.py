import random
from typing import Union
from deck.card import Card, Rank, Suit


class Deck:
    """
    A class representing a standard deck of 52 poker-style playing cards.

    This deck consists of four suits (Hearts, Diamonds, Clubs, and Spades) with
    thirteen ranks in each suit (Ace, 2-10, Jack, Queen, and King). It supports
    operations for shuffling the deck and dealing cards one at a time.

    The deck follows a Last-In, First-Out (LIFO) approach for dealing cards, making
    it efficient with an O(1) time complexity when drawing cards.

    Attributes:
        cards (list): A list of Card objects representing the deck.

    Methods:
        shuffle():
            Shuffles the deck into a random order using the Fisher-Yates algorithm.

        deal_one_card():
            Deals a single card from the top of the deck. Returns None if the deck is empty.
    """

    def __init__(self):
        """
        Initializes a new deck of 52 playing cards.
        """

        self._cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    @property
    def cards(self):
        """
        Provides read-only access to the deck's cards.

        Returns:
            list[Card]: A list of Card objects representing the current deck state.
        """
        return self._cards[:]  # Return a copy to prevent external modification

    def shuffle(self):
        """
        Randomly shuffles the deck using the Fisher-Yates algorithm.

        This method modifies the deck in place by swapping card positions
        to ensure a uniformly random order. It does not return any value.

        The algorithm iterates through the deck from the last card to the first,
        selecting a random index and swapping the current card with the randomly
        chosen card.

        Returns:
            None: This method doesn't return anything

        Example usage:
            deck = Deck()
            deck.shuffle()  # Shuffles the deck in place

        Complexity:
            - Time Complexity: O(n)
            - Space Complexity: O(1) (modifies the deck in place)
        """
        for i in range(len(self._cards) - 1, 0, -1):
            j = random.randint(0, i)  # Pick a random index up to i
            self._cards[i], self._cards[j] = (
                self._cards[j],
                self._cards[i],
            )  # Swap elements

    def deal_one_card(self) -> Union[Card, None]:
        """
        Deals one card from the top of the deck.

        This method removes and returns the top card of the deck, following
        a Last-In, First-Out (LIFO) approach for optimal performance. If the
        deck is empty, it returns None instead of raising an error.

        The LIFO approach ensures that removing a card has O(1) time complexity,
        as it pops from the end of the list. In contrast, a FIFO approach (removing
        from the beginning) would have O(n) complexity due to element shifting.

        Returns:
            Card: The top card from the deck.
            None: If the deck is empty.

        Example usage:
            deck = Deck()
            card = deck.deal_one_card()  # Returns a Card object or None if empty
        """
        try:
            # Removes and returns the last card (top)
            return self._cards.pop()
        except IndexError:
            # Return None if the deck is empty
            return None
