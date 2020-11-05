from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("file handling challenge")
master.geometry("400x300")
master.configure(background="yellow")


def create():
    with open('my_weekend_activities.txt', 'w') as f:
        f.write('this is sentence one \n')
        f.write('this is sentence two \n')
        f.write('this is sentence three \n')
        f.write('this is sentence four \n')
        f.write('this is sentence five \n')
        f.close()


def display():
    with open('my_weekend_activities.txt', 'r') as f:
        text_display = f.read()
        entry.insert(END, text_display)
        f.close()


def append():
    text_inp = entry.get("1.0", "end-1c")
    with open('my_weekend_activities.txt', 'a') as f:
        f.write(text_inp + "\n")
        entry.delete("1.0", END)
        message_label['text'] = "sentence appended!"
        message_label.after(2000, clear_label)


def clear_label():
    # remove text
    message_label['text'] = ""


def clear():
    entry.delete("1.0", END)


def exit():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        master.destroy()
    else:
        pass


lbl = Label(master, text="My Weekend Activities", font=("arial", 15, "bold"), bg="yellow", pady=5, padx=5).place(x=90, y=20)
entry = Text(master, height=5, width=46)
entry.place(x=10, y=60)

# create, display and append btn
create_btn = Button(master, text="Create Textfile", command=create).place(x=10, y=162)
display_btn = Button(master, text="Display", command=display).place(x=160, y=162)
append_btn = Button(master, text="Append Data", command=append).place(x=270, y=162)

# clear and exit buttons - last row
clear_btn = Button(master, text="Clear", width=11, bg="blue", fg="white", command=clear).place(x=10, y=210)
exit_btn = Button(master, text="Exit", width=11, bg="red", fg="white", command=exit).place(x=270, y=210)

# message label
message_label = Label(master, fg="green", bg="yellow", font=("arial", 15, "bold"))
message_label.place(x=100, y=260)

master.mainloop()
