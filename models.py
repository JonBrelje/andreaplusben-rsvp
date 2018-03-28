from app import db
from sqlalchemy.dialects.postgresql import JSON


class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    party = db.Column(db.Integer)
    name = db.Column(db.String())
    rehearsalInvite = db.Column(db.Integer)
    welcomeReceptionInvite = db.Column(db.Integer)
    rehearsalFoodChoice = db.Column(db.String())
    receptionFoodChoice = db.Column(db.String())
    rehearsalRSVPStatus = db.Column(db.Integer)
    welcomeReceptionRSVPStatus = db.Column(db.Integer)
    receptionRSVPStatus = db.Column(db.Integer)
    comment = db.Column(db.String())


    def __init__(self, party, name, rehearsalInvite, welcomeReceptionInvite, rehearsalFoodChoice, receptionFoodChoice,rehearsalRSVPStatus, welcomeReceptionRSVPStatus, receptionRSVPStatus, comment):
        self.party = party
        self.name = name
        self.rehearsalInvite = rehearsalInvite
        self.welcomeReceptionInvite = welcomeReceptionInvite
        self.rehearsalFoodChoice = rehearsalFoodChoice
        self.receptionFoodChoice = receptionFoodChoice
        self.rehearsalRSVPStatus = rehearsalRSVPStatus
        self.welcomeReceptionRSVPStatus = welcomeReceptionRSVPStatus
        self.receptionRSVPStatus = receptionRSVPStatus
        self.comment = comment

    def __repr__(self):
        return '<id {}>'.format(self.id)