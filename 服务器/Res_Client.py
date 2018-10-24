import socket
import Structure
import pickle

r = Structure.RegisterStructure('chenzehan3', 'siwei')

data = pickle.dumps(r)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 10003))

aim_addr = ('127.0.0.1', 10086)
s.sendto(data, aim_addr)