import urllib.request as request, json, time
import pandas as pd

# Routes to the best csgo players
PLAYERS_URL      = "http://172.29.1.1:5000/players"
PLAYERS_IS_ALIVE = PLAYERS_URL + "/isalive" 

# Routes to the best csgo teams today
TEAMS_URL      = "http://172.29.1.2:5000/teams"
TEAMS_IS_ALIVE = TEAMS_URL + "/isalive"

# Routes to the best csgo teams of all time
TEAMS_OF_ALL_TIME_URL = "http://172.29.1.3:5000/best_teams_of_all_time"
TEAMS_ALL_IS_ALIVE    = TEAMS_OF_ALL_TIME_URL + "/isalive"

# This method provide access to an url
def access_url(url):
    print("acessando a url: ", url)
    
    response = request.urlopen(url)
    data = response.read()
    
    return data.decode("utf-8")

# Signal if the players service is working
def players_is_alive():
    is_alive = False
    
    if access_url(PLAYERS_IS_ALIVE) == "yes":
        is_alive = True
    
    return is_alive

# Signal if the teams service is working
def teams_is_alive():
    is_alive = False
    
    if access_url(TEAMS_IS_ALIVE) == "yes":
        is_alive = True
    
    return is_alive

# Signal if the teams of all service is working
def teams_of_all_is_alive():
    is_alive = False
    
    if access_url(TEAMS_ALL_IS_ALIVE) == "yes":
        is_alive = False
    
    return is_alive

# Get the best playes from the playes service
def get_best_csgo_players():
    data = access_url()
    
    players_list = json.loads(data)
    
    return players_list["players"]

# Get the best teams from the teams service
def get_best_csgo_teams():
    data = access_url()
    
    teams = json.loads(data)
    
    return teams["teams"]

# Get the best teams of all from the best teams of all service
def get_best_csgo_teams_of_all_time():
    data = access_url()
    
    teams_of_all = json.loads(data)
    
    return teams_of_all["teams"]

# Print the ranking of csgo players
def print_best_csgo_players(players):
    for player in players:
        pass

# Print the ranking of csgo teams
def print_best_csgo_teams(teams):
    for team in teams:
        pass

# Print the ranking of csgo teams of all time
def print_best_csgo_teams_of_all_time(teams):
    for team in teams:
        pass

def header_for_players():
    pass

def header_for_teams():
    pass

def header_for_teams_of_all_time():
    pass

def footer ():
    print("*****************************************************************")

if __name__ == "__main__":
    print(access_url(TEAMS_OF_ALL_TIME_URL))