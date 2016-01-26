import random


DEFENSE_MATRIX_SIZE = 5  # TODO: Read this from config
CHOSEN_NUMBER_RANGE = (1, 11)  # Upper limit excluded


class Player:
    """Represents a 'player' of a tournament
    """

    def __init__(self):
        self.id = random.randrange(1, 100000000)  # for testing
        self.host = 'localhost'
        self.port = random.randrange(5001, 11000)

        self._chosen_number = 0
        self._defense_matrix = set()

    def choose_number(self):
        self._chosen_number = random.randrange(*CHOSEN_NUMBER_RANGE)

    def get_chosen_number(self):
        return self._chosen_number

    def make_defense_matrix(self):
        self._defense_matrix = random.sample(
            range(*CHOSEN_NUMBER_RANGE), DEFENSE_MATRIX_SIZE
        )

    def get_defense_matrix(self):
        return self._defense_matrix


'''
TODO:
    - Is there repetition between this 'Player' and the one on the referee
    server?
    - Read defense matrix length from some config

'''
