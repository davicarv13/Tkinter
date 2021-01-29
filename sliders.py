from tkinter import *

root = Tk()

root.geometry("800x400")

vertical = Scale(root, from_= 0, to=200)
vertical.grid()

my_num = IntVar()

horizontal = Scale(root, from_= 0, to=200, orient=HORIZONTAL, variable=my_num)
horizontal.grid()

#Grab slider value
Label(root, text=my_num.get()).grid()
 
root.mainloop()