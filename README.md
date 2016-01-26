
## Solution to the 'ping pong championship' coding problem

**Note**: Still a work in progress!

The solution uses Python 3.

To run http servers, the Flask library is also used.


## Installation

Clone the repository.

```sh
$ git clone git@github.com:ManiacalAce/ping_pong_exercise.git
```

Then go into the project and install the dependencies.

```sh
$ cd ping_pong_exercise/

$ pip install -r requirements/dev.txt
```

Run the demo.

```sh
$ python src/run.py
```

**Note**: `src/run.py` currently doesn't work. It wll be implemented soon!


## Design

A few approaches were considered - some still need to be explored further.
Some of these approaches and related thoughts are described in the notes file
[architecture_possibilities](docs/design/architecture_possibilities.md).

The final approach chosen is the one titled `3.1 REST - Referee and all players
are RESTful endpoints. Players are 'passive' entities.` The program 'flow' is
also described.
Please refer to the file mentioned above.

The notes aren't complete, but should still give some insights on the various
reasonings.


## Pending Items

### Critical
* `src/run.py` to launch the demo.
* The reporting module.
* Loading player information from a config file.
* Authentication

### Enhancements
* Explore the 'active player' approach of solving this problem.
* Never used Flask before, so need to read up on any best practices that the
    Flask community follows.
* Need to organize config stuff - debug mode is hardcoded currently.
* Refactoring can be done in various places once core functionality is done.
