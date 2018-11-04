import socket
import pickle
import threading
# import pymysql
import hashlib
import time
import datetime
import pickle
import Structure

class UDP_ForWard():
    global usr_online
    global usr_sum

    def __init__(self):
        self.usr_online = [['xx', ('127.0.0.2', 11123), 'xxasd'], ['gx', ('127.0.0.3',11125), 'gxnbwd']]
        self.addr_port = ('127.0.0.1', 11149)


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
                threading.Thread(target=self.Login, args=(UDP_socket, data_structure,)).start()

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

    def sendCheck(self,UDP_socket):
         while True:
            time.sleep(20)
            threading.Thread(target=self.receivecheck(UDP_socket)).start()
            for each in self.usr_online:
                print(each)
                UDP_socket.sendto(pickle.dumps("更新检测确认"), each[1])
            time.sleep(360)

    def receivecheck(self,UDP_socket):
        temp = []
        starttime = datetime.datetime.now()
        print(starttime)
        # while True:
        data, addr = UDP_socket.recvfrom(2048)
        data_structure = pickle.loads(data)
        data_structure.userIP = addr
        if data_structure.operation_num == 3:
            for each in self.usr_online:
                if (each[0] == data_structure.username and each[2] == data_structure.hashstring):
                    temp.append(each)
        endtime = datetime.datetime.now()
        if ((endtime - starttime).seconds >= 60):
            self.usr_online = temp
            print(self.usr_online)
            # break

    def BIND(self):
        UDP_socket = self.BuiltSocket()
        self.sendCheck(UDP_socket)


s = UDP_ForWard()
s.BIND()


'''
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
'''
'''
    def Login(self, UDP_socket, data_structure):
        hash = hashlib.md5('python'.encode('utf-8'))
        isonline = 0
        # 连接数据库
        # db = pymysql.connect('127.0.0.1', 'root', 'root', 'chatting')
        # 获得游标对象
        # cursor = db.cursor()
        # 执行数据库语句
        # cursor.execute("SELECT * "
                       "FROM  `user` "
                       "WHERE username = '%s' "
                       % (data_structure.username))
        data = cursor.fetchall()

        if data[0] == data_structure.username and data[1] == data_structure.password:
            print("核实有效，确有此人")
            UDP_socket.sendto(pickle.dumps('登录成功，您已于服务成功建立连接'), data_structure.userIP)
            db.close()
            # 检测是否重复登录  将原登录客户退出并抹去在线用户列表中
            for each in usr_online:
                if data_structure.username == each[0]:
                    UDP_socket.sendto(pickle.dumps("CLOSE"), each[1])
                    self.usr_online = filter(lambda x: x != [data_structure.username, each[1], each[2]], self.usr_online)
                    isonline = 1
                    break
            # 添加到用户上线列表
            hash.update((data_structure.username + data_structure.userIP[0] + str(data_structure.userIP[1]) + data_structure.password).encode('utf-8'))
            self.usr_online.append([data_structure.username, data_structure.userIP, hash.hexdigest()])
            # 检查是否有离线消息

            # 清空文件内容

            # 发送好友上线列表



            # 收到下线信号

            # 收到消息

            # 收到文件
        else:
            print("查无此人")
            UDP_socket.sendto(pickle.dumps("登录失败，密码或用户名错误"), data_structure.userIP)
            db.close()

'''

