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



users = {
    "Bence": {"username": "Bence", "password": ""},
    "Rasch": {"username": "Rasch", "password": ""},
    "Test": {"username": "Test", "password": ""}
}
bg_color = "#48CFCB"
dark_bg = "#424242"
button_color = "#48CFCB"
text_color = "#F5F5F5"

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

    refresh_button = Button(buttons, text="Refresh", command=refresh_chat1, height=2, bg="#48CFCB")
    refresh_button.place(relx=0.5, rely=0.8, relwidth=0.95, anchor=N)


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

    load_chat1()

    global Chat1
    Chat1 = Entry(rightcisechat, bg="white", width=130)
    Chat1.place(relx=0.5, rely=1, anchor=S)
    priv_msg_button = Button(buttons, text="Private Message", command=lambda: open_private_message("Bence"), height=2, bg="#48CFCB")
    priv_msg_button.place(relx=0.5, rely=0.7, relwidth=0.95, anchor=N)


def load_chat1():
    chat_textbox.delete(1.0, END)
    with open('./messages.txt', 'r', encoding='utf-8') as fajl2:
        for sor in fajl2:
            if "Bence" in sor:
                chat_textbox.insert(END, sor + "\n", 'right')
            else:
                chat_textbox.insert(END, sor + "\n", 'left')
        chat_textbox.yview(END)


def refresh_chat1():
    load_chat1()


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

    refresh_button = Button(buttons, text="Refresh", command=refresh_chat2, height=2, bg="#48CFCB")
    refresh_button.place(relx=0.5, rely=0.8, relwidth=0.95, anchor=N)


    global rightcisechat2
    rightcisechat2 = Frame(user2window, width=800, height=750, bg="blue")
    rightcisechat2.place(relx=1, rely=0.5, anchor=E)

    global chat_textbox2
    chat_textbox2 = Text(rightcisechat2, bg="white", width=100, height=47, wrap="word")
    chat_textbox2.place(relx=0.5, rely=0.5, anchor=CENTER)

    scrollbar = Scrollbar(rightcisechat2, command=chat_textbox2.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
    chat_textbox2.config(yscrollcommand=scrollbar.set)

    chat_textbox2.tag_configure('right', justify='right', lmargin1=200, rmargin=50)
    chat_textbox2.tag_configure('left', justify='left', lmargin1=10, rmargin=200)

    load_chat2()

    global Chat2
    Chat2 = Entry(rightcisechat2, bg="white", width=130)
    Chat2.place(relx=0.5, rely=1, anchor=S)
    priv_msg_button = Button(buttons, text="Private Message", command=lambda: open_private_message("Rasch"), height=2, bg="#48CFCB")
    priv_msg_button.place(relx=0.5, rely=0.7, relwidth=0.95, anchor=N)



def load_chat2():
    chat_textbox2.delete(1.0, END)
    with open('./messages.txt', 'r', encoding='utf-8') as fajl2:
        for sor in fajl2:
            if "Vincent" in sor:
                chat_textbox2.insert(END, sor + "\n", 'right')
            else:
                chat_textbox2.insert(END, sor + "\n", 'left')
        chat_textbox2.yview(END)


def refresh_chat2():
    load_chat2()


def messages2():
    message = "Vincent: " + Chat2.get()
    chat_textbox2.insert(END, message + "\n", 'right')
    chat_textbox2.yview(END)

    with open('./messages.txt', 'a', encoding='utf-8') as fajl:
        fajl.write(message + "\n")






def openuser3():
    user3window = Toplevel()
    user3window.geometry("1000x750")
    user3window.minsize(1000, 750)
    user3window.maxsize(1000, 750)
    user3window.config(bg="#424242")
    user3window.title("User Profile")


    lsideinfo = Frame(user3window, bg="#303030", width=200, height=750)
    lsideinfo.place(relx=0, rely=0.5, anchor=W)

    name3 = Label(lsideinfo, text="Test User", font=("Arial", 20), bg="#303030", fg="#656565")
    name3.place(relx=0.5, rely=0, anchor=N)

    buttons = Frame(lsideinfo, bg="#303030")
    buttons.place(relx=0, rely=0.35, relwidth=1, relheight=0.65)

    info = Button(buttons, text="INFO", command=openinfo, height=2, bg="#48CFCB")
    info.place(relx=0.5, rely=0, relwidth=0.95, anchor=N)
    galeri = Button(buttons, text="GALERIE", command=openinfo, height=2, bg="#48CFCB")
    galeri.place(relx=0.5, rely=0.1, relwidth=0.95, anchor=N)
    ChatSend = Button(buttons, text="ChatSend", command=messages3, height=2, bg="#48CFCB")
    ChatSend.place(relx=0.5, rely=0.9, relwidth=0.95, anchor=N)

    refresh_button3 = Button(buttons, text="Refresh Chat", command=refresh_chat3, height=2, bg="#48CFCB")
    refresh_button3.place(relx=0.5, rely=0.8, relwidth=0.95, anchor=N)

    global rightcisechat3
    rightcisechat3 = Frame(user3window, width=800, height=750, bg="blue")
    rightcisechat3.place(relx=1, rely=0.5, anchor=E)

    global chat_textbox3
    chat_textbox3 = Text(rightcisechat3, bg="white", width=100, height=47, wrap="word")
    chat_textbox3.place(relx=0.5, rely=0.5, anchor=CENTER)

    scrollbar3 = Scrollbar(rightcisechat3, command=chat_textbox3.yview)
    scrollbar3.place(relx=1, rely=0, relheight=1, anchor=NE)
    chat_textbox3.config(yscrollcommand=scrollbar3.set)

    chat_textbox3.tag_configure('right', justify='right', lmargin1=200, rmargin=50)
    chat_textbox3.tag_configure('left', justify='left', lmargin1=10, rmargin=200)

    load_chat3()

    global Chat3
    Chat3 = Entry(rightcisechat3, bg="white", width=130)
    Chat3.place(relx=0.5, rely=1, anchor=S)
    priv_msg_button = Button(buttons, text="Private Message", command=lambda: open_private_message("Test"), height=2, bg="#48CFCB")
    priv_msg_button.place(relx=0.5, rely=0.7, relwidth=0.95, anchor=N)


def load_chat3():
    chat_textbox3.delete(1.0, END)
    with open('./messages.txt', 'r', encoding='utf-8') as fajl2:
        for sor in fajl2:
            if "Test" in sor:
                chat_textbox3.insert(END, sor + "\n", 'right')
            else:
                chat_textbox3.insert(END, sor + "\n", 'left')
        chat_textbox3.yview(END)


def refresh_chat3():
    load_chat3()


def messages3():
    message = "Test: " + Chat3.get()
    chat_textbox3.insert(END, message + "\n", 'right')
    chat_textbox3.yview(END)

    with open('./messages.txt', 'a', encoding='utf-8') as fajl:
        fajl.write(message + "\n")


def open_private_message(sender):
    pm_window = Toplevel()
    pm_window.title(f"Private Messaging - {sender}")
    pm_window.geometry("500x600")
    pm_window.config(bg=dark_bg)

    Label(pm_window, text="Select recipient:", font=Labelfont, bg=dark_bg, fg=text_color).pack(pady=10)

    recipient_var = StringVar(pm_window)
    recipient_options = [user for user in users.keys() if user != sender]
    recipient_var.set(recipient_options[0])

    recipient_menu = OptionMenu(pm_window, recipient_var, *recipient_options)
    recipient_menu.config(bg=button_color)
    recipient_menu.pack(pady=5)

    message_display = Text(pm_window, width=60, height=20, bg="white", wrap="word")
    message_display.pack(pady=10)

    def load_messages():
        message_display.delete(1.0, END)
        recipient = recipient_var.get()

        filenames = sorted([sender, recipient])
        filename = f"{filenames[0]}_{filenames[1]}.txt"

        try:
            with open(filename, 'r') as file:
                for line in file:
                    message_display.insert(END, line)
        except FileNotFoundError:
            message_display.insert(END, "No previous messages.\n")

    recipient_var.trace("w", lambda *args: load_messages())
    load_messages()

    message_entry = Entry(pm_window, width=50)
    message_entry.pack(pady=5)

    def send_message():
        recipient = recipient_var.get()
        message = f"{sender}: {message_entry.get()}\n"
        if message_entry.get().strip():
            message_display.insert(END, message)
            message_display.yview(END)


            filenames = sorted([sender, recipient])
            filename = f"{filenames[0]}_{filenames[1]}.txt"
            with open(filename, 'a') as file:
                file.write(message)

            message_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Message cannot be empty!")

    Button(pm_window, text="Send", command=send_message, bg=button_color).pack(pady=10)


def login():
    username_input = user_entry.get()
    password_input = passwd_entry.get()


    if username_input in users:
        if users[username_input]["password"] == password_input:
            if username_input == "Bence":
                openuser1()
            elif username_input == "Rasch":
                openuser2()
            elif username_input == "Test":
                openuser3()
        else:
            messagebox.showerror("Error", "Invalid password")
    else:
        messagebox.showerror("Error", "Invalid username")




Enter = Button(userpass, text="Login", command=login)
Enter.grid(row=3, column=1)

root.mainloop()
