from enum import Enum, IntEnum


class Suit(str, Enum):
    Hearts = "hearts"
    Spades = "spades"
    Clubs = "clubs"
    Diamonds = "diamonds"

    @classmethod
    def list(cls):
        return list(map(lambda c: c, cls))


class Rank(IntEnum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

    @classmethod
    def list(cls):
        return list(map(lambda c: c, cls))


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        if isinstance(suit, str) and not isinstance(suit, Suit):
            self.suit = Suit[suit]
        if isinstance(rank, str) and not isinstance(rank, Rank):
            self.rank = Rank[rank]

        if not isinstance(self.suit, Suit):
            raise TypeError(
                f"Expected suit to be a Suit or string, got {type(suit).__name__}"
            )
        if not isinstance(self.rank, Rank):
            raise TypeError(
                f"Expected rank to be a Rank or string, got {type(rank).__name__}"
            )

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"
