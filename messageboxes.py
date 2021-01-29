from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    # Primeiro parametro: titulo do alerta
    # Segundo parametro: conteudo do alerta
    if(messagebox.askyesno("Popup", "Answer")):
        print("yes")
    else:
        print("no")

Button(root, text="Click", command=popup).pack()

root.mainloop()