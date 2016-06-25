#!/usr/bin/env python3

import socket
import socketHelper
import raspEYE
import time
import datetime
import os


def createServer(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print('Listening to port ' + str(port))

    while True:

        c, address = s.accept()
        print('Connected to ' + address[0] + ':' + str(address[1]))

        command = socketHelper.recvData(c).decode()
        print('Command received: ' + command)

        if command == 'capture':

            fileName = 'image ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '.png'
            raspEYE.takePicture(fileName,sec=0, res=(1000, 750))
            print('Picture taken')

            print('Start sending picture...')
            socketHelper.sendData(c, fileName.encode())
            socketHelper.sendFile(c, fileName)
            socketHelper.sendData(c, 'Finished'.encode())
            print('Finished sending')

            os.remove(fileName)


if __name__ == '__main__':

    createServer('192.168.0.150', 12345)
