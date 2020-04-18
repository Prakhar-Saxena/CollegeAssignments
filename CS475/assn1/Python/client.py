from multiprocessing.connection import Client
import socket

from user import getPassword

s = socket.socket()

port = 3141

s.connect((socket.gethostbyname('tux2'), port))

print('server IP: ', socket.gethostbyname('tux2'))

print(s.recv(1024))
s.close()


'''
address = ('localhost', 6000)
conn = Client(address, authkey='predator')
conn.send(getPassword('user_passwords'))
conn.send('close')
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
conn.close()
'''
