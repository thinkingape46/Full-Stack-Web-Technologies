import os
# OAuth is supposed to be used when deployed and not meant to be used locally.
# To make it work we use some environment variables.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

# Flask-Dance
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'anykeyfornow'

blueprint = make_google_blueprint(client_id='220150878126-q2guomog2lqab5p370vbpavn7g5su722.apps.googleusercontent.com', client_secret='2JaUSGc7_hVrJmFdo9bf3Jjl', offline=True, scope=['profile', 'email'])
app.register_blueprint(blueprint, url_prefix='/login')


# Set the templates.

@app.route('/')
def index():    
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    
    # Below lines are to make sure that user doesn't get access to welcome page unless they are logged in.
    resp = google.get('oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))

    resp = google.get('oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)


if __name__=='__main__':
    app.run()