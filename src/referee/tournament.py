import logging
import random


logger = logging.getLogger(__name__)

WINNING_SCORE = 5  # TODO: Make this configurable?


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
        self._loser = None

    def start(self):
        """Run the round and return the winning player"""

        attacker_number = self._attacker.get_chosen_number()
        defender_matrix = self._defender.get_defense_matrix()

        if attacker_number in defender_matrix:
            self._winner, self._loser = self._defender, self._attacker
        else:
            self._winner, self._loser = self._attacker, self._defender

    def get_winner(self):
        return self._winner

    def get_loser(self):
        return self._loser

    def get_result_summary(self):
        pass


class Game:
    """Represents a single game of a stage. A game is between two players and
    can have multiple rounds.
    """

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        self._winner = None
        self._loser = None

    def start(self):
        attacker, defender = self._determine_order_of_play()
        p1_score, p2_score = 0, 0

        while ((p1_score != WINNING_SCORE) or (p2_score != WINNING_SCORE)):
            attacker.choose_number()
            defender.make_defense_matrix()

            round = Round(attacker, defender)
            round.run()

            round_winner = round.get_winner()
            if round_winner == self._player1:
                p1_score += 1
            elif round_winner == self._player2:
                p2_score += 1

            attacker = round_winner
            defender = round.get_loser()

        if p1_score == WINNING_SCORE:
            self._winner, self._loser = self._player1, self._player2
        elif p2_score == WINNING_SCORE:
            self._winner, self._loser = self._player2, self._player1

    def get_winner(self):
        return self._winner

    def get_loser(self):
        return self._loser

    def get_result_summary(self):
        pass

    def _determine_order_of_play(self):
        """Randomly determines order of play."""
        order_of_play = [self._player1, self._player2]
        # shuffle em up!
        random.shuffle(order_of_play)
        return order_of_play


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
    - Reporting
        - stage titles

    - Make 'winning' score configurable.
    - If a player can't be reached for a certain interval, he must forfeit the
        round/game.
    - Custom exceptions
    - There's comparison happening between player references across different
    classes. Compare only IDs? (like we would do if we had DBs)
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
