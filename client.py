#!/usr/bin/env python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'raspberrypi'
port = 12345

s.connect((host, port))
s.send('capture'.encode())
print(s.recv(1024).decode())
s.close()