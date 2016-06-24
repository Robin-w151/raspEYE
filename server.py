#!/usr/bin/env python3

import socket


def createServer(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    while True:
        c, address = s.accept()
        print('Connected to ', address)
        command = c.recv(1024).decode()
        print(command)

        file = open('test.png', 'rb')

        data = b''

        while True:
            buffer = file.read(1024)
            if not buffer:
                break
            data += buffer

        file.close()

        print(str(len(data)))
        c.sendall(str(len(data)).encode())

        if 'OK' != c.recv(1024).decode():
            print('test')
            break

        c.sendall(data)
        print('File sent')

        ack = c.recv(1024).decode()
        print(ack)

        c.close()
        print('Connection closed')


if __name__ == '__main__':

    createServer('127.0.0.1', 12345)
