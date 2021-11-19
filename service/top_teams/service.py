# This service returns the ranking of the best csgo teams in the world
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
TOP_TEAMS = 'service/assets/top_teams/best_teams.json'

# Load file with the best teams today
def load_teams():
    teams = None
    
    # Open the file and get the list of teams
    with open(TOP_TEAMS, 'r') as file:
        list = json.load(file)
        teams = list["teams"]

    return teams

# This route provides the information about the service is working or not
@service.route("/teams/isalive")
def is_alive():
    return IS_ALIVE

# This route provides service informations
@service.route("/teams/info")
def info():
    return jsonify(
        AUTHOR,
        EMAIL,
        VERSION
    )

# Main route return the top teams today
@service.route('/teams')
def top_ten_teams():
    teams = load_teams()
    
    return jsonify(
        teams
    )

if __name__ == "__main__":
    service.run(
        debug= DEBUG,
        host= HOST,
        port=PORT
    )