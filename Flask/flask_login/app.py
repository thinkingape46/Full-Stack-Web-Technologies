# app.py

from myproject import app, db
from flask import render_template, url_for, redirect, request, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
# It makes sure that for the user to see the welcome view, they have to login first.
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(message='You have Logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        # Get the user by the email provided.
        # first() is used, because emails will be unique.
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(password=form.password.data) and user is not None:
            login_user(user)
            flash(message='Logged In Succesfully')

            # Next is used when the login view is triggered because tried to visit a page that requires a login.
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User(email, username, password)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registeration')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__=='__main__':
    app.run(debug=True)

