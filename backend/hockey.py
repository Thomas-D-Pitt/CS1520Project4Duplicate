from flask import Flask, render_template, request, abort

import random, string, json

app = Flask(__name__)

class Team():
	PossibleTeamNames = ['Meerkats', 'Elephants', 'Antelopes', 'Seals', 'Seagulls', 'Starfish',
						'Deer', 'Rabbits', 'Squirrels', 'Flamingos', 'Salamanders', 'Cranes']
	def __init__(self, name):
		self.name = name
		self.players = []

	def __repr__(self):
		result =  F"name: {self.name}\nplayers:\n"
		for player in self.players:
			result += F"\t{player}\n"

		return result

class Player():
	def __init__(self, position, team):
		self.name = randomString().capitalize()
		self.position = position
		self.goals = random.randrange(0, 10)
		self.assists = random.randrange(0, 10)
		self.team = team

	def __repr__(self):
		return F"name: {self.name}, team: {self.team}, position: {self.position}, goals: {self.goals}, assists: {self.assists}"

def randomString(minLength = 4, maxLength = 8):
	length = random.randrange(minLength, maxLength + 1)
	return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def getAllTeams():
	teams = []

	for name in Team.PossibleTeamNames:
		teams.append(getTeam(name))

	return teams

def getTeam(teamName):

	teamName = teamName.capitalize()

	random.seed(teamName)

	createdTeam = Team(teamName)

	for i in range(6):
		createdTeam.players.append(Player('D', createdTeam.name).__dict__)
	for i in range(3):
		createdTeam.players.append(Player('LW', createdTeam.name).__dict__)
	for i in range(3):
		createdTeam.players.append(Player('RW', createdTeam.name).__dict__)
	for i in range(3):
		createdTeam.players.append(Player('C', createdTeam.name).__dict__)

	return createdTeam.__dict__

def getTeamObject(teamName):

	teamName = teamName.capitalize()

	random.seed(teamName)

	createdTeam = Team(teamName)

	for i in range(6):
		createdTeam.players.append(Player('D', createdTeam.name).__dict__)
	for i in range(3):
		createdTeam.players.append(Player('LW', createdTeam.name).__dict__)
	for i in range(3):
		createdTeam.players.append(Player('RW', createdTeam.name).__dict__)
	for i in range(3):
		createdTeam.players.append(Player('C', createdTeam.name).__dict__)

	return createdTeam

@app.route("/")
def root_page():
	return render_template("base.html")

@app.route('/teams/<path:teamName>', methods=['GET'])
def teamName(teamName):
	if teamName in Team.PossibleTeamNames:
		return json.dumps(getTeam(teamName))
	else:
		abort(404)

@app.route('/teams/', methods=['GET'])
def teams():
	return json.dumps(Team.PossibleTeamNames)

if __name__ == "__main__":
	app.run()
	#print(getTeamObject('Elephants'))
