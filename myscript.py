import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# to read .env files
load_dotenv()

# configs
app = Flask(__name__)
app.config["SECRET_KEY"] = "my random secret key"
basedir = os.path.abspath(os.path.dirname(__file__))  # project's root directory
sqlite_db_path = os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + sqlite_db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Models 

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


@app.route('/')
def homepage():
    return 'Welcome to Flask.'

if __name__ == '__main__':
    # app.run(debug=True, port=8001)
    app.run(debug=True)