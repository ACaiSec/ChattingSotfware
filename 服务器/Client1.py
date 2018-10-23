import socket
import threading
from InfoStructure import *

class Client():
    def __init__(self):
        self.addr_port = ('127.0.0.1', 10000)
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
            # 发送数据:
            data = input('Send message:')
            data_structure  = InfoStructure('xuxu', '127.0.0.1:10000', 'xx', '127.0.0.1:10001', data)
            data_ser = pickle.dumps(data_structure)
            UDP_socket.sendto(data_ser, self.aim_addr)

    def GetMessage(self, UDP_socket):
        while True:
            data_ser = UDP_socket.recv(1024)
            data_structure = pickle.loads(data_ser)
            print('\nReceived Message:', data_structure.data)
            #print(UDP_socket.recv(2048).decode('utf-8'))

c = Client()
c.Chatting()
'''
while True:
    # 发送数据:
    data = input('Send message:')
    s.sendto(data, ('127.0.0.1', 10086))
    # 接收数据:
    # print(s.recv(1024).decode('utf-8'))
'''