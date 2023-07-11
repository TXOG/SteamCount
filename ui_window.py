# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowvMsVFc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 607)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.mainStack = QStackedWidget(self.centralwidget)
        self.mainStack.setObjectName(u"mainStack")
        self.mainStack.setGeometry(QRect(0, 0, 801, 611))
        self.mainStack.setStyleSheet(u"")
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.profilePage.setStyleSheet(u"background-color: rgb(27, 40, 56);")
        self.ProfilePageText = QLabel(self.profilePage)
        self.ProfilePageText.setObjectName(u"ProfilePageText")
        self.ProfilePageText.setGeometry(QRect(0, 20, 801, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(32)
        font.setBold(True)
        self.ProfilePageText.setFont(font)
        self.ProfilePageText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ProfilePageText.setAlignment(Qt.AlignCenter)
        self.ProfilePicture = QLabel(self.profilePage)
        self.ProfilePicture.setObjectName(u"ProfilePicture")
        self.ProfilePicture.setGeometry(QRect(310, 100, 181, 181))
        self.NameOfPlayer = QLabel(self.profilePage)
        self.NameOfPlayer.setObjectName(u"NameOfPlayer")
        self.NameOfPlayer.setGeometry(QRect(0, 310, 801, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.NameOfPlayer.setFont(font1)
        self.NameOfPlayer.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.NameOfPlayer.setAlignment(Qt.AlignCenter)
        self.LevelOfPlayer = QLabel(self.profilePage)
        self.LevelOfPlayer.setObjectName(u"LevelOfPlayer")
        self.LevelOfPlayer.setGeometry(QRect(0, 360, 801, 31))
        self.LevelOfPlayer.setFont(font1)
        self.LevelOfPlayer.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.LevelOfPlayer.setAlignment(Qt.AlignCenter)
        self.BackBtn = QPushButton(self.profilePage)
        self.BackBtn.setObjectName(u"BackBtn")
        self.BackBtn.setGeometry(QRect(10, 10, 101, 31))
        font2 = QFont()
        font2.setBold(True)
        self.BackBtn.setFont(font2)
        self.BackBtn.setLayoutDirection(Qt.LeftToRight)
        self.BackBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #66c0f4;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    padding: 8px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fa3;\n"
"	transform: scale(0.8);\n"
"}")
        self.BackBtn.setFlat(False)
        self.mainStack.addWidget(self.profilePage)
        self.setup = QWidget()
        self.setup.setObjectName(u"setup")
        self.title = QLabel(self.setup)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(6, 50, 791, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(48)
        font3.setBold(True)
        self.title.setFont(font3)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title.setAlignment(Qt.AlignCenter)
        self.apiKeyInput = QLineEdit(self.setup)
        self.apiKeyInput.setObjectName(u"apiKeyInput")
        self.apiKeyInput.setGeometry(QRect(240, 190, 321, 31))
        self.apiKeyInput.setStyleSheet(u"QWidget {\n"
"    background-color: #f2f2f2;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.steamIDInput = QLineEdit(self.setup)
        self.steamIDInput.setObjectName(u"steamIDInput")
        self.steamIDInput.setGeometry(QRect(240, 290, 321, 31))
        self.steamIDInput.setStyleSheet(u"QWidget {\n"
"    background-color: #f2f2f2;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.submitButton = QPushButton(self.setup)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(310, 390, 181, 31))
        self.submitButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #66c0f4;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    padding: 8px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fa3;\n"
"	transform: scale(0.8);\n"
"}")
        self.background = QLabel(self.setup)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(-2, -5, 811, 611))
        self.background.setStyleSheet(u"background-image: url('./bg1.png');\n"
"background-position: center;\n"
"background-origin: content;\n"
"background-clip: border;\n"
"background-size: 100% 100%;\n"
"")
        self.mainStack.addWidget(self.setup)
        self.background.raise_()
        self.title.raise_()
        self.apiKeyInput.raise_()
        self.steamIDInput.raise_()
        self.submitButton.raise_()
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: rgb(27, 40, 56);")
        self.currentGameText = QLabel(self.main)
        self.currentGameText.setObjectName(u"currentGameText")
        self.currentGameText.setGeometry(QRect(0, 110, 801, 61))
        self.currentGameText.setFont(font)
        self.currentGameText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.currentGameText.setAlignment(Qt.AlignCenter)
        self.gameImage = QLabel(self.main)
        self.gameImage.setObjectName(u"gameImage")
        self.gameImage.setGeometry(QRect(170, 190, 461, 215))
        self.gameImage.setAlignment(Qt.AlignCenter)
        self.currentPlayerNumber = QLabel(self.main)
        self.currentPlayerNumber.setObjectName(u"currentPlayerNumber")
        self.currentPlayerNumber.setGeometry(QRect(0, 410, 801, 31))
        self.currentPlayerNumber.setFont(font1)
        self.currentPlayerNumber.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.currentPlayerNumber.setAlignment(Qt.AlignCenter)
        self.playerName = QLabel(self.main)
        self.playerName.setObjectName(u"playerName")
        self.playerName.setGeometry(QRect(20, 15, 671, 71))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.playerName.setFont(font4)
        self.playerName.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.playerName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.logoutButton = QPushButton(self.main)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(690, 550, 101, 41))
        self.logoutButton.setFont(font2)
        self.logoutButton.setLayoutDirection(Qt.LeftToRight)
        self.logoutButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #66c0f4;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    padding: 8px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fa3;\n"
"	transform: scale(0.8);\n"
"}")
        self.logoutButton.setFlat(False)
        self.playerGameTime = QLabel(self.main)
        self.playerGameTime.setObjectName(u"playerGameTime")
        self.playerGameTime.setGeometry(QRect(0, 450, 801, 31))
        self.playerGameTime.setFont(font1)
        self.playerGameTime.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.playerGameTime.setAlignment(Qt.AlignCenter)
        self.pfpImage = QPushButton(self.main)
        self.pfpImage.setObjectName(u"pfpImage")
        self.pfpImage.setGeometry(QRect(710, 10, 81, 81))
        self.pfpImage.setStyleSheet(u"border: 0%;")
        self.mainStack.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ProfilePageText.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.ProfilePicture.setText("")
        self.NameOfPlayer.setText(QCoreApplication.translate("MainWindow", u"[NAMEOFPLAYER]", None))
        self.LevelOfPlayer.setText(QCoreApplication.translate("MainWindow", u"[LEVELOFPLAYER]", None))
        self.BackBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Steam Count", None))
        self.apiKeyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input API_KEY", None))
        self.steamIDInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input STEAM_ID", None))
        self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.background.setText("")
        self.currentGameText.setText(QCoreApplication.translate("MainWindow", u"Currently Playing: NONE", None))
        self.gameImage.setText("")
        self.currentPlayerNumber.setText(QCoreApplication.translate("MainWindow", u"Current Players: NONE", None))
        self.playerName.setText("")
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.playerGameTime.setText(QCoreApplication.translate("MainWindow", u"Total Play Time: NONE", None))
        self.pfpImage.setText("")
    # retranslateUi

