#!/usr/bin/env python3

import socket
import socketHelper
import tkinter

host = '192.168.0.150'
port = 12345

def captureImage():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    socketHelper.sendData(s, 'capture'.encode())

    fileName = socketHelper.recvData(s).decode()
    socketHelper.recvFile(s, fileName)
    print(socketHelper.recvData(s).decode())

    s.shutdown(socket.SHUT_RDWR)
    s.close()


main = tkinter.Tk()
main.title('raspEYE')
main.geometry('300x300')
main.configure(background='grey')

captureButton = tkinter.Button(main, text='Capture', command=captureImage)
captureButton.pack()

main.mainloop()
