from tkinter import *
from tkinter.messagebox import showinfo
import sql_connect


def login(user, password):
        result = (sql_connect.sql_reqest(user, password, method="GET"))
        if "Error" in result:
            showinfo(message=result)
            print("YES")
        else:
            showinfo(message=result)
            print("NOT")

def sign_up(user, password):
        result = (sql_connect.sql_reqest(user, password, method="POST"))
        if "Error" in result:
            showinfo(message=result)
            print("YES")
        else:
            showinfo(message=result)
            print("NOT")

class Window(Tk):
    def __init__(self, width=500, height=200):
        super().__init__()

        self.title("My app")
        self.geometry(str(width)+'x'+str(height))

        self.lable1 = Label(self, text="Sing Up or Login")
        self.lable1.grid(row=0, column=1)
    
        self.lable_user = Label(self, text="User Name")
        self.lable_user.grid(row=1, column=0)
    
        self.username = StringVar()
    
        self.entry_user = Entry(self, textvariable=self.username)
        self.entry_user.grid(row=1, column=1)


        self.lable_password = Label(self, text="Password")
        self.lable_password.grid(row=2, column=0)
        
        self.password = StringVar()

        self.entry_password = Entry(self, show='*', textvariable=self.password)
        self.entry_password.grid(row=2, column=1)


        self.login_btn = Button(self, text="Login", command=self.login_fn).grid(row=3, column=1)

        self.sing_btn = Button(self, text="Sign Up", command=self.sign_up_fn).grid(row=0, column=0)

    def login_fn(self):
        user = self.username.get()
        password = self.password.get()
        login(user, password)

    def sign_up_fn(self):
        user = self.username.get()
        password = self.password.get()
        sign_up(user, password)