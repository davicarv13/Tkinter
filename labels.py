from tkinter import *

root = Tk()

#Creating labels widgets
myLabel1 = Label(root, text="Hello") 
myLabel2 = Label(root, text="Hello") 

#Putting label on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
