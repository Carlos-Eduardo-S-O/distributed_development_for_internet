import urllib.request as request, json
from time import sleep

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
        is_alive = True
    
    return is_alive

# Get the best playes from the playes service
def get_best_csgo_players():
    data = access_url(PLAYERS_URL)
    
    players = json.loads(data)
    
    return players

# Get the best teams from the teams service
def get_best_csgo_teams():
    data = access_url(TEAMS_URL)
    
    teams = json.loads(data)
    
    return teams

# Get the best teams of all from the best teams of all service
def get_best_csgo_teams_of_all_time():
    data = access_url(TEAMS_OF_ALL_TIME_URL)
    
    teams = json.loads(data)
    
    return teams

# Print the ranking of csgo players
def print_best_csgo_players(players):
    for player in players:
        print(player["ranking"], "- " + player["name"])
        print("    " + player["nickname"], "Rating:", player["rating"], "Mapas:",player["maps"], "\n")

# Print the ranking of csgo teams
def print_best_csgo_teams(teams):
    for team in teams:
        print( team["ranking"], "- " + team["team"], "País: " + team["nacionality"], "\n")

# Print the ranking of csgo teams of all time
def print_best_csgo_teams_of_all_time(teams):
    for team in teams:
        print(team["ranking"], "- " + team["name"], "Rating:", team["rating"], "Maps:", team["maps"], "\n")

def header_for_players():
    footer()
    footer()
    print("---------------------------- MELHORES JOGADORES DO MUNDO -----------------------------")
    footer()
    print("\n")

def header_for_teams():
    footer()
    footer()
    print("--------------------- MELHORES TIMES DO MUNDO DE TODOS OS TEMPOS ---------------------")
    footer()
    print("\n")

def header_for_teams_of_all_time():
    footer()
    footer()
    print("------------------------------ MELHORES TIMES DO MUNDO -------------------------------")
    footer()
    print("\n")

def footer():
    print("--------------------------------------------------------------------------------------")

def print_ranking():
    time = 2
    players_list, teams_list, teams_of_all_time = get_lists()
    
    header_for_players()
    if players_list:
        print_best_csgo_players(players_list)
    else:
        print("Esse serviço não está no ar!")
    print("")
    sleep(time)
    
    header_for_teams()
    if teams_list:
        print_best_csgo_teams(teams_list)
    else:
        print("Esse serviço não está no ar!")
    print("")
    sleep(time)
    
    header_for_teams_of_all_time()
    if teams_of_all_time:
        print_best_csgo_teams_of_all_time(teams_of_all_time)
    else: 
        print("Esse serviço não está no ar!")
    print("")
    sleep(time)
    
def get_lists():
    players_list      = None
    teams_list        = None
    teams_of_all_time = None
    
    if players_is_alive():
        players_list = get_best_csgo_players()
    
    if teams_is_alive():
        teams_list = get_best_csgo_teams()
    
    if teams_of_all_is_alive():
        teams_of_all_time = get_best_csgo_teams_of_all_time()

    return players_list, teams_list, teams_of_all_time

if __name__ == "__main__":
    try:
        while True:
            print_ranking()
            sleep(3)
    except KeyboardInterrupt:
        print("\nObrigado por usar os nossos serviços!!!")
    
    