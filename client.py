#!/usr/bin/env python3

import os
import socket
import socketHelper
import sys
import tkinter


host = '192.168.0.150'
port = 12345

currentFileName = ''
fileList = []

def onExit():

    global fileList

    for file in fileList:
        if os.path.isfile(file):
            os.remove(file)

    main.destroy()


def saveImage():

    global currentFileName
    global fileList

    if currentFileName in fileList:
        fileList.remove(currentFileName)
        print('Saved ' + currentFileName)


def captureImage():

    global info
    global currentFileName
    global fileList

    info.set('Connecting')
    infoLabel.update_idletasks()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    info.set('Sending command')
    infoLabel.update_idletasks()
    socketHelper.sendData(s, 'capture'.encode())

    info.set('Receiving data')
    infoLabel.update_idletasks()
    fileName = socketHelper.recvData(s).decode()
    currentFileName = fileName
    fileList.append(fileName)
    socketHelper.recvFile(s, fileName)

    if 'Finished' != socketHelper.recvData(s).decode():
        sys.exit(-1)

    print('Captured ' + fileName)

    s.shutdown(socket.SHUT_RDWR)
    s.close()

    img = tkinter.PhotoImage(file=fileName)
    imageLabel = tkinter.Label(image=img)
    imageLabel.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    imageLabel.image = img

    info.set('Finished')
    infoLabel.update_idletasks()

main = tkinter.Tk()
main.title('raspEYE')
main.geometry('1000x800')
main.configure(background='light grey')

info = tkinter.StringVar()
info.set('Ready')

captureButton = tkinter.Button(main, text='Capture', font=('Arial', 14), command=captureImage)
captureButton.config(height=2, width=15)
captureButton.place(relx=0.4, rely=0.91, anchor=tkinter.CENTER)

saveButton = tkinter.Button(main, text='Save', font=('Arial', 14), command=saveImage)
saveButton.config(height=2, width=15)
saveButton.place(relx=0.6, rely=0.91, anchor=tkinter.CENTER)

infoLabel = tkinter.Label(main, textvariable=info, font=('Arial', 14))
infoLabel.place(relx=0.5, rely=0.97, anchor=tkinter.CENTER)

main.wm_protocol('WM_DELETE_WINDOW', onExit)
main.mainloop()
