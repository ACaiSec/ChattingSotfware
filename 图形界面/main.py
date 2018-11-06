import sys

from PyQt5.QtWidgets import QApplication, QMessageBox
sys.path.append('..\客户端')

from chatroom_UI import example
from Client2 import Client
from login import Login
from register import Register

def islogin():
    signal = client.Login(lo.userEdit.text(),lo.passEdit.text())
    if signal:
        chat_UI.show()
        lo.hide()
    else:
        QMessageBox.information(lo,'登陆失败','请再次尝试')
        lo.passEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = Client()
    lo = Login(client)
    lo.show()
    reg = Register(client)
    chat_UI = example()
    lo.register.clicked.connect(reg.show) 
    lo.login.clicked.connect(islogin)   
    sys.exit(app.exec_())


