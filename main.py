import os
import sys
import threading
import time

from plyer import notification
import requests
from dotenv import load_dotenv
from threading import Thread
from ui_window import Ui_MainWindow

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QDialog, QFileDialog
from PySide6.QtCore import Qt, QPoint, QRect
from PySide6 import QtWidgets
from PySide6.QtCore import QByteArray
from PySide6.QtCore import QDir

load_dotenv()

exitLoop = False

currentGameName = ""
game_name = ""

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

    def createENV(self):
        global api_key
        global steam_id
        api_key = self.apiKeyInput.text()
        steam_id = self.steamIDInput.text()

        if len(api_key) > 0 and len(steam_id) > 0:
            with open('.env', 'w+') as envfile:
                envfile.write(f"API_KEY = '{api_key}' \nSTEAM_ID = '{steam_id}'")

                updateWindowThread = threading.Thread(
                    target=lambda: checkForGameChange())  # Use lambda to pass the method as a callable
                updateWindowThread.start()

                self.mainStack.setCurrentWidget(self.main)

        else:
            return

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
                url = "http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/?appid=" + str(
                    app['appid'])

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
                background-size: 100% 100%;
                ''')
                window.currentPlayerNumber.setText(("Current Players: " + playerCount))

        return None
    else:
        return None


def checkForGameChange():
    global currentGameName
    while True:
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
                window.pfpImage.setStyleSheet('''
                    background-image: url('./profilePicture.jpg');
                    background-position: center;
                    background-repeat: no-repeat;
                    background-origin: content;
                    background-clip: border;
                    background-size: 100% 100%;
                    border-radius: 75px;
                ''')

                window.playerName.setText(player_info['personaname'])

                window.currentGameText.setText(("Currently Playing: NONE"))

        time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Steam Count")
    window.show()
    sys.exit(app.exec())