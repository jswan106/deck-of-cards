from deck.card import Card, Rank, Suit
from deck.deck import Deck

if __name__ == "__main__":
    deck = Deck()
    print(f"Deck Cards length: {len(deck._cards)}")

    print("Shuffling Deck...")
    deck.shuffle()

    print(f"Deck Cards length after shuffle: {len(deck._cards)}")

    first_card = deck.deal_one_card()
    print(f"First Dealt Card - {first_card}")

    second_card = deck.deal_one_card()
    print(f"Second Dealt Card - {second_card}")

    print(f"Deck Cards length after 2 cards were dealt: {len(deck._cards)}")
