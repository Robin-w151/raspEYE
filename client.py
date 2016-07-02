#!/usr/bin/env python3

import cameraView
import loginView
import socket
import tkinter


class Application:

    def __init__(self, address, port):

        self.address = address
        self.port = port
        self.connection = None

        self.window = tkinter.Tk()
        self.window.title('raspEYE')

        self.mainFrame = None

        self.window.wm_protocol('WM_DELETE_WINDOW', self.exit)

    def start(self):

        self.mainFrame = loginView.LoginView(self)
        self.mainFrame.start()

        self.window.mainloop()

    def connect(self, ip, port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        status = s.connect_ex((ip, port))
        s.settimeout(None)

        if status != 0:
            self.mainFrame.status.set('Could not connect')
            self.mainFrame.statusLabel.update_idletasks()

        else:
            self.mainFrame.exit()
            self.mainFrame = cameraView.CameraView(self, ip, port)
            self.mainFrame.start()

        s.shutdown(socket.SHUT_RDWR)
        s.close()

    def exit(self):

        if self.mainFrame is not None:
            self.mainFrame.exit()

        self.window.destroy()

if __name__ == "__main__":

    application = Application('192.168.1.150', 12345)
    application.start()
