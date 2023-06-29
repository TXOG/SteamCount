# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowIzhlLC.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.mainStack = QStackedWidget(self.centralwidget)
        self.mainStack.setObjectName(u"mainStack")
        self.mainStack.setGeometry(QRect(-1, -1, 801, 601))
        self.mainStack.setStyleSheet(u"")
        self.setup = QWidget()
        self.setup.setObjectName(u"setup")
        self.title = QLabel(self.setup)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(6, 50, 791, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(48)
        font.setBold(True)
        self.title.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(32)
        font1.setBold(True)
        self.currentGameText.setFont(font1)
        self.currentGameText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.currentGameText.setAlignment(Qt.AlignCenter)
        self.gameImage = QLabel(self.main)
        self.gameImage.setObjectName(u"gameImage")
        self.gameImage.setGeometry(QRect(170, 190, 461, 215))
        self.gameImage.setAlignment(Qt.AlignCenter)
        self.currentPlayerNumber = QLabel(self.main)
        self.currentPlayerNumber.setObjectName(u"currentPlayerNumber")
        self.currentPlayerNumber.setGeometry(QRect(0, 420, 801, 61))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.currentPlayerNumber.setFont(font2)
        self.currentPlayerNumber.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.currentPlayerNumber.setAlignment(Qt.AlignCenter)
        self.pfpImage = QLabel(self.main)
        self.pfpImage.setObjectName(u"pfpImage")
        self.pfpImage.setGeometry(QRect(720, 20, 64, 64))
        self.pfpImage.setAlignment(Qt.AlignCenter)
        self.playerName = QLabel(self.main)
        self.playerName.setObjectName(u"playerName")
        self.playerName.setGeometry(QRect(20, 15, 671, 71))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.playerName.setFont(font3)
        self.playerName.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.playerName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mainStack.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Steam Count", None))
        self.apiKeyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input API_KEY", None))
        self.steamIDInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input STEAM_ID", None))
        self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.background.setText("")
        self.currentGameText.setText(QCoreApplication.translate("MainWindow", u"Currently Playing: NONE", None))
        self.gameImage.setText("")
        self.currentPlayerNumber.setText(QCoreApplication.translate("MainWindow", u"Current Players: NONE", None))
        self.pfpImage.setText("")
        self.playerName.setText("")
    # retranslateUi

