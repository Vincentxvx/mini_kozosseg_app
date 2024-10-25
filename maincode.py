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
Titlefont = tkFont.Font(family="Times New Roman", size=18, weight="bold", underline=1)
Labelfont = tkFont.Font(family="Times New Roman", size=12, weight="bold", underline=1)

# Variables

user1 = ""
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

# UI Elements
Cim = Label(root, text="Please enter your login information: ", font=Titlefont, fg="white", bg="#48CFCB")
Cim.place(relx=0.5, rely=0.1, anchor=N)

userpass = Frame(root, bg="#48CFCB")
userpass.place(rely=0.3, relx=0.5, anchor=N)

UsernameFrame = Frame(userpass, bg="#48CFCB")
UsernameFrame.grid(column=1, row=0)

user = Label(UsernameFrame, text="Username:", bg="#48CFCB", font=Labelfont)
user.grid(column=0, row=2)
user_entry = Entry(UsernameFrame, width=50)
user_entry.grid(column=1, row=2)

passwdFrame = Frame(userpass, bg="#48CFCB")
passwdFrame.grid(column=1, row=2)

passwd = Label(passwdFrame, text="Password:", bg="#48CFCB", font=Labelfont)
passwd.grid(column=0, row=2)
passwd_entry = Entry(passwdFrame, width=50, show="*")
passwd_entry.grid(column=1, row=2)

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
    info.place(relx=0.5, rely=0, relwidth=0.95, anchor=N)  
    galeri = Button(buttons, text="GALERIE", command=openinfo, height=2, bg="#48CFCB")
    galeri.place(relx=0.5, rely=0.1, relwidth=0.95, anchor=N) 
    ChatSend = Button(buttons, text="ChatSend", command=messages1, height=2, bg="#48CFCB")
    ChatSend.place(relx=0.5, rely=0.9, relwidth=0.95, anchor=N)  
    
    # Scrollbar
    global rightcisechat
    rightcisechat = Frame(user1window, width=800, height=750, bg="blue")
    rightcisechat.place(relx=1, rely=0.5, anchor=E)

    global chat_textbox
    chat_textbox = Text(rightcisechat, bg="white", width=100, height=47, wrap="word")
    
    chat_textbox.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    scrollbar = Scrollbar(rightcisechat, command=chat_textbox.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    chat_textbox.config(yscrollcommand=scrollbar.set)


    chat_textbox.tag_configure('right', justify='right', lmargin1=200, rmargin=50) 
    chat_textbox.tag_configure('left', justify='left', lmargin1=10, rmargin=200)   

# korábbi
    with open('./messages.txt', 'r', encoding='utf-8') as fajl2:
        for sor in fajl2:
            if "Bence" in sor:
                chat_textbox.insert(END, sor + "\n", 'right')
            else:
                chat_textbox.insert(END, sor + "\n", 'left')
        chat_textbox.yview(END)

    global Chat1
    Chat1 = Entry(rightcisechat, bg="white", width=130)
    Chat1.place(relx=0.5, rely=1, anchor=S)

def messages1():
    message = "Bence: " + Chat1.get()
    chat_textbox.insert(END, message + "\n", 'right')
    chat_textbox.yview(END)
    
    with open('./messages.txt', 'a', encoding='utf-8') as fajl:
        fajl.write(message + "\n")


def openuser2():
    user2window = Toplevel()
    user2window.geometry("1000x750")
    user2window.minsize(1000, 750)
    user2window.maxsize(1000, 750)
    user2window.config(bg="#424242")
    user2window.title("User Profile")  

    # info1
    lsideinfo = Frame(user2window, bg="#303030", width=200, height=750)
    lsideinfo.place(relx=0, rely=0.5, anchor=W)

    name1 = Label(lsideinfo, text="Vincent", font=("Arial", 20), bg="#303030", fg="#656565")
    name1.place(relx=0.5, rely=0, anchor=N)
    
    buttons = Frame(lsideinfo, bg="#303030")
    buttons.place(relx=0, rely=0.35, relwidth=1, relheight=0.65) 
 
    info = Button(buttons, text="INFO", command=openinfo, height=2, bg="#48CFCB")
    info.place(relx=0.5, rely=0, relwidth=0.95, anchor=N)  
    galeri = Button(buttons, text="GALERIE", command=openinfo, height=2, bg="#48CFCB")
    galeri.place(relx=0.5, rely=0.1, relwidth=0.95, anchor=N) 
    ChatSend = Button(buttons, text="ChatSend", command=messages2, height=2, bg="#48CFCB")
    ChatSend.place(relx=0.5, rely=0.9, relwidth=0.95, anchor=N)  
    
    
    global rightcisechat2
    rightcisechat2 = Frame(user2window, width=800, height=750, bg="blue")
    rightcisechat2.place(relx=1, rely=0.5, anchor=E)

    global chat_textbox2
    chat_textbox2 = Text(rightcisechat2, bg="white", width=100, height=47, wrap="word") #szavanként töri
    chat_textbox2.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    scrollbar = Scrollbar(rightcisechat2, command=chat_textbox2.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    chat_textbox2.config(yscrollcommand=scrollbar.set)

    
    chat_textbox2.tag_configure('right', justify='right', lmargin1=200, rmargin=50)  
    chat_textbox2.tag_configure('left', justify='left', lmargin1=10, rmargin=200)   

    
    with open('./messages.txt', 'r', encoding='utf-8') as fajl2:
        for sor in fajl2:
            if "Vincent" in sor:
                chat_textbox2.insert(END, sor + "\n", 'right')
            else:
                chat_textbox2.insert(END, sor + "\n", 'left')
        chat_textbox2.yview(END)

    global Chat2
    Chat2 = Entry(rightcisechat2, bg="white", width=130)
    Chat2.place(relx=0.5, rely=1, anchor=S)

def messages2():
    message = "Vincent: " + Chat2.get()
    chat_textbox2.insert(END, message + "\n", 'right')
    chat_textbox2.yview(END)
    
    with open('./messages.txt', 'a', encoding='utf-8') as fajl:
        fajl.write(message + "\n")


def login():
    global user1, user2, user_entry, passw1, passw2, passwd_entry

    username_input = user_entry.get()
    password_input = passwd_entry.get()

    if username_input == user1 and password_input == passw1:
        openuser1()
    elif username_input == user2 and password_input == passw2:
        openuser2()
    else:
        print("Login failed")
        messagebox.showerror("Error", "Invalid username or password")

# Functions
Enter = Button(userpass, text="Login", command=login)
Enter.grid(row=3, column=1)

root.mainloop()