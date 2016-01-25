import threading

from flask import Flask, request, jsonify

from tournament import (MAX_TOURNEY_PLAYERS, connected_players)


app = Flask(__name__)
logger = app.logger


def start_tourney():
    logger.info('Ready to beigin! Look whos joined!')
    logger.info(connected_players)


@app.route('/tournament/connect/', methods=['POST'])
def connect():
    player_id = int(request.form['player_id'])
    connected_players.add(player_id)
    # TODO: Disallow reconnects

    logger.info('Player ID: {} connected!'.format(player_id))

    # When the final player joins, kick off the tourney
    if len(connected_players) == MAX_TOURNEY_PLAYERS:
        t = threading.Thread(target=start_tourney)
        t.start()

    return jsonify(**{
        'status': 'ok'
    })


if __name__ == '__main__':
    app.run(debug=True)


'''
TODO

- get host, port of player from request for later use.

Refactoring:
- move BL out of routes and into service files
- Error handling
    - int-ing of POST data
'''
