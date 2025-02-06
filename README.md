# Deck of Cards

## Overview

This project implements a standard deck of 52 poker-style playing cards. It includes functionality to shuffle the deck and deal cards one at a time. The deck consists of four suits (Hearts, Diamonds, Clubs, and Spades) with thirteen ranks in each suit (Ace, 2-10, Jack, Queen, and King).

## Features

- **Deck of 52 Cards**: Represents a full deck of playing cards.
- **Custom Shuffle Implementation**: Uses the Fisher-Yates algorithm instead of built-in shuffle methods.
- **Efficient Card Dealing**: Follows a Last-In, First-Out (LIFO) approach for O(1) performance when dealing.

## Installation

No external dependencies are required apart from Python.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd deck-of-cards
   ```
2. Ensure you have Python 3 installed.

## Usage

```python
from deck import Deck

deck = Deck()      # Create a new deck
deck.shuffle()     # Shuffle the deck
card = deck.deal_one_card()  # Deal one card
print(card)        # Output: e.g., "King of Hearts"
```

## Project Structure

```
deck-of-cards/
│── deck/
│   ├── __init__.py
│   ├── card.py  # Defines the Card class
│   ├── deck.py  # Implements the Deck class
│── tests/
│   ├── test_card.py  # Unit tests for Card class
│   ├── test_deck.py  # Unit tests for Deck class
│── README.md  # Project documentation
```

## Testing

To run unit tests, use:

```bash
python -m unittest discover tests
```

## License

This project is open-source under the MIT License.

## Notes

- The `shuffle()` method does **not** use `random.shuffle()` as per assignment constraints.
- `deal_one_card()` returns `None` if all cards have been dealt.

## Author

Jordan Swan
