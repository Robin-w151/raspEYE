#!/usr/bin/env python3

import socket
import socketHelper
import tkinter


host = '192.168.0.150'
port = 12345

def captureImage():

    global info

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
    socketHelper.recvFile(s, fileName)
    print(socketHelper.recvData(s).decode())

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
captureButton.place(relx=0.5, rely=0.91, anchor=tkinter.CENTER)

infoLabel = tkinter.Label(main, textvariable=info, font=('Arial', 14))
infoLabel.place(relx=0.5, rely=0.97, anchor=tkinter.CENTER)



main.mainloop()
