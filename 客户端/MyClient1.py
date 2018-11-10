# -*- coding: utf-8 -*-
import pickle
import socket
import sys
import threading
from functools import partial
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMessageBox
from PyQt5.QtCore import QDateTime, Qt

from cList_UI import list_Ui
from login import Login as login
from register import Register as register
from Structure import *


class Client:
    def __init__(self):
        # self.addr_port = (self.GetHostIP(), 10002)
        # 发送、接收登录包
        self.addr_port = ('127.0.0.1', 10002)
        # 客户端接收各种消息的地址
        # self.attention_port = ('127.0.0.1', 10986)
        # 客户端发送聊天消息的端口
        self.sendMessage_port = ('127.0.0.1', 10099)
        # 客户端发送关注功能包的端口
        self.focus_port = ('127.0.0.1', 10088)

        # 服务器接受各种信息的地址
        self.aim_addr = ('127.0.0.1', 10187)
        # 服务器接收心跳回复包的地址
        self.bindcheck_port = ('127.0.0.1', 10112)

        self.login_UI = login()
        self.register_UI = register()
        # 将界面作为作为一个类属性
        self.login_UI.login.clicked.connect(self.Login)
        self.login_UI.register.clicked.connect(self.register_UI.show)
        self.register_UI.register.clicked.connect(self.register_UI.buttonclicked)

    def GetHostIP(self):
        """
        取客户端的本地IP
        :return:[str] -- [客户端IP]
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def BuiltSocket(self, socket_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(socket_port)
        return s

    def Chatting(self, UDP_socket):
        # UDP_socket = self.BuiltSocket(self.addr_port)
        while True:
            threading.Thread(target=self.SendMessage, args=(UDP_socket,) ).start()
            threading.Thread(target=self.Focus, args=(UDP_socket,) ).start()
            threading.Thread(target=self.GetAll, args=(UDP_socket,) ).start()

    def SendMessage(self, target_user, data):
        # target_user的获取方式
        UDP_socket = self.BuiltSocket(self.sendMessage_port)
        data_structure = InfoStructure(self.username, target_user, '127.0.0.1:10000', data)
        data_ser = pickle.dumps(data_structure)
        UDP_socket.sendto(data_ser, self.aim_addr)

    # 关注功能
    def Focus(self):
        """
        关注用户
        :param username: {[str]} -- [用户名的字符串]
        :param target_user: {[str]} -- [要关注的用户名的字符串]
        :return: [bool] -- [标记量，表示关注是否成功]
        """
        UDP_socket = self.BuiltSocket(self.focus_port)
        target_user = input("搜索：")
        data_structure = FocusStructure(self.username, target_user)
        data_ser = pickle.dumps(data_structure)
        # 端口占用？与发聊天消息的
        UDP_socket.sendto(data_ser, self.aim_addr)
        # 收到Verity结构体
        data_str = UDP_socket.recv(1024)
        data_rev = pickle.loads(data_str)
        # if data_rev.verify and data_rev.operation_num == 4:
        if data_rev.verify:
            # target_user加入列表中
            # target_user，直接使用，直接插入列表中；但是IP地址需要从服务器放过来并接收,便于聊天?????
            return True
        else:
            return False

    def GetMessage(self, data_structure):
        print(data_structure.data)
        print('\nReceived Message:', data_structure)

    #收到心跳包并回复
    def GetHeart(self, UDP_socket):
        #收到的心跳包的结构是什么？？根据发来的心跳包进行回复确认??
        data_structure = UpdateStructure(self.username)
        UDP_socket.sendto(data_structure, self.bindcheck_port)

    #得到列表,只收不发，attention端口
    def GetFocus(self, UDP_socket):
        # UDP_socket = self.BuiltSocket(self.attention_port)
        data_ser = UDP_socket.recv(1024)
        data_structure = pickle.loads(data_ser)
        if data_structure.operation_num == 8:
            #关注列表
            return data_structure.attentionlist

    def GetAll(self, UDP_socket):
        data_rec = UDP_socket.recv(1024)
        data_structure = pickle.loads(data_rec)
        operation_num = data_structure.operation_num
        if operation_num == 2:
            threading.Thread(target=self.msgShowInChat, args=(data_structure.username, ))
            # threading.Thread(target=self.GetMessage, args=(data_structure), ).start()
            # self.GetMessage(UDP_socket)
        elif operation_num == 7:
            threading.Thread(target=self.GetHeart, args=(UDP_socket), ).start()

    def Register(self, username, password):
        """
        用户注册
        :param username: {[str]} -- [用户名的字符串]
        :param password: {[str]} -- [密码的字符串]
        :return: [bool] -- [用户注册成功/失败]
        """
        if not self.register_UI.userEdit.text():
            # 如果注册用户名为空
            QMessageBox.information(self.register_UI, '注册失败', '用户名不能为空')
        elif len(self.register_UI.passEdit.text()) < 6:
            # 如果密码长度小于6
            QMessageBox.information(self, '注册失败', '密码长度过短')
        elif self.register_UI.passEdit.text() != self.register_UI.confirmPassEdit.text():
            # 两次密码不一致
            QMessageBox.information(self, '注册失败', '两次输入密码不一致')
        else:
            username = self.register_UI.userEdit.text()
            password = self.register_UI.passEdit.text()
            UDP_socket = self.BuiltSocket()
            data_structure = RegisterStructure(username, password)
            data_ser = pickle.dumps(data_structure)
            UDP_socket.sendto(data_ser, self.aim_addr)
            data_str = UDP_socket.recv(1024)
            data_rev = pickle.loads(data_str)
            if data_rev.verity:
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
        # 下述是发登录包流程
        
        UDP_socket = self.BuiltSocket(self.addr_port)
        # username = input("用户名：")
        # password = input("密码：")
        data_structure = LoginStructure(username, password)
        data_ser = pickle.dumps(data_structure)
        UDP_socket.sendto(data_ser, self.aim_addr)
        while True:
            data_rev = UDP_socket.recv(1024)
            data_rev = pickle.loads(data_rev)
            if data_rev.operation_num == 1:
                if data_rev.vertify == True:
                    #获取关注在线列表
                    self.usernames = self.GetFocus(UDP_socket)
                    # usernames = ['abc', 'bcd', 'cde']
                    if data_rev.verify == True and data_rev.operation_num == 1:
                        self.username = username
                        self.list = list_Ui(self.username)
                        # 这里缺一句界面关联关注功能的函数调用，界面组后续会补上
                        self.list.toolButton_add.clicked.connect(self.addBtnClicked)
                        i = 0
                        for x in self.usernames:
                            self.list.addConcern(x)
                            self.list.listWidget.item(i).chat.pushButton_send.clicked.connect(
                                partial(self.sendBtnClicked, str(x)))
                            i = i + 1
                        self.login_UI.close()
                        self.list.show()
                        #转到监听函数，监听接下来可能收到的信息包、被关注包、心跳包并回复
                        self.Chatting(UDP_socket)
                    else:
                    # 如果失败
                        QMessageBox.information(self.login_UI, '登陆失败', '请再次尝试')
                        self.login_UI.cleanPassword()
                    return True
                else:
                    return False
            elif data_rev.operation_num == 6:
                pass


    def addBtnClicked(self):
        """
        按钮触发关注用户
        :param user:{[str]} --[要关注的用户名的字符串] 
        """
        user = str(self.list.lineEdit.text())
        if self.Focus():
            self.usernames.append(user) # 添加到本地关注列表中
            self.list.addConcern(user)
            self.list.listWidget.item(self.list.listWidget.count()-1).chat.pushButton_send.clicked.connect(lambda: self.sendBtnClicked(user))
        else:
            QMessageBox.warning(self.list, 'Warn', '该用户已存在列表中或该用户不存在', QMessageBox.Ok)
    
    def sendBtnClicked(self, user):
        """
        按键触发发送消息
        :param user:{[str]} --[要发送的用户名的字符串]
        """
        row = self.list.searchuser(user)
        if self.list.listWidget.item(row).chat.textEdit_send.toPlainText() == "" :
            QMessageBox.warning(self.list.listWidget.item(row).chat, "Warn", "发送内容不能为空", QMessageBox.Ok)
            return
        else:
            msg=str(self.list.listWidget.item(row).chat.textEdit_send.toHtml())
            self.SendMessage(user, msg)
            # 这里要调用客户端发送消息的函数
            self.list.listWidget.item(row).chat.textEdit_send.clear()
            self.list.listWidget.item(row).chat.textEdit_send.setFocus()
            time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
            self.list.listWidget.item(row).chat.textBrowser_show.setTextColor(Qt.darkGreen)
            self.list.listWidget.item(row).chat.textBrowser_show.setCurrentFont(QFont('Times New Roman', 9))
            self.list.listWidget.item(row).chat.textBrowser_show.append(self.username + '\t' + time)
            self.list.listWidget.item(row).chat.textBrowser_show.append(msg)
    
    def msgShowInChat (self, username, msg):
        """
        将收到的信息显示到对应的聊天窗口中
        :param username:{[str]} --[信息来源的用户名的字符串]
        :param msg:{[str]} --[收到的消息的字符串]
        """
        ##客户端接收到消息后应调用此函数，但线程中函数貌似不能调用其他函数，暂时不知道怎么解决
        # 加线程ser...
        row = self.list.searchuser(username)
        time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.list.listWidget.item(row).chat.textBrowser_show.setTextColor(Qt.darkBlue)
        self.list.listWidget.item(row).chat.textBrowser_show.setCurrentFont(QFont('Times New Roman', 9))
        self.list.listWidget.item(row).chat.textBrowser_show.append(username + '\t' + time)
        self.list.listWidget.item(row).chat.textBrowser_show.append(msg)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Client()
    # c.Register('123', '456')
    c.login_UI.show()
    sys.exit(app.exec_())
