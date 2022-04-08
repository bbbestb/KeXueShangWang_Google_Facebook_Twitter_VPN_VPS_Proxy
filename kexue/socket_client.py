'''
Created on 2011-8-14

@author: Jay Ren
'''

import socket


def socket_client():
    HOST = '127.0.0.1'  # The remote host
    PORT = 5007  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(b'Hello, world')
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))

if __name__ == '__main__':
    socket_client()
