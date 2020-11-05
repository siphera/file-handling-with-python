import tkinter as tk


def button_pressed():
    # put text
    label['text'] = "Hello World!"
    # run clear_label after 2000ms (2s)
    root.after(2000, clear_label)

def clear_label():
    # remove text
    label['text'] = ""


root = tk.Tk()

label = tk.Label(root) # empty label for text
label.pack()

button = tk.Button(root, text="Press Button", command=button_pressed)
button.pack()

root.mainloop()