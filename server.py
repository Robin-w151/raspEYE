#!/usr/bin/env python3

import datetime
import netifaces
import os
import raspEYE
import socket
import socketHelper
import threading
import time


class Server(threading.Thread):

    def __init__(self, host, port):

        threading.Thread.__init__(self)

        self.isStopped = False

        self.host = host
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(2)

        print('IP Address: ' + host)
        print('Listening to port ' + str(port))

    def run(self):

        while not self.isStopped:

            c, address = self.s.accept()

            if self.isStopped:
                return

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

    def stop(self):

        self.isStopped = True

    def __exit__(self):

        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()


if __name__ == '__main__':

    ip = netifaces.ifaddresses('eth0')[2][0]['addr']

    server = Server(ip, 12345)
    server.start()

    while True:

        command = input('Enter EXIT to quit: ').lower()

        if command == 'exit':

            server.stop()

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server.host, server.port))

            s.shutdown(socket.SHUT_RDWR)
            s.close()
            break

    server.join()