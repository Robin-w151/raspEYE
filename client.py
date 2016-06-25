#!/usr/bin/env python3

import socket
import socketHelper
import fileHelper


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

s.connect((host, port))


data = input('Enter command: ')
socketHelper.sendData(s, data.encode())

socketHelper.recvFile(s, 'copy.jpg')

print(socketHelper.recvData(s).decode())


s.shutdown(socket.SHUT_RDWR)
s.close()
