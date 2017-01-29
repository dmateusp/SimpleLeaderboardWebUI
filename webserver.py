from flask import Flask, url_for, jsonify, render_template
import sqlite3

app = Flask(__name__)

def toDict(team):
	return {'team': team[0], 'score': team[1]}

def getSubmissions():
	conn = sqlite3.connect('../submissions.db')
	c = conn.cursor()
	c.execute("SELECT * FROM SUBMISSIONS")
	submissions = c.fetchall()

	submissions_dict = list(map(toDict,submissions))
	return submissions_dict

# Returns the leaderboard in JSON format
@app.route('/api/leaderboard')
def leaderboard():
	return jsonify(getSubmissions())

# Returns the leaderboard in HTML
@app.route('/html/leaderboard')
def htmlLeaderboard():
	teams = getSubmissions()
	return render_template('leaderboard.html', teams=teams)

# Returns the homepage
@app.route('/')
def index():
	return render_template('index.html')