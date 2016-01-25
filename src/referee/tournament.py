import logging


logger = logging.getLogger(__name__)


class Tournament:
    """Encapsulates a 'tournament'.

    This is a class because we might want to allow multiple tournaments on our
    server.
    """

    def __init__(self, max_players=8):
        # player_id -> player. Should be stored in some persistent storage.
        self._connected_players = {}

        if (max_players % 2) != 0:
            max_players += 1
        self._max_players = max_players

    def add_player(self, player):
        if player.id in self._connected_players:
            # TODO: Custom exception
            raise ValueError(
                'Player ID: {} is already part of this tournament.'.format(player.id)  #noqa
            )
        if self.is_at_max_capacity():
            raise ValueError('Tournament is at max capacity!')

        self._connected_players[player.id] = player

    def has_player(self, player_id):
        return player_id in self._connected_players

    def get_vacancies(self):
        return self._max_players - len(self._connected_players)

    def is_at_max_capacity(self):
        return self.get_vacancies() == 0

    def start(self):
        pass


'''
TODO:
    - Draw games for various stages
    - If a player can't be reached for a certain interval, he must forfeit the
        round/game.
    - Custom exceptions
'''
