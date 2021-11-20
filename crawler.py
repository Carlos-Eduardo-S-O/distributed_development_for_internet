import requests, json 
from time import sleep

# Path for the json files that are used to feed the three services
TOP_PLAYERS           = 'assets/top_playes/best_players.json'
TOP_TEAMS             = 'assets/top_teams/best_teams.json'
TOP_TEAMS_OF_ALL_TIME = 'assets/top_teams_of_all/best_teams_of_all.json'

# Routes to the services that will be feed by this program
PLAYERS_URL      = "http://172.29.1.1:5000/players/write"
TEAMS_URL        = "http://172.29.1.2:5000/teams/write"
TEAMS_OF_ALL_URL = "http://172.29.1.3:5000/best_teams_of_all_time/write"

# Load a json file
def load_JSON(path, key):
    data = None
    
    with open(path, 'r') as file:
        list = json.load(file)
        data = list[key]
        file.close()
    
    return data

def load_rankings():
    players, teams, teams_of_all = load_JSON(TOP_PLAYERS, "players"), load_JSON(TOP_TEAMS, "teams"), load_JSON(TOP_TEAMS_OF_ALL_TIME, "teams")
    
    return players, teams, teams_of_all

def send_data(url, data):
    response = "error: o ranking não existe."
    
    if data: 
        response = requests.post(url, json=json.dumps(data))
        
        if response.ok:
            response = "ranking enviado."
        else:
            response = "erro ao enviar o ranking: " + response.text
    
    return response

if __name__ == "__main__":
    
    try:
        while True:
            players, teams, teams_of_all = load_rankings()
            
            response = send_data(PLAYERS_URL, players)
            print("[BEST PLAYERS RANKING]:",response)
            
            response = send_data(TEAMS_URL, teams)
            print("[BEST TEAMS RANKING]:",response)
            
            response = send_data(TEAMS_OF_ALL_URL, teams_of_all)
            print("[BEST TEAMS OF ALL TIME RANKING]:",response,)
            print()
            
            sleep(10)
    except KeyboardInterrupt:
        print("\nObrigado por utilizar os nossos serviços!!!")
