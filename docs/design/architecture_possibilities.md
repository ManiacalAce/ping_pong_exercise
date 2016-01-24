# Approaches to Architecture

## 1. Using Sockets

- Sockets are usually the chosen approach when it comes to 2-way communication
    between processes.

### Thoughts

- The problem statement specifically states (multiple times) that communication
    has to happen between processes via a RESTful approach.
    - Is the problem that it is 'RESTful' or is the problem actually the fact
        that I'm interpreting 'RESTful' as being http-based? (sockets w/ REST
        possible??)
- Not gonna explore variants of socket approach since problem asks to use REST.

------------------------------------------------------------------------------

## 2. REST - Referee is a server, players are clients. Clients poll server.

- Ref listens

### Thoughts

- Players keep 'polling' the referee. This is awkward and wasteful of
    resources.

------------------------------------------------------------------------------

## 3.1 REST - Referee and all players are RESTful endpoints. Players are 'passive' entities.

- Players are 'passive'. They have endpoints that may be accessed by the
    referee, but don't do anything themselves beyond making 'connect' requests.

### Flow

1. R is up and listens.
2. P1-P8 connect
    - P -> R: /connect/
3. When R gets the final 'connect' request, we proceed to the drawing phase.
4. R draws games. (This info is stored somewhere with R)
5. Process game:
    - For each game:
        - P1 = attacking player, P2 = defending player
        - While P1 score or P2 score is not 5:
            - R -> P1: /choose-number/ (returns number)
            - R -> P2: /make-defense-matrix/ (returns matrix)
            - Determine winner of round
            - Increment score
            - Determine new values of P1 and P2
        - Determine winning player and losing player
        - R informs losing player to shut down
            - R -> P: /shut-down/
6. R continues to draw games while there are players available.
7. When the final game completes, winner is declared.
8. Export a report with game details.
9. End.

### Thoughts

- What if later, we want the players to be controlled by humans? Can players
    still be 'passive' endpoints with this requirement?
        - Player process would become a 'server' to a UI client that the human
            interacts with.
            - Not too bad for a solution.
- (???) Players have no capability to 'cheat' (they can't make out-of-turn requests
    to other players, etc.). They just adhere to a certain 'interface' that is
    enforced by the referee.
- For step 3, how do we 'start' with the next phase if we wish to immediately
    return a 'OK' response on every connect?
    - Hand off the next phase to a thread? And that thread will make requests
        to the 'player' processes?
    - Alternative would be to block and do everything else, then finally return
        the 'OK' response for the final player's 'connect' request. This is
        very weird.

------------------------------------------------------------------------------

## 3.2 REST - Referee and all players are RESTful endpoints. Players are 'active' entities.

-

## Thoughts

------------------------------------------------------------------------------
# Implementation

- Servers are involved. Possible choices for RESTful approach:
    - simple http from Python's standard library? (too verbose?)
    - Django? (overkill?)
    - Flask? (lighter than Django, but still overkill?)


# Misc Questions

- The size of a defending player's matrix - should this be held by the player
    (as the problem suggests) or the server (to prevent fraud)?
