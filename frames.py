from tkinter import *
from tkinter import ttk

root = Tk()

frame1 = LabelFrame(root, text="Label Frame 1", pady=20, padx=50, width=root.winfo_screenwidth())
frame2 = LabelFrame(root, text="Label Frame 2", pady=20, padx=20, height=root.winfo_screenheight())

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

label1 = Label(frame1, text="Frame 1")
label2 = Label(frame2, text="Frame 2")

label1.grid(row=0, column=0)
label2.grid(row=0, column=0)

root.mainloop()