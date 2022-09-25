import random
from card import Card
from card import Suit


class Deck:
    """ a list of playing cards. 

    The responsibility of a deck to randomize card order and give player cards.

    Attributes:
        cards_available(List [Cards]): A list of card available for game.
        __full_deck (List [Cards]): List of all cards in a deck
    """
    cards_available = []

    __full_deck = [
        Card(2, Suit.HEART),
        Card(3, Suit.HEART),
        Card(4, Suit.HEART),
        Card(5, Suit.HEART),
        Card(6, Suit.HEART),
        Card(7, Suit.HEART),
        Card(8, Suit.HEART),
        Card(8, Suit.HEART),
        Card(10, Suit.HEART),
        Card(11, Suit.HEART),
        Card(12, Suit.HEART),
        Card(13, Suit.HEART),
        Card(14, Suit.HEART),
        Card(2, Suit.DIAMOND),
        Card(3, Suit.DIAMOND),
        Card(4, Suit.DIAMOND),
        Card(5, Suit.DIAMOND),
        Card(6, Suit.DIAMOND),
        Card(7, Suit.DIAMOND),
        Card(8, Suit.DIAMOND),
        Card(8, Suit.DIAMOND),
        Card(10, Suit.DIAMOND),
        Card(11, Suit.DIAMOND),
        Card(12, Suit.DIAMOND),
        Card(13, Suit.DIAMOND),
        Card(14, Suit.DIAMOND),
        Card(2, Suit.SPADE),
        Card(3, Suit.SPADE),
        Card(4, Suit.SPADE),
        Card(5, Suit.SPADE),
        Card(6, Suit.SPADE),
        Card(7, Suit.SPADE),
        Card(8, Suit.SPADE),
        Card(8, Suit.SPADE),
        Card(10, Suit.SPADE),
        Card(11, Suit.SPADE),
        Card(12, Suit.SPADE),
        Card(13, Suit.SPADE),
        Card(14, Suit.SPADE),
        Card(2, Suit.CLUBS),
        Card(3, Suit.CLUBS),
        Card(4, Suit.CLUBS),
        Card(5, Suit.CLUBS),
        Card(6, Suit.CLUBS),
        Card(7, Suit.CLUBS),
        Card(8, Suit.CLUBS),
        Card(8, Suit.CLUBS),
        Card(10, Suit.CLUBS),
        Card(11, Suit.CLUBS),
        Card(12, Suit.CLUBS),
        Card(13, Suit.CLUBS),
        Card(14, Suit.CLUBS),

    ]

    def __init__(self) -> None:
        self.reset_deck()

    def reset_deck(self) -> None:
        """used to reset deck with all 52 cards in an random order.
        """
        self.cards_avaiable = self.__full_deck
        random.shuffle(self.cards_avaiable)

    def pick_card(self) -> Card:
        """picks top card for player.
        """
        if len(self.cards_available) < 1:
            self.reset_deck()
        chosen_card = self.cards_avaiable.pop()
        return chosen_card
