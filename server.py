#!/usr/bin/env python3

import datetime
import os
import raspEYE
import socket
import socketHelper
import threading
import time


class Server:

    def __init__(self, host, port):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(1)

        print('Listening to port ' + str(port))

    def run(self):

        while True:

            c, address = self.s.accept()
            print('Connected to ' + address[0] + ':' + str(address[1]))

            command = socketHelper.recvData(c).decode()
            if command != '':
                print('Command received: ' + command)

            command = command.split(' ')

            if command[0] == 'capture':

                fileName = 'image ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '.png'
                raspEYE.takePicture(fileName, sec=0, res=(1000, 750), bw=(True if 'true' in command else False))
                print('Picture taken')

                print('Start sending picture...')
                socketHelper.sendData(c, fileName.encode())
                socketHelper.sendFile(c, fileName)
                socketHelper.sendData(c, 'Finished'.encode())
                print('Finished sending')

                os.remove(fileName)

            print('Disconnected from ' + address[0] + ':' + str(address[1]))

    def __exit__(self):

        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()


if __name__ == '__main__':

    server = Server('192.168.1.150', 12345)
    server.run()
