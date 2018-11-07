import socket
import threading
import pickle
import sys
from Structure import *
from login import Login as login
from PyQt5.QtWidgets import QApplication, QListWidgetItem,QMessageBox
from PyQt5.QtGui import QFont
from register import Register as register
from chatroom_UI import chat_Ui
from cList_UI import list_Ui


class Client:
    def __init__(self):
        self.addr_port = ('127.0.0.1', 10001)
        # 此客户端开放的端口
        self.aim_addr = ('127.0.0.1', 10086)
        # 目标地址
        self.login_UI = login()
        self.register_UI = register()
        self.list = list_Ui()
        # 将界面作为作为一个类属性
        self.login_UI.login.clicked.connect(self.Login)
        self.register_UI.register.clicked.connect(self.register_UI.buttonclicked)

    def BuiltSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.addr_port)
        return s

    def Chatting(self):
        UDP_socket = self.BuiltSocket()
        threading.Thread(target=self.SendMessage, args=(UDP_socket,)).start()
        threading.Thread(target=self.GetMessage, args=(UDP_socket,)).start()

    def SendMessage(self, UDP_socket):
        while True:
            # 发送数据
            data = input('Send message:')
            data_structure = InfoStructure('xx', 'xuxu', '127.0.0.1:10000', data)
            data_ser = pickle.dumps(data_structure)
            UDP_socket.sendto(data_ser, self.aim_addr)

    def GetMessage(self, UDP_socket):
        while True:
            data_ser = UDP_socket.recv(1024)
            data_structure = pickle.loads(data_ser)
            print('\nReceived Message:', data_structure.data)
            # print(UDP_socket.recv(2048).decode('utf-8'))

    def Register(self):
        """
        用户注册
        :param username: {[str]} -- [用户名的字符串]
        :param password: {[str]} -- [密码的字符串]
        :return: [bool] -- [用户注册成功/失败]
        """
        if not self.userEdit.text():
            # 如果注册用户名为空
            QMessageBox.information(self, '注册失败', '用户名不能为空')
        elif len(self.passEdit.text()) < 6:
            # 如果密码长度小于6
            QMessageBox.information(self, '注册失败', '密码长度过短')
        elif self.passEdit.text() != self.confirmPassEdit.text():
            # 两次密码不一致
            QMessageBox.information(self, '注册失败', '两次输入密码不一致')
        else:
            username = self.login_UI.userEdit.text()
            password = self.login_UI.passEdit.text()
            UDP_socket = self.BuiltSocket()
            data_structure = RegisterStructure(username, password)
            data_ser = pickle.dumps(data_structure)
            UDP_socket.sendto(data_ser, self.aim_addr)
            data_rev = UDP_socket.recv(1024)
            if data_rev == b'Insert success!!!':
                QMessageBox.about(self.register_UI, '注册成功', '欢迎使用本聊天室')
                self.register_UI.close()
                self.login_UI.show()
            else:
                QMessageBox.information(self.register_UI, '注册失败', '该用户名已被占用！')


    def Login(self):
        """
        用户登录
        :param username: {[str]} -- [用户名的字符串]
        :param password: {[str]} -- [密码的字符串]
        :param is_remeber: {[bool]} -- [记住密码的标记变量（暂无）] (default: {False})
        :param auto_login: {[bool]} -- [自动登录的标记变量（暂无）] (default: {False})
        :return: [bool] -- [标记量，表示登陆是否成功]
        """
        username = self.login_UI.userEdit.text()
        password = self.login_UI.passEdit.text()
        is_remeber = self.login_UI.rem_password.isChecked()
        auto_login = self.login_UI.auto_login.isChecked()
        # 四个基本的数据
        # 这里需要你们写出来发登录包
        usernames = []  # 用户名的字符串列表

        '''在这里发出登录包'''

        mark = True     # 登录是否成功的标记
        # 结果的判定逻辑
        if mark:
            # 如果登录成功
            for x in usernames:
                y = QListWidgetItem()
                font = QFont()
                font.setPointSize(16)
                y.setText(x)
                self.list.listWidget.addItem(y)
            self.login_UI.close()
            self.list.show()
        else:
            # 如果失败
            QMessageBox.information(self.login_UI, '登陆失败', '请再次尝试')
            self.login_UI.cleanPassword()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Client()
    # c.Register('123', '456')
    c.login_UI.show()
    sys.exit(app.exec_())
