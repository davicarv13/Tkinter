from tkinter import *
from tkinter import filedialog

root = Tk()

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/home/davi/", title="Select a file:", filetypes=(('png files', "*.png"),("all files", "*.*")))
    print(filepath)

button = Button(root, text="Click", command=openFile)
button.pack()

root.mainloop()