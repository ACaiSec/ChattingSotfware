import socket
import pickle
import threading
import pymysql
import hashlib
import time
import datetime
import pickle
from Structure import *

class UDP_ForWard():
    global usr_online
    global usr_sum

    def __init__(self):
        self.usr_online = [['xx', ('127.0.0.2', 10150), 'xxasd'],
                           ['gx', ('127.0.0.3', 10199), 'xasfeefdfdf'],
                           ['abcd', ('127.4.5.6', 12346), 'sasasa']]
        self.addr_port = ('127.0.0.1', 10187)
        self.bindcheck_port = ('127.0.0.1', 10193)
        self.attention_port = ('127.0.0.1',10986)

        # threading.Thread(target=self.GetInfo).start()
        threading.Thread(target=self.BindCheck).start()
        # threading.Thread(target = self.BroadcastAttention).start()

    def BuiltSocket(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(port)
        return s

    def GetInfo(self):
        UDP_socket = self.BuiltSocket(self.addr_port)
        print("Begin")
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

            elif data_structure.operation_num == 4:
                # Focus
                print("Focus!")
                threading.Thread(target=self.Focus, args=(UDP_socket, data_structure,)).start()

    def Forward(self, UDP_socket, data_structure):
            print('Received from :%s.' % data_structure.username)
            data = pickle.dumps(data_structure)
            # 强行实现双向转发
            if data_structure.userIP == ('127.0.0.1', 10000):
                UDP_socket.sendto(data , ('127.0.0.1', 10001))
            else:
                UDP_socket.sendto(data, ('127.0.0.1', 10000))

    # 注册
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
            finish = Verify(1, 1)
            UDP_socket.sendto(pickle.dumps(finish), data_structure.userIP)
            # 发送成功信息
            db.close()
        else:
            print("Insert false!")
            unfinish = Verify(1, 0)
            UDP_socket.sendto(pickle.dumps(unfinish), data_structure.userIP)
            db.close()


    # 登录
    def Login(self, UDP_socket, data_structure):
        hash = hashlib.md5('python'.encode('utf-8'))
        # 连接数据库
        db = pymysql.connect('127.0.0.1', 'root', 'root', 'chatting')
        # 获得游标对象
        cursor = db.cursor()
        # 执行数据库语句
        cursor.execute("SELECT * "
                       "FROM  `user` "
                       "WHERE username = '%s' "
                       % (data_structure.username))
        data = cursor.fetchall()

        if data[0] == data_structure.username and data[1] == data_structure.password:
            print("核实有效，确有此人")
            finish = Verify(2, 1)
            UDP_socket.sendto(pickle.dumps(finish), data_structure.userIP)
            db.close()
            # 检测是否重复登录  将原登录客户退出并抹去在线用户列表中
            for each in usr_online:
                if data_structure.username == each[0]:
                    repeat = relogin
                    UDP_socket.sendto(pickle.dumps(repeat), each[1])
                    self.usr_online = filter(lambda x: x != [data_structure.username, each[1], each[2]], self.usr_online)
                    break
            # 添加到用户上线列表bi
            hash.update((data_structure.username + data_structure.userIP[0] + str(data_structure.userIP[1]) + data_structure.password).encode('utf-8'))
            self.usr_online.append([data_structure.username, data_structure.userIP, hash.hexdigest()])
            moreattention = self.GetFriend(data_structure.username)
            attlist = attention(moreattention)
            UDP_socket.sendto(pickle.dumps(attlist), data_structure.IP)
            # 检查是否有离线消息

            # 清空文件内容

            # 发送好友上线列表

            # 收到下线信号

            # 收到消息

            # 收到文件
        else:
            print("查无此人")
            unfinish = Verify(2, 0)
            UDP_socket.sendto(pickle.dumps(unfinish), data_structure.userIP)
            db.close()



    #关注
    def Focus(self, UDP_socket, data_structure):
        db = pymysql.connect('127.0.0.1', 'root', 'root', 'chatting')
        cursor = db.cursor()
        cursor.execute("SELECT username "
                       "FROM  `user` "
                       "WHERE username = '%s' "
                       % (data_structure.target_user))
        data = cursor.fetchall()



        if len(data) > 0:
            cursor2 = db.cursor()
            cursor2.execute("SELECT * "
                            "FROM  `focus` "
                            "WHERE user = '%s' "
                            "AND focus_user = '%s' "
                           % (data_structure.user, data_structure.target_user))
            data2 = cursor.fetchall()
            if len(data2) != 0:
                # 已经关注
                pass
            else:
                cursor3 = db.cursor()
                cursor3.execute("INSERT "
                                "INTO focus "
                                "VALUES ('%s', '%s')"
                                % (data_structure.user, data_structure.target_user))

            return_structure = Verify(4, True)
            data_ser = pickle.dumps(return_structure)
            UDP_socket.sendto(data_ser, data_structure.userIP)
            print("Focus success")






    def BindCheck(self):
        UDP_socket = self.BuiltSocket(self.bindcheck_port)
        UDP_socket.settimeout(10)
        self.SendCheck(UDP_socket)

    # 广播更新检测消息给客户端每个用户，每隔6分钟从新循环进行广播
    def SendCheck(self,UDP_socket):
        heart = loopcheck()
        while True:
            time.sleep(20)

            '''
                若在线列表全空了是否应sleep一定时间后在进行广播
                while Ture:
                    if len(self.usr_online)==0:
                        time.sleep(30)
                    else:
                        break
                貌似不用了，空表情况下不会报错，等待列表不为空的情况下即可
            '''

            for each in self.usr_online:
                print(each)
                UDP_socket.sendto(pickle.dumps(heart), each[1])
            threading.Thread(target=self.ReceiveCheck(UDP_socket)).start()
            time.sleep(360)


    # 有一点需要注意当全体不在线，给谁广播？接收到时好办收不到直接就更新为空
    # 第二时间刚好错过问题


    # 接受哈希，更新在线用户列表
    def ReceiveCheck(self,UDP_socket):
        temp = []
        starttime = datetime.datetime.now()
        print(starttime)
        while True:
            try:
                data, addr = UDP_socket.recvfrom(2048)          # 此行阻塞，接收不到消息陷入等待下面代码块不会执行
                data_structure = pickle.loads(data)
                data_structure.userIP = addr
                if data_structure.operation_num == 3:
                    for each in self.usr_online:
                        if (each[0] == data_structure.username and each[2] == data_structure.hashstring):
                            print(each)
                            temp.append(each)
            except:
                endtime = datetime.datetime.now()
                if((endtime-starttime).seconds >= 60):
                    self.usr_online = temp
                    print(self.usr_online)
                    break





    # 获取好友列表
    def GetFriend(self, user_name):
        onlinefri = []
        db = pymysql.connect('127.0.0.1', 'root', 'root', 'chatting')
        cursor = db.cursor()
        cursor.execute("SELECT username "
                       "FROM  `user` "
                       "WHERE username = '%s' "
                       % (user_name))
        data = cursor.fetchall()

        if len(data) > 0:
            cursor2 = db.cursor()
            cursor2.execute("SELECT * "
                            "FROM  `focus` "
                            "WHERE user = '%s' "
                            % (user_name))
            data2 = cursor.fetchall()
            if len(data2) != 0:
                for each in data:
                    for another in self.usr_online:
                        if (each[1] == another[0]):
                            onlinefri.append(each[1])

        return onlinefri

    # 定时广播发送用户在线关注列表 开多了一个线程和端口
    def BroadcastAttention(self):
        UDP_socket = self.BuiltSocket(self.attention_port)
        while True:
            time.sleep(300)
            for each in self.usr_online:
                moreattention  = self.GetFriend(each[0])
                focusstructure = attention(moreattention)
                UDP_socket.sendto(pickle.dumps(focusstructure), each[1])




s = UDP_ForWard()


