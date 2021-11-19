# This service returns the ranking of the best csgo teams in the world of all time
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
TOP_TEAMS = 'service/assets/top_teams_of_all/best_teams_of_all.json'

# Load file with the best teams of all time
def load_teams():
    teams = None
    
    # Open the file and get the list of teams
    with open(TOP_TEAMS, 'r') as file:
        list = json.load(file)
        teams = list["teams"]

    return teams

# This route provides the information about the service is working or not
@service.route("/best_teams_of_all_time/isalive")
def is_alive():
    return IS_ALIVE

# This route provides service informations
@service.route("/best_teams_of_all_time/info")
def info():
    return jsonify(
        AUTHOR,
        EMAIL,
        VERSION
    )

# Main route return the top players
@service.route('/best_teams_of_all_time')
def top_ten_players():
    players = load_teams()
    
    return jsonify(
        players
    )

if __name__ == "__main__":
    service.run(
        debug= DEBUG,
        host= HOST,
        port=PORT
    )