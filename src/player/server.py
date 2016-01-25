from flask import Flask, jsonify, request
import requests

from player import Player


player = Player()
app = Flask('ping_pong_player:' + str(player.id))
logger = app.logger


@app.route('/choose-number/')
def choose_number():
    player.choose_number()
    return jsonify(**{
        'chosen_number': player.get_chosen_number()
    })


@app.route('/make-defense-matrix/')
def make_defense_matrix():
    player.make_defense_matrix()
    return jsonify(**{
        'defense_matrix': player.get_defense_matrix()
    })


def _shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the werkzeug server')
    func()


@app.route('/shutdown/', methods=['POST'])
def shutdown():
    _shutdown_server()
    msg = 'Player {} is shutting down...'.format(player.id)
    logger.info(msg)
    return msg


def connect_to_referee():
    # TODO: Add retrying logic
    referee_host = 'localhost'
    referee_port = 5000
    url = 'http://{host}:{port}/tournament/connect/'.format(
        host=referee_host, port=referee_port
    )
    requests.post(url, data={
        'player_id': player.id,
        'player_host': player.host,
        'player_port': player.port
    })

    # TODO: This logger doesn't work since 'app' isn't runnning yet.
    logger.info('Player ID: {} is connected to server!'.format(player.id))
    logger.info('what')


if __name__ == '__main__':
    # TODO: Do this asynchronously so server is allowed to start? grequests?
    connect_to_referee()

    app.run(debug=True, port=player.port)


'''
TODO

- Fix pre-app.run() logging.
- Take port as param (or randomize)

Refactoring:
    - Move BL out of routes and into service file

'''
