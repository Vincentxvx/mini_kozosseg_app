
from tkinter import *

user1window = Toplevel()
rightcisechat = Frame(user1window, width=800, height=750, bg="blue")
rightcisechat.place(relx=1,rely=0.5,anchor=E)

canvas = Canvas(rightcisechat)
scrollbar = Scrollbar(rightcisechat, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(rightcisechat)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    Label(scrollable_frame, text="Sample scrolling label").pack()

rightcisechat.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

user1window.mainloop()