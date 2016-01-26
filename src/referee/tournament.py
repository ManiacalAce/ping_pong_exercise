import logging


logger = logging.getLogger(__name__)


"""
A 'tournament' has 'stages'. A 'stage' has 'games'. Each game is between
two players and consists of multiple rounds. Each round occurs between an
'attacker' and a 'defender'.

Tournament > Stage > Game > Round
"""


class Round:
    """Represents a single round of a game, between an attacker and a
    defender.
    """

    def __init__(self, attacker, defender):
        self._attacker = attacker
        self._defender = defender
        self._winner = None

    def start(self):
        """Run the round and return the winning player"""

        attacker_number = self._attacker.get_chosen_number()
        defender_matrix = self._defender.get_defense_matrix()

        if attacker_number in defender_matrix:
            self._winner = self._defender
        else:
            self._winner = self._attacker

    def get_winner(self):
        return self._winner

    def get_result_summary(self):
        pass


class Game:
    """Represents a single game of a stage. A game is between two players and
    can have multiple rounds.
    """

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2

    def run():
        # determine order of play
        # begin various rounds
        pass

    def _determine_who_goes_first(self):
        return self._player1


class Stage:
    """Represents a stage in a tournament."""

    def __init__(self, from_players):
        """
        params:
            from_players:
                An iterable of player instances from which we create this
                tournament stage. Games will be drawn for these players.
        """
        self.title = 'Stage X'  # TODO: Handle titles for reporting.

        self._games = self._draw_games(from_players)

    def _draw_games(player_pool):
        return []


class Tournament:
    """Encapsulates a 'tournament'.

    This is a class because we might want to allow multiple tournaments on our
    server.
    """

    def __init__(self, max_players=8):
        self._connected_players = {}  # player_id -> player

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
    - 'Stage' and 'Game' as their own entities?
    - Reporting
        - stage titles

    - Make 'winning' score configurable.
    - If a player can't be reached for a certain interval, he must forfeit the
        round/game.
    - Custom exceptions
    - Design 'Game' class to facilitate games between > 2 players?
        - Can be done, but assuming it's unnecessary.


    - 8 players
        - Stage 1
            - 8 players, 4 games, 4 winners
        - Stage 2
            - 4 players, 2 games, 2 winners
        - Stage 3
            - 2 players, 1 game, 1 winner

    - Have active players list
    - While len(active_players) > 1:
        - stage = make_stage(active_players) # stage with relevant no. of games
        - for game in stage.games:
            - game.start()
'''
