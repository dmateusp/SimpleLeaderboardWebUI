# SimpleLeaderboardWebUI
Leaderboard that plugs into the Competition system.

This Leaderboard uses Flask(Python), HTML and JavaScript to display the leaderboard of the competition

To read more about the Competition system process go [here](https://github.com/dmateusp/CompetitionSubmissionSystem/blob/master/README.md)

## Starting the server
1. Open a terminal on the root of your SimpleLeaderboardWebUI folder
2. `pip install -r requirements.txt`
3. Linux: `export FLASK_APP=webserver.py`, Windows `set FLASK_APP=webserver.py`
4. `python -m flask run` (this will run the server locally, then you can open the webpage on 127.0.0.1:5000/)
5. Alternatively, you can run the server on public host: `python flask run --host=0.0.0.0`

Of course, the CompetitionSubmissionSystem should be running at the same time, it is the one that will populate the Database with the teams' submissions!

## TODO
* Improving UI (a lot)
* Find another way to refresh the leaderboard, it is currently sending an AJAX request to the server every 1.5 seconds which should not be a problem normally in small scale competitions
