from puppy_company_blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    
    # We shall be using a link as string.
    # nullable=False, because every user will hava a default profile image.
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    
    # What does it mean by 'index=True'
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # passwords are hashed to 128 bit string.
    password_hash = db.Column(db.String(128))
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "Username: {a}".format(a=self.username)


class BlogPost(db.Model):
    
    # setting up the relationship, each blogpost is connected to a user.
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # DateTime storage.
    date = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return "Post Id: {a}, Date: {b}".format(a=self.id, b=self.date)


