#!/usr/bin/env python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

s.connect((host, port))


data = input()
s.send(data.encode())
file = open('copy.png', 'wb')
print('File opened')

length = int(s.recv(1024).decode())
print(length)
s.send('OK'.encode())

data = b''

while len(data) < length:
    buffer = s.recv(1024)
    if not buffer:
        break
    data += buffer

file.write(data)

file.close()
print('File closed')

msg = 'File received'
s.send(msg.encode())

s.shutdown(socket.SHUT_RDWR)
s.close()
