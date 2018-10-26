import socket
import threading
import pickle
from Structure import *


class Client:
    def __init__(self):
        self.addr_port = ('127.0.0.1', 10001)
        # 此客户端开放的端口
        self.aim_addr = ('127.0.0.1', 10086)
        # 目标地址

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
        data_rev = UDP_socket.recv(1024)
        if data_rev == b'Insert success!!!':
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


if __name__ == '__main__':
    c = Client()
    c.Register('123', '456')
