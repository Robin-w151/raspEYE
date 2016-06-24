#!/usr/bin/env python3

import socket
import socketHelper
import fileHelper


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

s.connect((host, port))

data = input()
socketHelper.sendData(s, data.encode())

data = socketHelper.recvData(s)
fileHelper.writeFile(data, 'copy.jpg', 'wb')
print('Finished')

s.shutdown(socket.SHUT_RDWR)
s.close()
