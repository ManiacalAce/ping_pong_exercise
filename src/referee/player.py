

class Player:
    """Server side representation of a 'player'.

    Actual players are independent services that must conform to a specfic
    RESTful interface. The implementation details are up to whoever codes up
    the player service.

    This class is responsible for wrapping an actual player endpoint.
    """

    def __init__(self, id, host, port):
        self.id = id
        self.remote_host = host
        self.remote_port = port

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


'''
TODO:
    - Validation (id, host, port, etc.)

'''
