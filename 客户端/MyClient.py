# -*- coding: utf-8 -*-
import socket
import threading
import pickle
from Server.Structure import *


class Client:
    def __init__(self):
        self.addr_port = (self.GetHostIP(), 10001)
        # 客户端IP与开放的端口
        self.aim_addr = ('127.0.0.1', 10086)
        # 目标地址，即服务器IP，为固定IP

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

    def BuiltSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.addr_port)
        return s

    def Chatting(self, username, target_user):
        UDP_socket = self.BuiltSocket()
        threading.Thread(target=self.SendMessage, args=(UDP_socket, username, target_user,)).start()
        threading.Thread(target=self.GetMessage, args=(UDP_socket,)).start()

    def SendMessage(self, UDP_socket, username, target_user):
        while True:
            # 发送数据
            data = input('Send message:')
            data_structure = InfoStructure(username, target_user, '127.0.0.1:10000', data)
            data_ser = pickle.dumps(data_structure)
            UDP_socket.sendto(data_ser, self.aim_addr)

    def GetMessage(self, UDP_socket):
        while True:
            data_ser = UDP_socket.recv(1024)
            data_structure = pickle.loads(data_ser)
            print('\nReceived Message:', data_structure.data)
            # print(UDP_socket.recv(2048).decode('utf-8'))

    def Register(self, username, password):
        """
        用户注册
        :param username: {[str]} -- [用户名的字符串]
        :param password: {[str]} -- [密码的字符串]
        :return: [bool] -- [用户注册成功/失败]
        """
        UDP_socket = self.BuiltSocket()
        data_structure = RegisterStructure(username, password)
        data_ser = pickle.dumps(data_structure)
        UDP_socket.sendto(data_ser, self.aim_addr)
        data_str = UDP_socket.recv(1024)
        data_rev = pickle.loads(data_str)
        if data_rev.verity:
            return True
        else:
            return False


    def Login(self, username, password, is_remeber=False, auto_login=False):
        """
        用户登录
        :param username: {[str]} -- [用户名的字符串]
        :param password: {[str]} -- [密码的字符串]
        :param is_remeber: {[bool]} -- [记住密码的标记变量（暂无）] (default: {False})
        :param auto_login: {[bool]} -- [自动登录的标记变量（暂无）] (default: {False})
        :return: [bool] -- [标记量，表示登陆是否成功]
        """
        UDP_socket = self.BuiltSocket()
        data_structure = LoginStructure(username, password)
        data_ser = pickle.dumps(data_structure)
        UDP_socket.sendto(data_ser, self.aim_addr)
        data_str = UDP_socket.recv(1024)
        data_rev = pickle.loads(data_str)
        if data_rev.verify:
            return True
        else:
            return False

    def Focus(self, username, target_user):
        """
        关注用户
        :param username: {[str]} -- [用户名的字符串]
        :param target_user: {[str]} -- [要关注的用户名的字符串]
        :return: [bool] -- [标记量，表示关注是否成功]
        """
        UDP_socket = self.BuiltSocket()
        data_structure = FocusStructure(username, target_user)
        data_ser = pickle.dumps(data_structure)
        UDP_socket.sendto(data_ser, self.aim_addr)
        data_str = UDP_socket.recv(1024)
        data_rev = pickle.loads(data_str)
        # if data_rev.verify and data_rev.operation_num == 4:
        if data_rev.verify:
            return True
        else:
            return False

    def Heartbeat(self):
        """
        确认在线的心跳包
        :return:
        """


if __name__ == '__main__':
    c = Client()
