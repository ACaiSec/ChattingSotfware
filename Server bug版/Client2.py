import socket
import threading
import pickle
from Structure import *
import time
class Client():
    def __init__(self):
<<<<<<< HEAD
        self.addr_port = ('127.0.0.3', 11125)
        # 此客户端开放的端口
        self.aim_addr = ('127.0.0.1', 11149)
=======
        self.addr_port = ('127.0.0.3', 10150)
        # 此客户端开放的端口
        self.aim_addr = ('127.0.0.1', 10148)
>>>>>>> bug bug bubug
        # 目标地址

    def BuiltSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.addr_port)
        return s

    def Chatting(self):
        UDP_socket = self.BuiltSocket()
        threading.Thread(target=self.GetMessage, args=(UDP_socket,)).start()
<<<<<<< HEAD
        time.sleep(40)
=======
>>>>>>> bug bug bubug
        threading.Thread(target=self.SendMessage, args=(UDP_socket,)).start()


    def SendMessage(self, UDP_socket):
<<<<<<< HEAD
        # while True:
            # 发送数据:
            # data = input('Send message:')

=======
         #  while True:
            # 发送数据:
            # data = input('Send message:')
            #  发送更新检测的相关信息  username password hashstring
>>>>>>> bug bug bubug
            data_structure = UpdateStructure('gx', 'xxcjs', 'xasfeefdfdf')
            data_ser = pickle.dumps(data_structure)
            UDP_socket.sendto(data_ser, self.aim_addr)

    def GetMessage(self, UDP_socket):
        while True:
            data_ser = UDP_socket.recv(1024)
            data_structure = pickle.loads(data_ser)
            print('\nReceived Message:', data_structure)
            #print(UDP_socket.recv(2048).decode('utf-8'))

c = Client()
c.Chatting()