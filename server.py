#!/usr/bin/env python3

import socket
import socketHelper
import fileHelper


def createServer(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    while True:

        c, address = s.accept()
        print('Connected to ', address)

        command = socketHelper.recvData(c).decode()
        print(command)

        data = fileHelper.readFile('cat.jpg', 'rb')
        socketHelper.sendData(c, data)


if __name__ == '__main__':

    createServer('127.0.0.1', 12345)
