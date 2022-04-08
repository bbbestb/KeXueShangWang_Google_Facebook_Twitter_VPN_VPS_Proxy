# use this socket server to debug an issue.

import socket

address = ('127.0.0.1', 8100)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)

while(True):
    ss, addr = s.accept()
    print 'got connected from', addr

    ss.send('byebye')
    ra = ss.recv(512)
    print ra

    for i in ra.split('\r\n\r\n'):
        print i

    for i in ra.split('\r\n'):
        print i.encode('hex')
        print i

    ss.close()

s.close()
