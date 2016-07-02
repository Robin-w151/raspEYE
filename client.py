#!/usr/bin/env python3

import cameraView
import loginView
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

    def login(self, password):

        self.mainFrame.exit()
        self.mainFrame = cameraView.CameraView(self, self.address, self.port)
        self.mainFrame.start()

    def exit(self):

        if self.mainFrame is not None:
            self.mainFrame.exit()

        self.window.destroy()

if __name__ == "__main__":

    application = Application('192.168.1.150', 12345)
    application.start()
