from tkinter import *

app = Tk()

app.title("Gerenciamento Brahma")
app.geometry("1400x800")
app.configure(background="#008")

txt1 = Label(app, text="Curso", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=150, height=30)

txt2 = Label(app, text="Cursos", bg="#ff0", fg="#000")

#ipad   - margin
#pad    - padding
#side   - posisionamento
#fill   - preenchimento
#expand - redimensionamento automatico

txt2.pack(ipadx=20, ipady=20, padx = 5, pady=5, side="top", fill=X, expand=True)

app.mainloop()