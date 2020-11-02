from tkinter import *

master = Tk()
master.title("Choose your pet")
master.geometry("400x300")
master.configure(background="yellow")


def create():
    entry_input = entry.get("1.0", "end")
    print(entry_input)
    # with open('my_weekend_activities.txt', 'w') as f:
    #     print(entry_input)
        # f.write(entry_input)


def display():
    pass


def append():
    pass


def clear():
    entry.delete(0, END)


lbl = Label(master, text="My Weekend Activities").place(x=120, y=30)
entry = Text(master, height=5, width=46) .place(x=10, y=60)

create_btn = Button(master, text="Create Textfile", command=create).place(x=10, y=162)
display_btn = Button(master, text="Display", command=display).place(x=160, y=162)
append_btn = Button(master, text="Append Data", command=append).place(x=270, y=162)

clear_btn = Button(master, text="Clear", width=11, bg="blue", command=clear).place(x=10, y=210)
exit_btn = Button(master, text="Exit", width=11, bg="red", command=master.destroy).place(x=270, y=210)

master.mainloop()