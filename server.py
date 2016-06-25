#!/usr/bin/env python3

import socket
import socketHelper
import raspEYE
import time
import datetime


def createServer(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    while True:

        c, address = s.accept()
        print('Connected to ', address)

        command = socketHelper.recvData(c).decode()

        if command == 'capture':

            fileName = 'image ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '.jpg'
            raspEYE.takePicture(fileName)

            socketHelper.sendData(c, fileName.encode())
            socketHelper.sendFile(c, fileName)
            socketHelper.sendData(c, 'Finished'.encode())


if __name__ == '__main__':

    createServer('192.168.0.150', 12345)
