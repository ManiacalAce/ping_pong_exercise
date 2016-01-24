import threading

from flask import Flask, request, jsonify


app = Flask(__name__)

MAX_TOURNEY_PLAYERS = 2
connected_players = set()  # should be stored in some persistent storage


def start_tourney():
    print('Ready to beigin! Look whos joined!')
    print(connected_players)


@app.route('/tournament/connect/', methods=['POST'])
def connect():
    player_id = int(request.form['player_id'])
    connected_players.add(player_id)

    print('Player ID: {} connected!'.format(player_id))

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
