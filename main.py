from flask import Flask,jsonify

from flask_migrate import Migrate
from db.config import DATABASE_URI

from db.database import db
from controllers import user_controller

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db.init_app(app)

migrate = Migrate(app, db)

from models.user import User
@app.route('/')
def welcome ():
    return jsonify({"message":"Welcome to the Late Show API!"})


@app.route('/register')
def register():
    return "User registration page will be here."

@app.route('/login')
def login():
    return "User login page will be here."

@app.route('/episodes')
def fetch_all_episodes():
    return "List of episodes will be here."

@app.route('/episodes/<int:episode_id>')
def episode_detail(episode_id):
    return f"Details of episode {episode_id} will be here."

@app.route('/guests')
def fetch_all_guests():
    return "List of guests will be here."

@app.route('/appearances')
def appearances():
    return "List of guest appearances will be here."




@app.route('/users/<int:id>')
def fetch_user(id):
    user = user_controller.get_a_single_user(id)
    if user:
        return jsonify(user), 200
    else:
        return "User not found", 404
    

if __name__ == '__main__':
    app.run()
