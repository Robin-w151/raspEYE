#!/usr/bin/env python3

import socket
import raspEYE


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'raspberrypi'
port = 12345
s.bind((host, port))

s.listen(1)

while True:
    c, addr = s.accept()
    print('Connected to ', addr)

    command = c.recv(1024).decode()
    if command == 'capture':
        raspEYE.takePicture()
        c.send('Captured image'.encode())