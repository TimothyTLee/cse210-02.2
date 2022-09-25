from deck import Deck


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Card]): deals out an available card from a deck of 52.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
        keeps track of score (adds or subtracts for starting score of 300).
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.is_playing = True
        self.total_score = 300
        self.current_card = self.deck.pick_card()
        self.next_card = None

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            hi_lo = self.get_inputs()
            result = self.check_inputs(hi_lo)
            self.do_updates(result)
            self.do_outputs(result)
            self.do_continue()

    def get_inputs(self):
        """Ask the user if the next_card is higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        return input(f"Higher or Lower than {self.current_card.value} {self.current_card.suit} [h/l]")

    def check_inputs(self, hi_lo) -> bool:
        self.next_card = self.deck.pick_card()
        if (self.next_card.value > self.current_card.value and hi_lo == "h") or (self.next_card.value < self.current_card.value and hi_lo == "l"):
            return True
        return False

    def do_updates(self, result) -> None:
        if result:
            self.total_score += 100
        else:
            self.total_score -= 75
        self.current_card = self.next_card
        self.next_card = None

    def do_outputs(self, result):
        """Displays the card  number and suit and shows the current score. Also asks the player if they want to continue play or quit.
            also ends game if player reaches zero. 

        Args:
            self (Director): An instance of Director.
        """
        if(result):
            print(f"You were correct")
        else:
            print(f"You were incorrect")
        print(f"Your score is: {self.total_score}\n")

    def do_continue(self):
        if(self.total_score < 1):
            self.is_playing = False
        else:
            self.is_playing = input("Continue? [y/n]") == "y"
