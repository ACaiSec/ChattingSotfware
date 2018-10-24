import socket
import pickle
import Structure
import threading
import pymysql

class UDP_ForWard():
    def __init__(self):
        self.addr_port = ('127.0.0.1', 10086)

    def BuiltSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.addr_port)
        return s

    def GetInfo(self):
        UDP_socket = self.BuiltSocket()
        while True:
            try:
                data, addr = UDP_socket.recvfrom(2048)
                data_structure = pickle.loads(data)
                print("Connection : ", addr)
                data_structure.userIP = addr
            except:
                continue

            if data_structure.operation_num == 0:
                # Register
                threading.Thread(target=self.Register, args=(UDP_socket, data_structure,)).start()

            elif data_structure.operation_num == 1:
                # Login
                pass

            elif data_structure.operation_num == 2:
                # Chatting
                threading.Thread(target=self.Forward, args=(UDP_socket, data_structure, )).start()
                # self.Forward(UDP_socket, data_structure)

            elif data_structure.operation_num == 3:
                # Exit
                pass

    def Forward(self, UDP_socket, data_structure):
            print('Received from :%s.' % data_structure.username)
            data = pickle.dumps(data_structure)
            # 强行实现双向转发
            if data_structure.userIP == ('127.0.0.1', 10000):
                UDP_socket.sendto(data , ('127.0.0.1', 10001))
            else:
                UDP_socket.sendto(data, ('127.0.0.1', 10000))

    def Register(self, UDP_socket, data_structure):
        db = pymysql.connect('127.0.0.1', 'root', 'root', 'chatting')
        cursor = db.cursor()
        cursor.execute("SELECT * "
                       "FROM  `user` "
                       "WHERE username = '%s' "
                       % (data_structure.username))
        data = cursor.fetchall()

        if len(data) == 0:
            cursor.execute("insert "
                           "into user (username, password) "
                           "values('%s', '%s')"
                           % (data_structure.username, data_structure.password))
            print("Insert success!")
            UDP_socket.sendto(b'Insert success!!!', data_structure.userIP)
            # 发送成功信息
            db.close()
        else:
            print("Insert false!")
            UDP_socket.sendto(b'Insert false!!!', data_structure.userIP)
            db.close()

s = UDP_ForWard()
s.GetInfo()