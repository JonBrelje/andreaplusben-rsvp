from app import db, login
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, check_password_hash

# Courtesy of Flask Mega-Tutorial
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#################################################
class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())
    party = db.Column(db.Integer)
    name = db.Column(db.String())
    rehearsalInvite = db.Column(db.Integer)
    welcomeReceptionInvite = db.Column(db.Integer)
    brunchInvite = db.Column(db.Integer)
    rehearsalRSVPStatus = db.Column(db.String())
    welcomeReceptionRSVPStatus = db.Column(db.String())
    receptionRSVPStatus = db.Column(db.String())
    brunchRSVPStatus = db.Column(db.String())
    comment = db.Column(db.Text())


    def __init__(self, code, party, name, rehearsalInvite, welcomeReceptionInvite, brunchInvite, rehearsalRSVPStatus, welcomeReceptionRSVPStatus, receptionRSVPStatus, brunchRSVPStatus, comment):
        self.code = code
        self.party = party
        self.name = name
        self.rehearsalInvite = rehearsalInvite
        self.welcomeReceptionInvite = welcomeReceptionInvite
        self.brunchInvite = brunchInvite
        self.rehearsalRSVPStatus = rehearsalRSVPStatus
        self.welcomeReceptionRSVPStatus = welcomeReceptionRSVPStatus
        self.receptionRSVPStatus = receptionRSVPStatus
        self.brunchRSVPStatus = brunchRSVPStatus
        self.comment = comment

    def __repr__(self):
        return '<id {}>'.format(self.id)

class RSVPChoice(db.Model):
    __tablename__ = "rsvpchoices"

    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String())
    response = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, event, response, date):
        self.event = event
        self.response = response
        self.date = date
