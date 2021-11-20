# This service returns the ranking of the best csgo teams in the world
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
AUTHOR  = "Carlos Eduardo"
EMAIL   = "carlos.edu.estudos@gmail.com"
VERSION = "1.0"
DESCRIPTION = "Provides the best teams today"

# Database host
DATABASE = "data_base"

# This route provides the information about the service is working or not
@service.route("/teams/isalive")
def is_alive():
    return IS_ALIVE

# This route provides service informations
@service.route("/teams/info")
def get_info():
    return jsonify(
        author = AUTHOR,
        email = EMAIL,
        version = VERSION,
        decription = DESCRIPTION
    )

# This route is the responsible to write the team list
@service.route("/teams/write", methods=["POST", "GET"])
def write_teams():
    teams = request.get_json()
    
    if teams:
        client = base.Client((DATABASE, 11211))
        client.set("teams", teams)
    
    return "Ok"

# Main route return the top teams today
@service.route('/teams')
def get_best_teams_of_today():
    response = "error: o ranking de melhores times não foi inicializado."

    client = base.Client((DATABASE, 11211))
    teams = client.get("teams")
    
    if teams:
        response = teams
    
    return response
    
if __name__ == "__main__":
    service.run(
        debug= DEBUG,
        host= HOST,
        port=PORT
    )