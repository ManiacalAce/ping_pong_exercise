from flask import Flask, request, jsonify


app = Flask(__name__)

MAX_TOURNEY_PLAYERS = 2
connected_players = set()  # should be stored in some persistent storage


@app.route('/tournament/connect/', methods=['POST'])
def connect():
    player_id = int(request.form['player_id'])
    connected_players.add(player_id)
    if len(connected_players) == MAX_TOURNEY_PLAYERS:
        print('Ready to begin!')
    print('Player ID: {} connected!'.format(player_id))
    return jsonify(**{
        'did_it_work': 'yeah',
        'pid': player_id
    })


if __name__ == '__main__':
    app.run(debug=True)


'''
- Thread?
- get host, port of player from request for later use.

Refactoring:
- move BL out of routes and into service files
- Error handling
    - int-ing of POST data
'''
