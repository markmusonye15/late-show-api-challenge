from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Late Show API!"


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




@app.route('/users')
def users():
    return "List of users will be here."

if __name__ == '__main__':
    app.run()
# This is a simple Flask application that serves as a starting point for the Late Show API.