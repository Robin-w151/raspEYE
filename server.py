#!/usr/bin/env python3

import socket
import raspEYE


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.150'
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
        file = open('image.jpg', 'rb')
        image = file.read(1024)
        while image:
            c.send(image)
            image = file.read(1024)

        file.close()

    c.close()