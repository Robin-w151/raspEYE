#!/usr/bin/env python3

import sys


def sendData(connection, data):

    length = str(len(data))
    data = length.encode() + b'\x00' + data

    connection.sendall(data)

    if 'ACK' != connection.recv(3).decode():
        sys.exit(1)


def sendFile(connection, fileName):

    file = open(fileName, 'rb')

    while True:

        buffer = file.read(8192)
        if not buffer:
            break
        sendData(connection, buffer)

    file.close()

    sendData(connection, b'EOF')


def recvData(connection):

    data = connection.recv(8192)
    index = data.find(b'\x00')
    length = data[:index].decode()

    if not isinstance(length, int):
        return b''

    data = data[index + 1:]

    while len(data) < int(length):
        buffer = connection.recv(8192)
        if not buffer:
            break
        data += buffer

    connection.send('ACK'.encode())

    return data


def recvFile(connection, fileName):

    file = open(fileName, 'wb')

    buffer = b''

    while buffer != b'EOF':

        buffer = recvData(connection)
        file.write(buffer)

    file.close()
