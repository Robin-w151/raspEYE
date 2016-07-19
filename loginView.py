import tkinter


class LoginView:

    def __init__(self, main):

        self.main = main
        self.font = ('Arial', 14)

        self.frame = tkinter.Frame(master=self.main.window, width=1000, height=870)
        self.frame.configure(background='light gray')

        self.ipLabel = tkinter.Label(self.frame, text='Address', font=self.font, width=7)
        self.ipLabel.configure(background='light gray')
        self.ipLabel.place(relx=0.40, rely=0.45, anchor=tkinter.W)

        self.ipText = tkinter.StringVar()
        self.ipText.set('192.168.0.150')
        self.ipEntry = tkinter.Entry(self.frame, width=12, font=self.font, textvariable=self.ipText)
        self.ipEntry.place(relx=0.55, rely=0.45, anchor=tkinter.CENTER)

        self.portLabel = tkinter.Label(self.frame, text='Port', font=self.font, width=4)
        self.portLabel.configure(background='light gray')
        self.portLabel.place(relx=0.43, rely=0.5, anchor=tkinter.W)

        self.portText = tkinter.StringVar()
        self.portText.set('12345')
        self.portEntry = tkinter.Entry(self.frame, width=12, font=self.font, textvariable=self.portText)
        self.portEntry.place(relx=0.55, rely=0.5, anchor=tkinter.CENTER)

        self.button = tkinter.Button(self.frame, text='Connect', font=self.font, command=self.connect)
        self.button.config(height=2, width=15)
        self.button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.status = tkinter.StringVar()
        self.statusLabel = tkinter.Label(self.frame, textvariable=self.status, font=self.font, width=20)
        self.statusLabel.configure(background='light gray')
        self.statusLabel.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

    def start(self):

        self.frame.pack()

    def connect(self):

        if self.ipEntry.get() != '' and self.portEntry.get() != '':
            self.main.connect(self.ipEntry.get(), int(self.portEntry.get()))

    def exit(self):

        self.frame.pack_forget()
