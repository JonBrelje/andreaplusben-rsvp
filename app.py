from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Guest3


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/rsvp', methods=['GET'])
def rsvp_get():
	name = request.args.get('name')
	headOfParty = Guest3.query.filter_by(name = name).first()
	if not headOfParty:
		# Guest name doesn't exist, render try again page
		return render_template('guest_not_found.html')

	group = Guest3.query.filter_by(party = headOfParty.party)

	rehearsal = False
	for guest in group:
		if guest.rehearsalInvite == 1:
			rehearsal = True
	welcome = False
	for guest in group:
		if guest.welcomeReceptionInvite == 1:
			welcome = True

	return render_template('rsvp.html', party = group, rehearsal = rehearsal, welcome = welcome)

@app.route('/rsvp', methods=['POST'])
def rsvp_post():
	i = 1
	while request.form.get("id"+str(i)):
		id = request.form.get("id"+str(i))
		guest = Guest3.query.filter_by(id = id).first()
		if guest.rehearsalInvite:
			guest.rehearsalRSVPStatus = request.form.get("rehearsalRSVPStatus" + str(id))
			guest.rehearsalFoodChoice = request.form.get("rehearsalFoodChoice" + str(id))
		if guest.welcomeReceptionInvite:
			guest.welcomeReceptionRSVPStatus = request.form.get("welcomeReceptionRSVPStatus" + str(id))
		guest.receptionRSVPStatus = request.form.get("receptionRSVPStatus" + str(id))
		guest.receptionFoodChoice = request.form.get("receptionFoodChoice" + str(id))

		if request.form.get("comment" + str(id)):
			guest.comment = request.form.get("comment" + str(id))
		db.session.commit()
		i += 1
	return render_template('saved.html')



@app.route("/gueststatus", methods=['GET'])
def get_guest_status():
   guests = Guest3.query.filter_by()
   return render_template('gueststatus.html', guests=guests)
     


if __name__ == '__main__':
    app.run()