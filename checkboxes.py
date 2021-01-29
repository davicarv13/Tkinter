from tkinter import *

root = Tk()

var = StringVar()
var2 = StringVar()

def printar(var):
    print(var.get())

c1 = Checkbutton(root, text="Checkbox 1", variable=var, command=lambda:printar(var), onvalue="On", offvalue="Off")
c2 = Checkbutton(root, text="Checkbox 2", variable=var2, command=lambda:printar(var2))
c1.grid()
c2.grid()

root.mainloop()