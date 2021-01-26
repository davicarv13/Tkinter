from tkinter import *
from tkinter import filedialog

root = Tk()

def openFile():
    filepath = filedialog.askopenfilename()
    print(filepath)

button = Button(root, text="Click", command=openFile)
button.pack()

root.mainloop()