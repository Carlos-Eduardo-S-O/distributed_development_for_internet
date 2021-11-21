# This service returns the ranking of the best players in the world
from flask import Flask, request, jsonify
from pymemcache.client import base

# Flask service
service = Flask(__name__)

# Service data
IS_ALIVE = 'yes'
#IS_ALIVE = 'no'
DEBUG    = True
HOST     = '0.0.0.0'
PORT     = 5000

#service info
AUTHOR  = "Carlos Eduardo"
EMAIL   = "carlos.edu.estudos@gmail.com"
VERSION = "1.0"
DESCRIPTION = "Provides the best players today"

# Database host
DATABASE = "data_base"

# This route provides the information about the service is working or not
@service.route("/players/isalive")
def is_alive():
    return IS_ALIVE

# This route provides service informations
@service.route("/players/info")
def get_info():
    return jsonify(
        author = AUTHOR,
        email = EMAIL,
        version = VERSION,
        decription = DESCRIPTION
    )

# This route is the responsible to write the player list
@service.route("/players/write", methods=["POST", "GET"])
def write_players():
    players = request.get_json()

    if players:
        client = base.Client((DATABASE, 11211))
        client.set("players", players)
    
    return "Ok"

# Main route return the top players
@service.route("/players")
def get_best_players():
    response = "error: o ranking de jogadores não foi inicializado."

    client = base.Client((DATABASE, 11211))
    players = client.get("players")
    
    if players:
        response = players

    return response
if __name__ == '__main__':
    service.run(
        debug= DEBUG,
        host= HOST,
        port=PORT
    )