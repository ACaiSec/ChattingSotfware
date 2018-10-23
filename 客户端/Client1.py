import socket
import threading

class Client():
    def __init__(self):
        self.addr_port = ('127.0.0.1', 10000)
        # 此客户端开放的端口
        self.aim_addr = ('127.0.0.1', 10086)
        # 目标地址

    def BuiltSocket(self):
        #第一个参数是满足IP地址协议，第一个参数创建的socket完成UDP协议
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.addr_port)
        return s

    #登录
    #主函数中循环判断登录成功
    def Login(self,UDP_socket):
        userName = input('用户名：')
        password = input('密码：')
        #登录信息格式
        UDP_socket.sendto(bytes('##'+ userName + '##' + password, 'utf-8'), self.aim_addr)
        recieve = UDP_socket.recv(1024)
        if recieve == 'Y':
            print('登陆成功！')
            return True
        elif recieve == 'N':
            print('用户名或者密码错误！')
            return False

    def Chatting(self):
        UDP_socket = self.BuiltSocket()
        threading.Thread(target=self.SendMessage, args=(UDP_socket,)).start()
        threading.Thread(target=self.GetMessage, args=(UDP_socket,)).start()

    def SendMessage(self, UDP_socket):
        while True:
            # 发送数据:
            data = input('Send message:')
            # 每一次发送数据都需要写上接收方的IP和port
            UDP_socket.sendto(bytes(data, 'utf-8'), self.aim_addr)

    def GetMessage(self, UDP_socket):
        while True:
            data = UDP_socket.recv(1024)
            print('\nReceived Message:', data.decode('utf-8'))


c = Client()
c.Login
while True:
    if c.Login == 1:
        c.Chatting()
    else:
        c.Login

#c.Chatting()
'''
while True:
    # 发送数据:
    data = input('Send message:')
    s.sendto(data, ('127.0.0.1', 10086))
    # 接收数据:
    # print(s.recv(1024).decode('utf-8'))
'''