from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
	teamName = db.Column(db.String(20), primary_key=True)

	def __init__(self, teamName):
		self.teamName = teamName

class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	position = db.Column(db.String(2), nullable=False)
	goals = db.Column(db.Integer, nullable=False)
	assists = db.Column(db.Integer, nullable=False)
	team = db.Column(db.String(20), db.ForeignKey('user.user_id'))