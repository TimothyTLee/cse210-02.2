import random
from enum import Enum


class Suit(Enum):
    """symbol tied to a card. 

    Attributes: list of four options avaiable
    """
    HEART = "Heart"
    DIAMOND = "Diamond"
    SPADE = "Spade"
    CLUBS = "Clubs"


class Card:
    """a playing card from a deck of 52. 

    The responsibility of a card is to hold its value and suit.

    Attributes:
        value(int): value of card.
        suit(Suit): suit of card.
    """
    value = 0
    suit = Suit.HEART

    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
