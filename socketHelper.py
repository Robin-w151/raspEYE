#!/usr/bin/env python3

import sys


def sendData(connection, data):

    length = str(len(data))
    connection.sendall(length.encode())

    if 'ACK' != connection.recv(128).decode():
        sys.exit(1)

    connection.sendall(data)


def recvData(connection):

    length = int(connection.recv(1024).decode())
    connection.send('ACK'.encode())

    data = b''

    while len(data) < length:
        buffer = connection.recv(1024)
        if not buffer:
            break
        data += buffer

    return data
