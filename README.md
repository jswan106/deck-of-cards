# Deck of Cards Code Sample Assignment
Your assignment is to code a set of Python classes that represent a deck of poker-style playing
cards (fifty-two playing cards in four suits: hearts, spades, clubs, diamonds, with face values of
Ace, 2-10, Jack, Queen, and King).

### Requirements
Within one of your classes, you must provide two operations:
1. **shuffle()**
    - Shuffle returns no value, but results in the cards in the deck being randomly permuted. 
    - Please do not use library-provided shuffle operations to implement this function. 
    - You may use library-provided random number generators in your solution if needed.
2. **deal_one_card()**
    - This function should return the card from the "top" of the deck to the caller. 
    - If the deck is empty, no card is dealt.

Specifically, a call to shuffle() followed by 52 calls to deal_one_card() should result in the caller
being provided all 52 cards of the deck in a random order.

Many details of this assignment have been left intentionally vague. Use your best judgement to
come up with reasonable design decisions. If you are torn between two approaches, feel free to
make note of that fact somewhere in your submission, but only submit one answer.

While this is a trivial assignment, pretend that this code will become a foundational part of a new
Strider product. Take whatever measures you feel are required for your code to meet this bar.

### Delivery
This is not a timed test. It is far more important that you do this correctly than it is that you do it
quickly. We are also aware that you may have other obligations, and we will not penalize you for
that. That said, we ask that people submit their response within 3-5 days. If that is not possible,
please let us know. 
