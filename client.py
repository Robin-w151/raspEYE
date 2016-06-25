#!/usr/bin/env python3

import socket
import socketHelper
import fileHelper


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.150'
port = 12345

s.connect((host, port))


command = input('Enter command: ')
socketHelper.sendData(s, command.encode())

if command == "capture":

    fileName = socketHelper.recvData(s).decode()
    socketHelper.recvFile(s, fileName)
    print(socketHelper.recvData(s).decode())


s.shutdown(socket.SHUT_RDWR)
s.close()
