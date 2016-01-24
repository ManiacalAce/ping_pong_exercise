

MAX_TOURNEY_PLAYERS = 2
connected_players = set()  # should be stored in some persistent storage


class Player:
    """Server side representation of a 'player'.

    Actual players are independent services that must conform to a specfic
    RESTful interface. The implementation details are up to whoever codes up
    the player service.

    This class is responsible for wrapping an actual player endpoint.
    """

    def __init__(self):
        self.id = None
        self.remote_host = None
        self.remote_port = None

        self._chosen_number = 0
        self._defense_matrix = set()

    def choose_number(self):
        pass

    def get_chosen_number(self):
        return self._chosen_number

    def make_defense_matrix(self):
        pass

    def get_defense_matrix(self):
        pass
