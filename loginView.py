import tkinter


class LoginView:

    def __init__(self, main):

        self.main = main

        self.frame = tkinter.Frame(master=self.main.window, width=1000, height=870)
        self.frame.configure(background='light gray')

        self.password = tkinter.Entry(self.frame, show='*', width=16, font=('Arial', 14))
        self.password.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button = tkinter.Button(self.frame, text='Log In', font=('Arial', 14), command=self.login)
        self.button.config(height=2, width=15)
        self.button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def start(self):

        self.frame.pack()

    def login(self):

        self.main.login('')

    def exit(self):

        self.frame.pack_forget()
