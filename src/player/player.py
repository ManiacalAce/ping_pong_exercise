import random


DEFENSE_MATRIX_SIZE = 5


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
        self._chosen_number = random.randrange(1, 11)

    def get_chosen_number(self):
        return self._chosen_number

    def make_defense_matrix(self):
        self._defense_matrix = [
            random.randrange(1, 11) for _ in range(0, DEFENSE_MATRIX_SIZE)
        ]

    def get_defense_matrix(self):
        return self._defense_matrix


'''
TODO:
    - Is there repetition between this 'Player' and the one on the referee
    server?
    - Read defense matrix length from some config

'''
