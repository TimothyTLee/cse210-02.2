from director import Director

# Runner is the main method for the game in charge
#  creating and starting the director


class Runner():

    def __init__(self):
        director = Director()
        director.start_game()


# Starting the runner on program start
Runner()
