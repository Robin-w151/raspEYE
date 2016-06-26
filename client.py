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


def deleteImage():

    global currentFileName
    global fileList

    if currentFileName not in fileList:
        fileList.append(currentFileName)
        print('Deleted ' + currentFileName)


def captureImage():

    global info
    global currentFileName
    global fileList
    global imageLabel

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
    imageLabel.config(image=img)
    imageLabel.image = img

    info.set('Finished')
    infoLabel.update_idletasks()

main = tkinter.Tk()
main.title('raspEYE')
main.geometry('1000x870')
main.configure(background='light grey')

info = tkinter.StringVar()
info.set('Ready')

img = tkinter.PhotoImage(file='logo.png')
imageLabel = tkinter.Label(image=img)
imageLabel.place(relx=0.5, rely=0.43, anchor=tkinter.CENTER)
imageLabel.image = img

captureButton = tkinter.Button(main, text='Capture', font=('Arial', 14), command=captureImage)
captureButton.config(height=2, width=15)
captureButton.place(relx=0.5, rely=0.91, anchor=tkinter.CENTER)

saveButton = tkinter.Button(main, text='Save', font=('Arial', 14), command=saveImage)
saveButton.config(height=2, width=15)
saveButton.place(relx=0.3, rely=0.91, anchor=tkinter.CENTER)

deleteButton = tkinter.Button(main, text='Delete', font=('Arial', 14), command=deleteImage)
deleteButton.config(height=2, width=15)
deleteButton.place(relx=0.7, rely=0.91, anchor=tkinter.CENTER)

infoLabel = tkinter.Label(main, textvariable=info, font=('Arial', 14))
infoLabel.place(relx=0.5, rely=0.97, anchor=tkinter.CENTER)

main.wm_protocol('WM_DELETE_WINDOW', onExit)
main.mainloop()
