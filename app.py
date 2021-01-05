import sys
from requests import post, get

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QTextBrowser, QMessageBox, QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from db import *
import __main__
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
MAIN_URL = "http://qtweb.pythonanywhere.com/main"

def clearLayout(layout):
    for i in range(layout.count()): 
        layout.itemAt(i).widget().close()
    




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(503, 570)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.main_label = QtWidgets.QLabel(Dialog)
        self.main_label.setGeometry(QtCore.QRect(10, 10, 490, 341))
        self.main_label.setObjectName("main_label")
        self.login = QtWidgets.QLabel(Dialog)
        self.login.setGeometry(QtCore.QRect(10, 20, 91, 41))
        self.login.setObjectName("login")
        self.login_input = QtWidgets.QLineEdit(Dialog)
        self.login_input.setGeometry(QtCore.QRect(150, 20, 321, 40))
        self.login_input.setObjectName("login_input")
        self.location_input = QtWidgets.QLineEdit(Dialog)
        self.location_input.setGeometry(QtCore.QRect(150, 220, 321, 40))
        self.location_input.setObjectName("location_input")
        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(150, 70, 321, 40))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.name_input = QtWidgets.QLineEdit(Dialog)
        self.name_input.setGeometry(QtCore.QRect(150, 120, 321, 40))
        self.name_input.setObjectName("name_input")
        self.location = QtWidgets.QLabel(Dialog)
        self.location.setGeometry(QtCore.QRect(10, 210, 91, 41))
        self.location.setObjectName("location")
        self.age = QtWidgets.QLabel(Dialog)
        self.age.setGeometry(QtCore.QRect(10, 170, 91, 41))
        self.age.setObjectName("age")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(10, 110, 91, 41))
        self.name.setObjectName("name")
        self.password = QtWidgets.QLabel(Dialog)
        self.password.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.password.setObjectName("password")
        self.description = QtWidgets.QLabel(Dialog)
        self.description.setGeometry(QtCore.QRect(10, 260, 131, 41))
        self.description.setObjectName("description")
        self.description_input = QtWidgets.QTextEdit(Dialog)
        self.description_input.setGeometry(QtCore.QRect(150, 270, 321, 131))
        self.description_input.setObjectName("description_input")
        self.age_input = QtWidgets.QSpinBox(Dialog)
        self.age_input.setGeometry(QtCore.QRect(150, 180, 71, 31))
        self.age_input.setObjectName("age_input")
        self.autorizationbtn = QtWidgets.QPushButton(Dialog)
        self.autorizationbtn.setGeometry(QtCore.QRect(30, 520, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.autorizationbtn.setFont(font)
        self.autorizationbtn.setObjectName("autorizationbtn")
        self.regbtn = QtWidgets.QPushButton(Dialog)
        self.regbtn.setGeometry(QtCore.QRect(280, 520, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.regbtn.setFont(font)
        self.regbtn.setObjectName("regbtn")
        self.load_imagebtn = QtWidgets.QPushButton(Dialog)
        self.load_imagebtn.setGeometry(QtCore.QRect(160, 450, 121, 31))
        self.load_imagebtn.setObjectName("load_imagebtn")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(10, 450, 131, 31))
        self.image.setObjectName("image")
        self.image_out = QtWidgets.QLabel(Dialog)
        self.image_out.setGeometry(QtCore.QRect(310, 420, 130, 90))
        self.image_out.setText("")
        self.image_out.setObjectName("image_out")
        self.age_user = QtWidgets.QLabel(Dialog)
        self.age_user.setGeometry(QtCore.QRect(50, 360, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age_user.setFont(font)
        self.age_user.setObjectName("age_user")
        self.image_user = QtWidgets.QLabel(Dialog)
        self.image_user.setGeometry(QtCore.QRect(130, 70, 261, 231))
        self.image_user.setText("")
        self.image_user.setObjectName("image_user")
        self.name_user = QtWidgets.QLabel(Dialog)
        self.name_user.setGeometry(QtCore.QRect(50, 330, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_user.setFont(font)
        self.name_user.setObjectName("name_user")
        self.description_user = QtWidgets.QLabel(Dialog)
        self.description_user.setGeometry(QtCore.QRect(50, 430, 421, 81))
        self.description_user.setObjectName("description_user")
        self.location_user = QtWidgets.QLabel(Dialog)
        self.location_user.setGeometry(QtCore.QRect(50, 390, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.location_user.setFont(font)
        self.location_user.setObjectName("location_user")
        self.your_avatar = QtWidgets.QLabel(Dialog)
        self.your_avatar.setGeometry(QtCore.QRect(150, 10, 161, 141))
        self.your_avatar.setText("")
        self.your_avatar.setObjectName("your_avatar")
        self.your_description_label = QtWidgets.QLabel(Dialog)
        self.your_description_label.setGeometry(QtCore.QRect(20, 390, 121, 31))
        self.your_description_label.setObjectName("your_description_label")
        self.your_image_label = QtWidgets.QLabel(Dialog)
        self.your_image_label.setGeometry(QtCore.QRect(20, 50, 141, 41))
        self.your_image_label.setObjectName("your_image_label")
        self.your_age_label = QtWidgets.QLabel(Dialog)
        self.your_age_label.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.your_age_label.setObjectName("your_age_label")
        self.your_age = QtWidgets.QLabel(Dialog)
        self.your_age.setGeometry(QtCore.QRect(110, 320, 371, 51))
        self.your_age.setObjectName("your_age")
        self.your_pass_label = QtWidgets.QLabel(Dialog)
        self.your_pass_label.setGeometry(QtCore.QRect(20, 250, 81, 21))
        self.your_pass_label.setObjectName("your_pass_label")
        self.your_local_label = QtWidgets.QLabel(Dialog)
        self.your_local_label.setGeometry(QtCore.QRect(20, 290, 81, 21))
        self.your_local_label.setObjectName("your_local_label")
        self.load_new_avata_btn = QtWidgets.QPushButton(Dialog)
        self.load_new_avata_btn.setGeometry(QtCore.QRect(320, 130, 161, 41))
        self.load_new_avata_btn.setObjectName("load_new_avata_btn")
        self.your_description = QtWidgets.QPlainTextEdit(Dialog)
        self.your_description.setEnabled(False)
        self.your_description.setGeometry(QtCore.QRect(140, 400, 171, 91))
        self.your_description.setObjectName("your_description")
        self.your_login_label = QtWidgets.QLabel(Dialog)
        self.your_login_label.setGeometry(QtCore.QRect(20, 190, 81, 41))
        self.your_login_label.setObjectName("your_login_label")
        self.person_acc_btn = QtWidgets.QPushButton(Dialog)
        self.person_acc_btn.setGeometry(QtCore.QRect(310, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.person_acc_btn.setFont(font)
        self.person_acc_btn.setObjectName("person_acc_btn")
        self.login1_label = QtWidgets.QLabel(Dialog)
        self.login1_label.setGeometry(QtCore.QRect(150, 170, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login1_label.setFont(font)
        self.login1_label.setObjectName("login1_label")
        self.login1_input = QtWidgets.QLineEdit(Dialog)
        self.login1_input.setGeometry(QtCore.QRect(150, 200, 171, 20))
        self.login1_input.setObjectName("login1_input")
        self.pass1_input = QtWidgets.QLineEdit(Dialog)
        self.pass1_input.setGeometry(QtCore.QRect(150, 180, 211, 21))
        self.pass1_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass1_input.setObjectName("pass1_input")
        self.pass2_label = QtWidgets.QLabel(Dialog)
        self.pass2_label.setGeometry(QtCore.QRect(150, 220, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass2_label.setFont(font)
        self.pass2_label.setObjectName("pass2_label")
        self.pass1_label = QtWidgets.QLabel(Dialog)
        self.pass1_label.setGeometry(QtCore.QRect(150, 150, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass1_label.setFont(font)
        self.pass1_label.setObjectName("pass1_label")
        self.pass2_input = QtWidgets.QLineEdit(Dialog)
        self.pass2_input.setGeometry(QtCore.QRect(150, 260, 211, 21))
        self.pass2_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2_input.setObjectName("pass2_input")
        self.local1_label = QtWidgets.QLabel(Dialog)
        self.local1_label.setGeometry(QtCore.QRect(150, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.local1_label.setFont(font)
        self.local1_label.setObjectName("local1_label")
        self.local1_input = QtWidgets.QLineEdit(Dialog)
        self.local1_input.setGeometry(QtCore.QRect(150, 200, 171, 31))
        self.local1_input.setObjectName("local1_input")
        self.age1_label = QtWidgets.QLabel(Dialog)
        self.age1_label.setGeometry(QtCore.QRect(150, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age1_label.setFont(font)
        self.age1_label.setObjectName("age1_label")
        self.age1_input = QtWidgets.QSpinBox(Dialog)
        self.age1_input.setGeometry(QtCore.QRect(140, 190, 211, 22))
        self.age1_input.setObjectName("age1_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 300, 141, 21))
        self.label.setObjectName("label")
        self.messages_btn = QtWidgets.QPushButton(Dialog)
        self.messages_btn.setGeometry(QtCore.QRect(0, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messages_btn.setFont(font)
        self.messages_btn.setObjectName("messages_btn")
        self.interlocutors = QtWidgets.QComboBox(Dialog)
        self.interlocutors.setGeometry(QtCore.QRect(180, 60, 151, 21))
        self.interlocutors.setObjectName("interlocutors")
        self.interlocutor_label = QtWidgets.QLabel(Dialog)
        self.interlocutor_label.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.interlocutor_label.setObjectName("interlocutor_label")
        self.message_text = QtWidgets.QTextEdit(Dialog)
        self.message_text.setGeometry(QtCore.QRect(20, 390, 461, 121))
        self.message_text.setObjectName("message_text")
        self.your_pass = QtWidgets.QLineEdit(Dialog)
        self.your_pass.setGeometry(QtCore.QRect(110, 240, 201, 31))
        self.your_pass.setObjectName("your_pass")
        self.your_local = QtWidgets.QLineEdit(Dialog)
        self.your_local.setGeometry(QtCore.QRect(110, 290, 201, 31))
        self.your_local.setObjectName("your_local")
        self.your_login = QtWidgets.QLineEdit(Dialog)
        self.your_login.setGeometry(QtCore.QRect(110, 190, 201, 31))
        self.your_login.setObjectName("your_login")
        self.name_user.raise_()
        self.main_label.raise_()
        self.your_pass.raise_()
        self.image_user.raise_()
        self.description.raise_()
        self.message_text.raise_()
        self.your_description_label.raise_()
        self.location_user.raise_()
        self.your_age_label.raise_()
        self.your_age.raise_()
        self.your_login.raise_()
        self.your_local.raise_()
        self.description_user.raise_()
        self.description_input.raise_()
        self.login.raise_()
        self.login_input.raise_()
        self.location_input.raise_()
        self.password_input.raise_()
        self.name_input.raise_()
        self.location.raise_()
        self.age.raise_()
        self.name.raise_()
        self.password.raise_()
        self.age_input.raise_()
        self.autorizationbtn.raise_()
        self.regbtn.raise_()
        self.load_imagebtn.raise_()
        self.image.raise_()
        self.image_out.raise_()
        self.age_user.raise_()
        self.your_avatar.raise_()
        self.your_image_label.raise_()
        self.your_pass_label.raise_()
        self.your_local_label.raise_()
        self.your_description.raise_()
        self.your_login_label.raise_()
        self.person_acc_btn.raise_()
        self.login1_label.raise_()
        self.login1_input.raise_()
        self.pass1_input.raise_()
        self.pass2_label.raise_()
        self.pass1_label.raise_()
        self.pass2_input.raise_()
        self.local1_label.raise_()
        self.local1_input.raise_()
        self.age1_label.raise_()
        self.age1_input.raise_()
        self.label.raise_()
        self.messages_btn.raise_()
        self.interlocutors.raise_()
        self.interlocutor_label.raise_()
        self.load_new_avata_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.main_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Знакомства</span></p></body></html>"))
        self.login.setText(_translate("Dialog", "Логин:"))
        self.location.setText(_translate("Dialog", "Город:"))
        self.age.setText(_translate("Dialog", "Возраст"))
        self.name.setText(_translate("Dialog", "Имя:"))
        self.password.setText(_translate("Dialog", "Пароль:"))
        self.description.setText(_translate("Dialog", "Расскажите какой вы:"))
        self.autorizationbtn.setText(_translate("Dialog", "Авторизация"))
        self.regbtn.setText(_translate("Dialog", "Регистрация"))
        self.load_imagebtn.setText(_translate("Dialog", "Загрузить"))
        self.image.setText(_translate("Dialog", "Загрузите фотографию:"))
        self.age_user.setText(_translate("Dialog", "Возраст,"))
        self.name_user.setText(_translate("Dialog", "Имя,"))
        self.description_user.setText(_translate("Dialog", "Информация о себе"))
        self.location_user.setText(_translate("Dialog", "Город"))
        self.your_description_label.setText(_translate("Dialog", "Информация о вас:"))
        self.your_image_label.setText(_translate("Dialog", "Ваша фотография:"))
        self.your_age_label.setText(_translate("Dialog", "Ваш возраст:"))
        self.your_age.setText(_translate("Dialog", "Возраст"))
        self.your_pass_label.setText(_translate("Dialog", "Ваш пароль:"))
        self.your_local_label.setText(_translate("Dialog", "Ваш город:"))
        self.load_new_avata_btn.setText(_translate("Dialog", "Загрузить новое фото"))
        self.your_login_label.setText(_translate("Dialog", "Ваше имя:"))
        self.person_acc_btn.setText(_translate("Dialog", "Личный кабинет"))
        self.login1_label.setText(_translate("Dialog", "Введите новый логин:"))
        self.pass2_label.setText(_translate("Dialog", "Введите новый пароль:"))
        self.pass1_label.setText(_translate("Dialog", "Введите старый пароль:"))
        self.local1_label.setText(_translate("Dialog", "Введите новый город:"))
        self.age1_label.setText(_translate("Dialog", "Укажите новый возраст:"))
        self.label.setText(_translate("Dialog", "и как с вами связаться"))
        self.messages_btn.setText(_translate("Dialog", "Сообщения"))
        self.interlocutor_label.setText(_translate("Dialog", "Выберите собеседника:"))















class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.interlocutors.hide()
        self.interlocutor_label.hide()
        self.message_text.hide()

        self.textbox = QTextBrowser(self)
        self.textbox.move(10, 0)
        self.textbox.resize(490, 341)
        self.textbox.setText("")
        self.textbox.setFont(QFont("Times", 32))
        self.textbox.hide()
        self.load_new_avata_btn.clicked.connect(self.new_ava)
        self.person_acc_btn.clicked.connect(self.pers)
        self.autorizationbtn.clicked.connect(self.like)
        self.regbtn.clicked.connect(self.dislike)
        self.load_imagebtn.clicked.connect(self.load_image)
        self.messages_btn.clicked.connect(self.get_messages)
        self.interlocutors.activated.connect(self.update)
        self.username = None
        self.partner_login = None
        self.user_choice = 0

    def new_description(self):
        self.your_description.setReadOnly(False)

    def accept_new_age(self):
        if self.age1_input.value() < 18:
            msg = QMessageBox()
            msg.setWindowTitle('Вы молодой, приходите позже')
            msg.setText('Вы слишком молоды, программа только для совершеннолетних')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec()
        self.age1_label.hide()
        self.age1_input.hide()
        self.personal_account()
        self.regbtn.show()
        self.person_acc_btn.show()
        self.messages_btn.show()
        self.your_age.setText(self.age1_input.value())

    def new_age(self):
        self.hide_all()
        self.age1_label.show()
        self.age1_input.show()


    def accept_new_local(self):
        if len(self.local1_input.text()) < 3:
            msg = QMessageBox()
            msg.setWindowTitle('В пароле меньше 3 символов')
            msg.setText('Введите 3 и более символов в поле для Города')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec()
        self.local1_label.hide()
        self.local1_input.hide()
        self.personal_account()
        self.regbtn.show()
        self.person_acc_btn.show()
        self.your_local.setText(self.local1_input.text())

    def new_local(self):
        self.hide_all()
        self.local1_label.show()
        self.local1_input.show()


    def accept_new_pass(self):
        a = self.pass1_input.text()
        if get_user(self.username)['password'] != a:
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Старый пароль неверен')
            msg.setIcon(QMessageBox.Question)           
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec()
        b = self.pass2_input.text()
        if len(b) < 8:
            msg = QMessageBox()
            msg.setWindowTitle('В пароле меньше 8 символов')
            msg.setText('Введите 8 и более символов в поле для Пароля')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec()
        self.pass1_label.hide()
        self.pass1_input.hide()
        self.pass2_label.hide()
        self.pass2_input.hide()
        self.personal_account() 
        self.regbtn.show()
        self.person_acc_btn.show()
        self.messages_btn.show()
        self.your_pass.setText(self.pass1_input.text())

    def new_pass(self):
        self.hide_all()
        self.pass1_label.show()
        self.pass1_input.show()
        self.pass2_label.show()
        self.pass2_input.show()

    def accept_new_login(self):
        if len(self.login1_input.text()) < 8:
            msg = QMessageBox()
            msg.setWindowTitle('В логине меньше 8 символов')
            msg.setText('Введите 8 и более символов в поле для Логина')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok)
            return msg.exec()
        self.login1_label.hide()
        self.login1_input.hide()
        self.personal_account()
        self.regbtn.show()
        self.person_acc_btn.show()
        self.messages_btn.show()
        self.your_login.setText(self.login1_input.text())

    def new_login(self):
        self.hide_all()
        self.login1_label.show()
        self.login1_input.show()

    def new_ava(self):
        self.filename = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.new_pixmap = QPixmap(self.filename)
        self.your_avatar.setScaledContents(True)
        self.your_avatar.setPixmap(self.new_pixmap)

    def pers(self):
        a = self.person_acc_btn.text()
        if a == 'Личный кабинет':
            self.personal_account()
            self.person_acc_btn.setText('Вернуться')
            self.messages_btn.hide()
            self.regbtn.setText('Сохранить')
            user = get_user(self.username)
            self.your_login.setText(self.username)
            self.your_pass.setText(user["password"])
            self.your_description.setPlainText(user["description"])
            self.your_age.setText(str(user["age"]))
            self.your_avatar.setScaledContents(True)
            self.your_avatar.setPixmap(QPixmap(user['img_path']))
            self.your_local.setText(user["location"])
            # вот это всё уберёшь крч, это я для проверки ставил, вкратце аватарки в личном, бушь брать с бд
        if a == 'Вернуться':
            self.come_back()
            self.partner()

    def hide_all(self):
        self.regbtn.hide()
        self.autorizationbtn.hide()
        self.person_acc_btn.hide()
        self.messages_btn.hide()
        self.your_image_label.hide()
        self.your_avatar.hide()
        self.load_new_avata_btn.hide()
        self.your_login_label.hide()
        self.your_login.hide()
        self.your_pass_label.hide()
        self.your_pass.hide()
        self.your_local_label.hide()
        self.your_local.hide()
        self.your_age_label.hide()
        self.your_age.hide()
        self.your_description_label.hide()
        self.your_description.hide()

    def load_image(self):#здесь картинку грузим
        self.filename = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        if self.filename:
            self.pixmap = QPixmap(self.filename)
            self.image_out.setScaledContents(True)
            self.image_out.setPixmap(self.pixmap)

    def like(self):
        a = self.autorizationbtn.text()
        if a == 'Авторизация':
            self.regbtn.setText("Продолжить")
            self.autorizationbtn.setText('Вернуться')
            self.main_fields()
        elif a == '👍':
            data = {'login1': self.username, 'login2': self.partner_login}
            mark(self.username, self.partner_login, 1)
            self.partner()
        elif a == 'Вернуться':
            self.go_main_window()

    def dislike(self):
        s = self.regbtn.text()
        if s == "Регистрация":
            self.regbtn.setText("Готово")
            self.autorizationbtn.setText('Вернуться')
            self.main_fields()
            self.secondary_fields()
        elif s == 'Готово': # здесь я добавил месседж боксы
            username = self.login_input.text()
            self.username = username
            password = self.password_input.text()
            name = self.name_input.text()
            location = self.location_input.text()
            description = self.description_input.toPlainText()
            age = self.age_input.value()
            if len(username) < 8 and not can_create(username):
                msg = QMessageBox()
                msg.setWindowTitle('В логине меньше 8 символов')
                msg.setText('Введите 8 и более символов в поле для Логина')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if len(password) < 8:
                msg = QMessageBox()
                msg.setWindowTitle('В пароле меньше 8 символов')
                msg.setText('Введите 8 и более символов в поле для Пароля')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if len(name) < 3:
                msg = QMessageBox()
                msg.setWindowTitle('В пароле меньше 3 символов')
                msg.setText('Введите 3 и более символов в поле для Имени')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if len(location) < 3:
                msg = QMessageBox()
                msg.setWindowTitle('В пароле меньше 3 символов')
                msg.setText('Введите 3 и более символов в поле для Города')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if len(description) < 10:
                msg = QMessageBox()
                msg.setWindowTitle('Вы ввели мало информации')
                msg.setText('Напишите в поле о себе больше информации')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if age < 18:
                msg = QMessageBox()
                msg.setWindowTitle('Вы молодой, приходите позже')
                msg.setText('Вы слишком молоды, программа только для совершеннолетних')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            try:
                print(self.pixmap)
            except AttributeError:
                msg = QMessageBox()
                msg.setWindowTitle('Загрузите ваше фото')
                msg.setText('Загрузите ваше фото')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()


            #желательно вот здесь заноси все данные в бд)
            user_create(self.username, password, name, age, location, description, self.filename)
            self.regbtn.setText('👎')
            self.autorizationbtn.setText('👍')
            self.start()
            self.image_user.show()
            self.name_user.show()
            self.age_user.show()
            self.location_user.show()
            self.description_user.show()
            self.messages_btn.show()
            self.person_acc_btn.show()#всё вот это форма, сам всё менять бушь
            # #вот это всё уберёшь крч, это я для проверки ставил, вкратце аватарки юзеров, бушь брать с бд
            self.partner()

        elif s == 'Продолжить':
            username = self.login_input.text()
            password = self.password_input.text()
            if len(username) < 8:
                msg = QMessageBox()
                msg.setWindowTitle('В логине меньше 8 символов')
                msg.setText('Введите 8 и более символов в поле для Логина')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if len(password) < 8:
                msg = QMessageBox()
                msg.setWindowTitle('В пароле меньше 8 символов')
                msg.setText('Введите 8 и более символов в поле для Пароля')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            if login_(username, password) is None:
                msg = QMessageBox()
                msg.setWindowTitle('Такого пользователя не существует')
                msg.setText('Ваш логин или пароль неверны!')
                msg.setIcon(QMessageBox.Question)
                msg.setStandardButtons(QMessageBox.Ok)
                return msg.exec()
            self.username = username
            self.regbtn.setText('👎')
            self.autorizationbtn.setText('👍')
            self.start()
            self.image_user.show()
            self.name_user.show()
            self.age_user.show()
            self.location_user.show()
            self.description_user.show()
            self.person_acc_btn.show()
            self.messages_btn.show()
            self.partner()

        elif s == '👎':
            mark(self.username, self.partner_login, 0)
            self.partner()
        elif s == 'Сохранить':
            password = self.your_pass.text()
            print(self.your_pass.text())
            age = self.your_age.text()
            location = self.your_local.text() 
            description = self.your_description.toPlainText()
            try:
                img_path = self.filename
            except AttributeError:
                img_path = get_user(self.username)['img_path']
            user_update(self.your_login.text(), password, age, location, description, img_path)
        elif s == 'Отправить':
            text = self.message_text.toPlainText()
            from_user_login = self.username
            to_user_login = self.interlocutors.currentText()
            self.message_text.setPlainText('')
            message_create(text, from_user_login, to_user_login)

    def personal_account(self): # функция для личного каба
        self.autorizationbtn.hide()
        self.your_image_label.show()
        self.your_avatar.show()
        self.load_new_avata_btn.show()
        self.your_login_label.show()
        self.your_login.show()
        self.your_pass_label.show()
        self.your_pass.show()
        self.your_local_label.show()
        self.your_local.show()
        self.your_age_label.show()
        self.your_age.show()
        self.your_description_label.show()
        self.your_description.show()
        self.image_user.hide()
        self.name_user.hide()
        self.age_user.hide()
        self.location_user.hide()
        self.description_user.hide()

    def assessment(self):
        self.your_image_label.hide()
        self.your_avatar.hide()
        self.load_new_avata_btn.hide()
        self.your_login_label.hide()
        self.your_login.hide()
        self.your_pass_label.hide()
        self.your_pass.hide()
        self.your_local_label.hide()
        self.your_local.hide()
        self.your_age_label.hide()
        self.your_age.hide()
        self.your_description_label.hide()
        self.your_description.hide()
        self.image_user.show()
        self.name_user.show()
        self.age_user.show()
        self.location_user.show()
        self.description_user.show()

    def start(self):
        self.login.hide()
        self.login_input.hide()

        self.password.hide()
        self.password_input.hide()

        self.name.hide()
        self.name_input.hide()
        
        self.age.hide()
        self.age_input.hide()
        
        self.location.hide()
        self.location_input.hide()

        self.description.hide()
        self.label.hide()
        self.description_input.hide()

        self.image.hide()
        self.load_imagebtn.hide()

        self.image_out.hide()

        self.image_user.hide()
        self.name_user.hide()
        self.age_user.hide()
        self.location_user.hide()
        self.description_user.hide()

        self.person_acc_btn.hide()
        self.messages_btn.hide()
        self.your_image_label.hide()
        self.your_avatar.hide()
        self.load_new_avata_btn.hide()
        self.your_login_label.hide()
        self.your_login.hide()
        self.your_pass_label.hide()
        self.your_pass.hide()
        self.your_local_label.hide()
        self.your_local.hide()
        self.your_age_label.hide()
        self.your_age.hide()
        self.your_description_label.hide()
        self.your_description.hide()
        self.login1_label.hide()
        self.login1_input.hide()
        self.pass1_label.hide()
        self.pass1_input.hide()
        self.pass2_label.hide()
        self.pass2_input.hide()
        self.local1_label.hide()
        self.local1_input.hide()
        self.age1_label.hide()
        self.age1_input.hide()


    def go_main_window(self):
        self.login.hide()
        self.login_input.hide()

        self.password.hide()
        self.password_input.hide()

        self.name.hide()
        self.name_input.hide()

        self.age.hide()
        self.age_input.hide()

        self.location.hide()
        self.location_input.hide()

        self.image.hide()
        self.load_imagebtn.hide()

        self.description.hide()
        self.label.hide()
        self.description_input.hide()

        self.image_out.hide()


        self.autorizationbtn.setText('Авторизация')

        self.regbtn.setText('Регистрация')

        self.main_label.show()

    def main_fields(self):
        self.login.show()
        self.login_input.show()

        self.password.show()
        self.password_input.show()

        self.main_label.hide()

    def secondary_fields(self):
        self.name.show()
        self.name_input.show()
        
        self.age.show()
        self.age_input.show()
        
        self.location.show()
        self.location_input.show()

        self.description.show()
        self.label.show()
        self.description_input.show()

        self.image.show()
        self.load_imagebtn.show()

        self.image_out.show()

    def get_messages(self):
        if self.messages_btn.text() == 'Сообщения':
            try:
                self.widget.deleteLater()
                self.lay.deleteLater()
                self.scroll_area.deleteLater()
                self.v_layout.deleteLater()
                self.widget.update()
                self.lay.update()
                self.scroll_area.update()
                self.v_layout.update()
            except:
                pass
            if self.user_choice:
                choice = self.interlocutors.currentText()
                users = get_interlocutors(self.username)
                del users[users.index(choice)]
                users = [choice] + users
                self.interlocutors.clear()
                self.interlocutors.addItems(users)
            else:
                users = get_interlocutors(self.username)
                self.interlocutors.clear()
                self.interlocutors.addItems(users)
            self.widget = QtWidgets.QWidget()
            self.lay = QVBoxLayout(self.widget)
            print(self.interlocutors.currentText(), 1)
            for message in get_some_messages(self.username, self.interlocutors.currentText()):
                label = QLabel(message)
                label.setContentsMargins(10, 10, 10, 10)
                label.setWordWrap(True) # Автоперенос слов
                self.lay.addWidget(label, stretch=10)

            print(self.lay.children())

            self.scroll_area = QtWidgets.QScrollArea(self) 
            self.scroll_area.setWidget(self.widget)
            self.scroll_area.hide()


            self.v_layout = QtWidgets.QVBoxLayout(self)
            self.v_layout.setContentsMargins(20, 100, 20, 200)
            self.v_layout.addWidget(self.scroll_area)
            self.messages_btn.setText("Вернуться")
            self.age_user.hide()
            self.name_user.hide()
            self.location_user.hide()
            self.description_user.hide()
            self.person_acc_btn.hide()
            self.scroll_area.show()
            self.interlocutors.show()
            self.interlocutor_label.show()
            self.message_text.show()
            self.regbtn.setText("Отправить")
            self.autorizationbtn.hide()
            self.age_user.hide()
            self.name_user.hide()
            self.location_user.hide()
            self.description_user.hide()
            self.person_acc_btn.hide()
            self.scroll_area.show()
            self.image_user.hide()
        elif self.messages_btn.text() == 'Вернуться':
            self.come_back()
            self.partner()

    def abc(self):
        r = post(MAIN_URL + "get_partner", data={'login': self.username})
        self.textbox.setText(f"{person['name']}, {person['age']}, {person['location']}\n{person['description']}")
        self.partner_login = person['login']

    def come_back(self):
        try:
            self.widget.deleteLater()
            self.lay.deleteLater()
            self.scroll_area.deleteLater()
            self.v_layout.deleteLater()
            self.v_layout.deleteLater()
            self.widget.update()
            self.lay.update()
            self.scroll_area.update()
            self.v_layout.update()
        except:
            print(123456)
        self.messages_btn.setText("Сообщения")
        self.person_acc_btn.setText('Личный кабинет')
        self.regbtn.setText('👎')
        self.autorizationbtn.show()
        self.autorizationbtn.setText('👍')
        self.start()
        self.image_user.show()
        self.name_user.show()
        self.age_user.show()
        self.location_user.show()
        self.description_user.show()
        self.person_acc_btn.show()
        self.messages_btn.show()
        self.messages_btn.show()
        self.interlocutors.hide()
        self.interlocutor_label.hide()
        self.message_text.hide()

    def update(self):
        self.user_choice = 1
        self.messages_btn.setText("Сообщения")

        choice = self.interlocutors.currentText()
        users = get_interlocutors(self.username)
        del users[users.index(choice)]
        users = [choice] + users
        self.interlocutors.clear()
        self.interlocutors.addItems(users)
        print(self.interlocutors.currentText(), 1)
        clearLayout(self.lay)
        print(self.lay.stretch(0))
        for message in get_some_messages(self.username, self.interlocutors.currentText()):
            label = QLabel(message)
            label.setContentsMargins(10, 10, 10, 10)
            label.setWordWrap(True) # Автоперенос слов
            self.lay.addWidget(label, stretch=10)



        self.messages_btn.setText("Вернуться")
        self.age_user.hide()
        self.name_user.hide()
        self.location_user.hide()
        self.description_user.hide()
        self.person_acc_btn.hide()
        self.scroll_area.show()
        self.interlocutors.show()
        self.interlocutor_label.show()
        self.message_text.show()
        self.regbtn.setText("Отправить")
        self.autorizationbtn.hide()
        self.age_user.hide()
        self.name_user.hide()
        self.location_user.hide()
        self.description_user.hide()
        self.person_acc_btn.hide()
        self.scroll_area.show()
        self.image_user.hide()

    def partner(self):
        partner = get_partner(self.username)
        if not partner is None:
            self.age_user.setText(str(partner['age']))
            self.name_user.setText(str(partner['name']))
            self.location_user.setText(str(partner['location']))
            self.description_user.setText(str(partner['description']))
            self.image_user.setScaledContents(True)
            self.image_user.setPixmap(QPixmap(partner['img_path']))
            self.partner_login = partner['login']
        else:
            self.description_user.setText("Вы оценили все анкеты!")
            self.autorizationbtn.setText("")
            self.regbtn.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.start()
    sys.exit(app.exec_())
