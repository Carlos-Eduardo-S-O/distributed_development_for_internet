# This service returns the ranking of the best csgo teams in the world of all time
from flask import Flask, jsonify, request
from pymemcache.client import base

# Flask service
service = Flask(__name__)

# Service data
IS_ALIVE = 'yes'
DEBUG    = True
HOST     = '0.0.0.0'
PORT     = 5000

#service info
AUTHOR      = "Carlos Eduardo"
EMAIL       = "carlos.edu.estudos@gmail.com"
VERSION     = "1.0"
DESCRIPTION = "Provides the best teams of all time"

# Database host
DATABASE = "data_base"

# This route provides the information about the service is working or not
@service.route("/best_teams_of_all_time/isalive")
def is_alive():
    return IS_ALIVE

# This route provides service informations
@service.route("/best_teams_of_all_time/info")
def get_info():
    return jsonify(
        author = AUTHOR,
        email = EMAIL,
        version = VERSION,
        decription = DESCRIPTION
    )

# This route is the responsible to write the best teams of all time list
@service.route("/best_teams_of_all_time/write", methods=["POST", "GET"])
def write_teams_of_all_time():
    teams = request.get_json()
    
    if teams:
        client = base.Client((DATABASE, 11211))
        client.set("teams_of_all_time", teams)

    return "Ok"

# Main route return the top players
@service.route("/best_teams_of_all_time")
def get_best_team_of_all_time():
    response = "error: o ranking de melhors times de todos os tempos não foi incializado."
    
    client = base.Client((DATABASE, 11211))
    teams = client.get("teams_of_all_time")
    
    if teams:
        response = teams
    
    return response

if __name__ == "__main__":
    service.run(
        debug= DEBUG,
        host= HOST,
        port=PORT
    )