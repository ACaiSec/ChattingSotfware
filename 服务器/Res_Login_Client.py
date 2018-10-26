import socket
import Structure
import pickle
def send_res():
    r = Structure.RegisterStructure('chenzehan3', 'siwei')

    data = pickle.dumps(r)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 10003))

    aim_addr = ('127.0.0.1', 10086)
    s.sendto(data, aim_addr)

def send_Login():
    l = Structure.LoginStructure('xuxu', 'pass')
    data1 = pickle.dumps(l)
    l2 = Structure.LoginStructure('xuxu123', 'pass123')
    data2 = pickle.dumps(l2)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 10003))

    aim_addr = ('127.0.0.1', 10086)
    s.sendto(data1, aim_addr)
    result = s.recvfrom(1024)
    print(result)

    s.sendto(data2, aim_addr)
    result = s.recvfrom(1024)
    print(result)

if __name__ == '__main__':
    send_Login()