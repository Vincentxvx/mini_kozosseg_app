from tkinter import *
from random import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage


# Color palette: #F5F5F5 #48CFCB #229799 #424242

root = Tk()
root.title("Mini közösségi app")
root.config(bg="#48CFCB")
root.minsize(500, 200)
root.maxsize(500, 200)
root.geometry('500x200')
Titlefont = tkFont.Font(family="Times New Roman",  size=18,  weight="bold", underline=1)
Labelfont = tkFont.Font(family="Times New Roman",  size=12,  weight="bold", underline=1)

# Variables

user1 = "Bence"
passw1 = ""
user2 = "Rasch"
passw2 = ""


Vincent = {
    "name": "Vincent",
    "age": 17,
    "gender": "Male"
}
Mate = {
    "name": "Máté",
    "age": 17,
    "gender": "Male"
}
# Variables


Cim = Label(root,  text="Please enter your login information: ",   font=Titlefont,   fg="white",  bg="#48CFCB")
Cim.place(relx=0.5,  rely=0.1,  anchor=N)

userpass = Frame(root,  bg="#48CFCB")
userpass.place(rely=0.3,  relx=0.5,  anchor=N)


UsernameFrame = Frame(userpass,  bg="#48CFCB")
UsernameFrame.grid(column=1,  row=0)

user = Label(UsernameFrame,  text="Username:",  bg="#48CFCB",  font=Labelfont)
user.grid(column=0,  row=2)
user_entry = Entry(UsernameFrame, textvariable=user, width=50)
user_entry.grid(column=1,  row=2)

passwdFrame = Frame(userpass,  bg="#48CFCB")
passwdFrame.grid(column=1,  row=2)

passwd = Label(passwdFrame,  text="password:",  bg="#48CFCB",  font=Labelfont)
passwd.grid(column=0,  row=2)
passwd_entry = Entry(passwdFrame,   textvariable=passwd,  width=50,   show="*")
passwd_entry.grid(column=1,   row=2)


# Functions

def openinfo():
    InfoWin = Toplevel()
    InfoWin.geometry("500x750")
    InfoWin.minsize(500, 750)
    InfoWin.maxsize(500, 750)
    InfoWin.config(bg="#424242")


def openuser1():
    user1window = Toplevel()
    user1window.geometry("1000x750")
    user1window.minsize(1000, 750)
    user1window.maxsize(1000, 750)
    user1window.config(bg="#424242")
    user1window.title("User Profile")  

    # info1
    lsideinfo = Frame(user1window, bg="#303030", width=200, height=750)
    lsideinfo.place(relx=0, rely=0.5, anchor=W)

    name1 = Label(lsideinfo, text="Bence", font=("Arial", 20), bg="#303030", fg="#656565")
    name1.place(relx=0.5, rely=0, anchor=N)

    

    
    buttons = Frame(lsideinfo, bg="#303030")
    buttons.place(relx=0, rely=0.35, relwidth=1, relheight=0.65) 

 
    info = Button(buttons, text="INFO", command=openinfo, height=2, bg="#48CFCB")
    info.place(relx=0.5, rely=0,relwidth=0.95, anchor=N)  
    galeri = Button(buttons, text="GALERIE", command=openinfo, height=2, bg="#48CFCB")
    galeri.place(relx=0.5, rely=0.1,relwidth=0.95, anchor=N)  




def openuser2():
    user2window = Toplevel()
    user2window.geometry("1000x750")
    user2window.minsize(1000,  750)
    user2window.maxsize(1000,   750)
    user2window.config(bg="#424242")
    user2window.title(user2)


def login():
    global user1,   user2,   user_entry,   passw1,   passw2,   passwd_entry

    username_input = user_entry.get()
    password_input = passwd_entry.get()

    if username_input == user1 and password_input == passw1:
        openuser1()
    else:
        if username_input == user2 and password_input == passw2:
            openuser2()
        else:
            print("Login failed")
            messagebox.showerror("Error",   "Invalid username or password")


# Functions

Enter = Button(userpass,  text="Login",  command=login)
Enter.grid(row=3,  column=1)

root.mainloop()