import socket

class UDP_ForWard():
    def __init__(self):
        self.addr_port = ('127.0.0.1', 10086)

    def receive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('127.0.0.1', 10086))

        while True:
            data, addr = s.recvfrom(1024)
            print('Received from %s:%s.' % addr)

            send_to = ('127.0.0.1', 10010)
            s.sendto(data, send_to)
            print('finish send.')

    def BuiltSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.addr_port)
        return s

    def Forward(self):
        UDP_socket = self.BuiltSocket()
        while True:
            data, addr = UDP_socket.recvfrom(1024)
            print('Received from %s:%s.' % addr)

            # 强行实现双向转发
            if addr == ('127.0.0.1', 10000):
                UDP_socket.sendto(data , ('127.0.0.1', 10001))
            else:
                UDP_socket.sendto(data, ('127.0.0.1', 10000))

s = UDP_ForWard()
s.Forward()