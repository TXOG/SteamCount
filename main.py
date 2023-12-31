import os
import sys
import threading
import time
from plyer import notification
import requests
from dotenv import load_dotenv
from threading import Thread
from ui_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QDialog, QFileDialog

load_dotenv()

exitLoop = False

currentGameName = ""
game_name = ""
personaName = ""
personLevel = 0

api_key = os.getenv('API_KEY')
steam_id = os.getenv('STEAM_ID')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        if os.path.exists('.env'):

            url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                player_info = data['response']['players'][0]

                response = requests.get(player_info['avatarmedium'])

                if response.status_code == 200:
                    with open("profilePicture.jpg", "wb") as f:
                        f.write(response.content)
                        f.close()

                    response = requests.get(player_info['avatarfull'])

                    with open("profilePictureLarge.jpg","wb") as f:
                        f.write(response.content)
                        f.close()

                else:
                    print("Error getting profile picture")

            else:
                print("Error getting Player Summaries")

            updateWindowThread = threading.Thread(
                target=lambda: checkForGameChange())  # Use lambda to pass the method as a callable
            updateWindowThread.start()
            self.mainStack.setCurrentWidget(self.main)

        else:
            self.mainStack.setCurrentWidget(self.setup)

        self.submitButton.clicked.connect(lambda: self.createENV())
        self.logoutButton.clicked.connect(lambda: self.logoutUser())
        self.pfpImage.clicked.connect(lambda: self.loadProfilePage())

    def loadProfilePage(self):

        global personLevel

        # ##### GETTING THE USERS LEVEL #####
        # url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}'
        
        # response = requests.get(url)
        # data = response.json()


        # if 'response' in data and 'players' in data['response']:
        #     players = data['response']['players']
        #     if players:
        #         player = players[0]  # Assuming only one player is returned
        #         if 'player_level' in player:
        #             personLevel = player['player_level']

        #         else:
        #             print("Error")

        self.mainStack.setCurrentWidget(self.profilePage)

        window.BackBtn.clicked.connect(lambda: self.mainStack.setCurrentWidget(self.main))

        window.ProfilePicture.setStyleSheet('''
            background-image: url('./profilePictureLarge.jpg');
            background-position: center;
            background-repeat: no-repeat;
            background-origin: content;
            background-clip: border;
        ''')

        window.NameOfPlayer.setText(f"Username: {personaName}")

        window.LevelOfPlayer.setText(f"Profile Level: {personLevel}")


    def createENV(self):
        global api_key
        global steam_id
        api_key = self.apiKeyInput.text().strip()
        steam_id = self.steamIDInput.text().strip()

        if len(api_key) > 0 and len(steam_id) > 0:
            with open('.env', 'w+') as envfile:
                envfile.write(f"API_KEY = '{api_key}' \nSTEAM_ID = '{steam_id}'")

                url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    player_info = data['response']['players'][0]

                    response = requests.get(player_info['avatarmedium'])

                    if response.status_code == 200:
                        with open("profilePicture.jpg", "wb") as f:
                            f.write(response.content)
                            f.close()

                    else:
                        print("Error getting profile picture")

                else:
                    print("Error getting Player Summaries")

                updateWindowThread = threading.Thread(
                    target=lambda: checkForGameChange())  # Use lambda to pass the method as a callable
                updateWindowThread.start()

                self.mainStack.setCurrentWidget(self.main)

        else:
            return

    def logoutUser(self):
        os.remove(".env")
        self.mainStack.setCurrentWidget(self.setup)

    def closeEvent(self, event):
        event.accept()

def requestAPIData(game_name):
    url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        app_list = data['applist']['apps']

        for app in app_list:
            if app['name'] == game_name:

                ###### GETTING GAME PLAYER COUNT AND GAME IMAGE ########

                url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/?appid={app['appid']}"

                response = requests.get(url)

                playerCount = str(response.json()['response']['player_count'])

                notification.notify(title=f"You have launched: {game_name}", message=f"Player Count: {playerCount}",
                                    timeout=5)

                img = requests.get(f"https://steamcdn-a.akamaihd.net/steam/apps/{app['appid']}/header.jpg")

                if img.status_code == 200:
                    with open("game_header.jpg", "wb") as f:
                        f.write(img.content)
                        f.close()

                else:
                    print("Error getting image")


                ###### GETTING USERS GAME TIME ######

                url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&format=json'
                
                response = requests.get(url)
                data = response.json()
                
                if 'response' in data and 'games' in data['response']:
                    games = data['response']['games']
                    for game in games:
                        if game['appid'] == app['appid']:
                            currentMinutesPlayed = game['playtime_forever']
                            break

                        else:
                            currentMinutesPlayed = 0


                window.pfpImage.setStyleSheet('''
                    background-image: url('./profilePicture.jpg');
                    background-position: center;
                    background-repeat: no-repeat;
                    background-origin: content;
                    background-clip: border;
                    border: 0%;
                ''')

                window.playerName.setText(personaName)

                window.currentGameText.setText(("Currently Playing: " + game_name))
                window.currentGameText.setStyleSheet('''
                color: '#42C236'
                ''')


                window.gameImage.setStyleSheet('''
                background-image: url('./game_header.jpg');
                background-position: center;
                background-repeat: no-repeat;
                background-origin: content;
                background-clip: border;
                ''')

                window.currentPlayerNumber.setText((f"Current Players: {playerCount}"))
                window.playerGameTime.setText((f"Total Play Time: {round(currentMinutesPlayed / 60, 2)} Hours"))

        return None
    else:
        return None

def checkForGameChange():
    global currentGameName
    global personaName

    while True:
        url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            player_info = data['response']['players'][0]

            personaName = player_info['personaname']

            if 'gameextrainfo' in player_info:
                game_name = player_info['gameextrainfo']

                if currentGameName != game_name:
                    currentGameName = game_name
                    requestAPIData(game_name)

            else:
                window.pfpImage.setStyleSheet('''
                    background-image: url('./profilePicture.jpg');
                    background-position: center;
                    background-repeat: no-repeat;
                    background-origin: content;
                    background-clip: border;
                    border: 0%;
                ''')

                window.playerName.setText(personaName)

                window.currentGameText.setText(("Currently Playing: NONE"))
                window.currentGameText.setStyleSheet('''
                color: '#FFFFFF'
                ''')
                window.gameImage.setStyleSheet('''
                                background-image: url('./placeholder.jpg');
                                ''')
                window.currentPlayerNumber.setText(("Current Players: NONE"))
                window.playerGameTime.setText(("Total Play Time: NONE"))

        time.sleep(0.1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Steam Count")
    window.show()
    sys.exit(app.exec())