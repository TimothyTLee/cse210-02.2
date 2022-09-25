import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.


# 2) Create the class constructor. Use the following method comment.


# 3) Create the roll(self) method. Use the following method comment.


class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.

    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
    value = 0
    points = 0

    """Constructs a new instance of Die with a value and points attribute.

    Args:
        self (Die): An instance of Die.
    """

    def __init__(self):
        value = 0
        ponts = 0

    """ calculates point based off values

    Args:
        self (Die): An instance of Die
    """

    def get_calc(self):
        if self.value == 1:
            return 100
        elif self.value == 5:
            return 50
        return 0

    """Generates a new random value and calculates the points.

    Args:
        self (Die): An instance of Die.
    """

    def roll(self):
        self.value = random.randint(1, 6)
        self.points = self.get_calc()

    """Resets the die back to it's initial state

    Args:
        self (Die): An instance of Die.
    """

    def reset(self):
        self.value = 0
        self.points = 0
