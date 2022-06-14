# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 65, 83, 255), stop:1 rgba(0, 135, 184, 255))")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background:transparent;\n"
"color:rgb(255, 255, 255)")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255)")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEditUsername = QLineEdit(Form)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setStyleSheet(u"background:transparent;\n"
"border: 1px solid white;\n"
"color: white\n"
"")

        self.horizontalLayout_3.addWidget(self.lineEditUsername)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255)")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditPassword = QLineEdit(Form)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setStyleSheet(u"background:transparent;\n"
"border: 1px solid white;\n"
"color: white\n"
"")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEditPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.label_status)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonLogin = QPushButton(Form)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setMaximumSize(QSize(101, 24))
        self.pushButtonLogin.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonLogin.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.pushButtonLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"PayPort", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEditPassword.setText("")
        self.label_status.setText("")
        self.pushButtonLogin.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi

