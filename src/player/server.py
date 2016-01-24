import random

from flask import Flask, jsonify
import requests


app = Flask(__name__)
logger = app.logger

DEFENSE_MATRIX_SIZE = 5


@app.route('/choose-number/')
def choose_number():
    number = random.randrange(1, 11)  # Abstract away choosing of number
    return jsonify(**{
        'chosen_number': number
    })


@app.route('/make-defense-matrix/')
def make_defense_matrix():
    matrix = [
        random.randrange(1, 11) for _ in range(0, DEFENSE_MATRIX_SIZE)
    ]
    return jsonify(**{
        'defense_matrix': matrix
    })


def connect_to_referee():
    # TODO: Add retrying logic
    referee_host = 'localhost'
    referee_port = 5000
    url = 'http://{host}:{port}/tournament/connect/'.format(
        host=referee_host, port=referee_port
    )
    player_id = random.randrange(1, 100000000)  # for testing
    requests.post(url, data={
        'player_id': player_id
    })

    # TODO: This logger doesn't work since 'app' isn't runnning yet.
    logger.info('Player ID: {} is connected to server!'.format(player_id))
    logger.info('what')


if __name__ == '__main__':
    # TODO: Do this asynchronously so server is allowed to start? grequests?
    connect_to_referee()

    port = random.randrange(5001, 11000)
    app.run(debug=True, port=port)


'''
TODO

- Fix pre-app.run() logging.
- Read defense matrix length from some config
- Take port as param (or randomize)

Refactoring:
    - Move BL out of routes and into service file

'''
