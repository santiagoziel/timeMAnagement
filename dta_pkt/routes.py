from flask import  render_template, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user

from dta_pkt import app, login_manager, bcrypt, db
from dta_pkt.forms import LogInForm,RegisterForm
from dta_pkt.models import User, Week

import datetime
import pytz

#if you try to enter a page that requires log in you will be redirected to login
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/deberiaEstar", methods=['GET', 'POST'])
@login_required
def deberiaEstar():
    my_date = datetime.datetime.now(pytz.timezone('America/Mexico_City'))
    moment = Week.query.filter_by(dia = my_date.weekday(), hora = my_date.hour).first()
    return render_template("shouldBeDoing.html", act=moment.act)

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html", user = current_user)

@app.route("/schedule", methods=['GET', 'POST'])
@login_required
def schedule():
    days_to_act = [Week.query.filter_by(dia=idx) for idx in range(7)]
    return render_template("schedule.html",day_to_act = days_to_act)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("deberiaEstar"))
    return render_template("login.html", form = form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username = form.username.data, password= hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form = form)

#error page
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
