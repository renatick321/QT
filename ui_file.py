# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
