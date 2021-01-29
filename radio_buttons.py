from tkinter import *
from tkinter import ttk

root = Tk()

root.config(bg="white")

# Usando esta função sempre que houver mudanças na variável o Tkinter saberá
r = IntVar()

#Seta automaticamente o checkbock cujo value é 2
r.set(2)

def mana():
    print(str(r.get()))

radio_button1 = Radiobutton(root, text="Option 1", variable=r, value=1, command=mana)
radio_button2 = Radiobutton(root, text="Option 2", variable=r, value=2)
radio_button1.pack()
radio_button2.pack()



Button(root, text="Click", command=mana).pack()

root.mainloop()