# This service returns the ranking of the best csgo teams in the world
from flask import Flask, jsonify, json

# Flask service
service = Flask(__name__)

# Service data
IS_ALIVE = 'yes'
DEBUG    = True
HOST     = '0.0.0.0'
PORT     = 5000

# Dictionaries
TOP_TEN = ''

# Load file
def load_file():
    pass

# This route provides the information about the service is working or not
def is_alive():
    pass

# This route provides service informations
def info():
    pass

# Main route return the top players
service.route('/')
def top_ten_players():
    pass
