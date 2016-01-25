
MAX_TOURNEY_PLAYERS = 2

# player_id -> player
connected_players = {}  # should be stored in some persistent storage


def start_tournament():
    print('Ready to beigin! Look whos joined!')
    print(connected_players)
