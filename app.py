from flask import Flask, flash, render_template, redirect, request, url_for
from flask_login import current_user, LoginManager, login_required, login_user
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login = LoginManager(app)

from forms import LoginForm, RegistrationForm
from models import Guest3, User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Courtesy of Flask Mega-Tutorial
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



# Courtesy of Flask Mega-Tutorial
@app.route('/register', methods=['GET', 'POST'])
def register():
    # if not current_user.is_authenticated or current_user.username != "jonathan.brelje":
    #    return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/rsvp', methods=['GET'])
def rsvp_get():
	name = request.args.get('name')
	headOfParty = Guest3.query.filter_by(name = name).first()
	if not headOfParty:
		# Guest name doesn't exist, render try again page
		return render_template('guest_not_found.html')

	group = Guest3.query.filter_by(party = headOfParty.party).order_by(Guest3.id.asc())

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
@login_required
def get_guest_status():
	guests = Guest3.query.filter_by().order_by(Guest3.party.asc(), Guest3.id.asc())
	return render_template('gueststatus.html', guests=guests)
     


if __name__ == '__main__':
    app.run()