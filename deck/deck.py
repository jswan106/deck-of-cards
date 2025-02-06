import random
from deck.card import Card, Rank, Suit


class Deck:
    def __init__(self):
        self._cards = [
            Card(suit=suit, rank=rank) for suit in Suit.list() for rank in Rank.list()
        ]

    def shuffle(self):
        for i in range(len(self._cards) - 1, 0, -1):
            j = random.randint(0, i)  # Pick a random index up to i
            self._cards[i], self._cards[j] = (
                self._cards[j],
                self._cards[i],
            )  # Swap elements

    def deal_one_card(self):
        try:
            return self._cards.pop(0)
        except IndexError:
            return None
