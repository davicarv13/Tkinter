from tkinter import *

root = Tk()

def myClick():
    label = Label(root, text="Click result")
    label.pack()

myButton = Button(root, text="Click Me", pady=5, padx=5, command=myClick, fg="#fff", width=20)

myButton.pack()

root.mainloop()