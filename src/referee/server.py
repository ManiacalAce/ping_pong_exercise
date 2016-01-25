import threading

from flask import (Flask, request, jsonify, abort)

from player import Player
from tournament import (
    MAX_TOURNEY_PLAYERS, connected_players, start_tournament
)


app = Flask(__name__)
logger = app.logger


@app.route('/tournament/connect/', methods=['POST'])
def connect():
    player_id = int(request.form['player_id'])
    player_host = request.form['player_host']
    player_port = int(request.form['player_pot'])

    # Players shouldn't be able to 'reset' data by re-connecting
    if player_id in connected_players:
        # TODO: Return proper error message
        return abort(400)
    else:
        player = Player(player_id, player_host, player_port)
        connected_players[player_id] = player

    remaining_players = (MAX_TOURNEY_PLAYERS - len(connected_players))
    logger.info(
        'Player ID: {} connected!\nWaiting for {} more players...'.format(
            player_id, remaining_players
        )
    )

    # When the final player joins, kick off the tourney
    if len(connected_players) == MAX_TOURNEY_PLAYERS:
        t = threading.Thread(target=start_tournament)
        t.start()

    return jsonify(**{
        'status': 'ok'
    })


if __name__ == '__main__':
    app.run(debug=True)


'''
TODO

- get host, port of player from request for later use.
- Authentication

Refactoring:
- move BL out of routes and into service files
- Error handling
    - int-ing of POST data
- Re-evaluate name of endpoints
'''
