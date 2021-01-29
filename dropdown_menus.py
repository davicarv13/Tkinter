from tkinter import *

root = Tk()

#Drop down Boxes

clicked = StringVar()

options = ["Monday", "Tuesday", "Wednesday", "Thurdsday"]
clicked.set(optios[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

root.mainloop()