'''
Created on 2011-8-14

@author: Jay Ren
'''

import socket


def socket_server():
    HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
    PORT = 5007  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
    conn.close()

if __name__ == '__main__':
    socket_server()
