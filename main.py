from deck.deck import Deck

if __name__ == "__main__":
    deck = Deck()
    print(f"Deck Cards length: {len(deck._cards)}")

    print("Shuffling Deck...")
    shuffle_return = deck.shuffle()
    
    print(f"Deck Cards length after shuffle: {len(deck._cards)}")
    print(f"Deck shuffle return: {shuffle_return}")

    hand = [deck.deal_one_card() for i in range(len(deck.cards))]
    for idx, card in enumerate(hand):
        print(f"Card {idx} - {card}")

    no_result = deck.deal_one_card()
    print(f"Card dealt from empty deck - {no_result}")
