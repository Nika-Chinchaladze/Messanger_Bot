from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTextEdit, QLineEdit, QFrame, QMessageBox
from PyQt5 import uic
from Messanger_Class import MessangerBot


class BotApp(QMainWindow):
    def __init__(self):
        super(BotApp, self).__init__()
        uic.loadUi("pyqt5/msgBot.ui", self)
        # define Content:
        self.header = self.findChild(QLabel, "labelHeading")
        self.image = self.findChild(QLabel, "labelPhoto")
        self.msg = self.findChild(QLabel, "labelEnter")
        self.authorize = self.findChild(QLabel, "labelLogin")
        self.vl = self.findChild(QFrame, "line")
        self.confirmButton = self.findChild(QPushButton, "confirmButton")
        self.closeButton = self.findChild(QPushButton, "closeButton")
        self.sendButton = self.findChild(QPushButton, "sendButton")
        self.login = self.findChild(QLineEdit, "lineName")
        self.password = self.findChild(QLineEdit, "linePass")
        self.textMsg = self.findChild(QTextEdit, "textMSG")

        # Actions:
        self.closeButton.clicked.connect(lambda: self.close())
        self.confirmButton.clicked.connect(self.confirm_method)
        self.sendButton.clicked.connect(self.send_sms)

        self.show()

    # =================================== FUNCTIONALITY ============================== #
    def confirm_method(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Information Has Been Saved, Successfully!")
        msg.setWindowTitle("Confirm")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def send_sms(self):
        my_text = self.textMsg.toPlainText()
        my_login = self.login.text()
        my_password = self.password.text()
        my_bot = MessangerBot()
        my_bot.login_messanger(my_log=my_login, my_pass=my_password)
        my_bot.send_messages(my_msg=my_text)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    messanger = BotApp()
    sys.exit(app.exec_())
