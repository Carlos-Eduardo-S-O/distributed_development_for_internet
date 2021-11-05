# This service returns the ranking of the best players in the world
from flask import Flask, jsonify, json

# Flask service
service = Flask(__name__)

# Service data
IS_ALIVE = 'yes'
DEBUG    = True
HOST     = '0.0.0.0'
PORT     = 5000

#service info
AUTHOR  = "Carlos Eduardo"
EMAIL   = "carlos.edu.estudos@gmail.com"
VERSION = "1.0"

# Dictionaries
TOP_PLAYERS = 'service/assets/top_playes/best_players.json'

# Load file
def load_file():
    players = None
    
    # Open the file and get the list of players
    with open(TOP_PLAYERS, 'r') as file:
        list = json.load(file)
        players = list["players"]

    return players
    

# This route provides the information about the service is working or not
service.route("/players/isalive")
def is_alive():
    return IS_ALIVE

# This route provides service informations
def info():
    return jsonify(
        
    )

# Main route return the top players
service.route('/players')
def top_players():
    pass

if __name__ == '__main__':
    service.run(
        debug
    )