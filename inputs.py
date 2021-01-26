from tkinter import *

root = Tk()

def addLabel():
    label = Label(root, text=type(e.get()))
    label.pack()   

e = Entry(root, width=20)
e.insert(0, 'Nome')
e.pack()

button = Button(root, text="click", command=addLabel)
button.pack()

root.mainloop()

