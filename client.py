#!/usr/bin/env python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.150'
port = 12345

s.connect((host, port))
s.send('capture'.encode())

file = open('image.jpg', 'wb')

while True:
    data = s.recv(1024)
    if not data:
        break
    file.write(data)

file.close()
s.close()