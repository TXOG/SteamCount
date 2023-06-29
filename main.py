import os
from plyer import notification
import requests
from dotenv import load_dotenv

load_dotenv()

steam_id = os.getenv("STEAM_ID")
api_key = os.getenv("API_KEY")

exitLoop = False

currentGameName = "None"
game_name = ""

def requestAPIData(game_name):
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        app_list = data['applist']['apps']

        for app in app_list:
            if app['name'] == game_name:

                url = "http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/?appid=" + str(app['appid'])

                response = requests.get(url)

                playerCount = str(response.json()['response']['player_count'])

                notification.notify(title= f"You have launched: {game_name}", message= f"Player Count: {playerCount}", timeout=5)

        return None
    else:
        return None


if __name__ == "__main__":
    while exitLoop == False:
        url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            player_info = data['response']['players'][0]

            if 'gameextrainfo' in player_info:
                game_name = player_info['gameextrainfo']

                if currentGameName != game_name:
                    currentGameName = game_name
                    requestAPIData(game_name)
        else:
            print("Server Problem")