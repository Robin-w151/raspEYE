#!/usr/bin/env python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.150'
port = 12345

s.connect((host, port))
s.send('capture'.encode())
print(s.recv(1024).decode())

image = s.recv(1024)
file = open('image.jpg', 'wb')
file.write(image)

s.close()