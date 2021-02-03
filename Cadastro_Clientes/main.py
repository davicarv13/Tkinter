from tkinter import *
from tkinter import ttk
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from PIL import ImageTk, Image

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("clientes.pdf")

    def geraRelatCliente(self):
        self.c = canvas.Canvas("clientes.pdf")
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, "Codigo:")
        self.c.drawString(50, 670, "Nome:")
        self.c.drawString(50, 630, "Telefone:")
        self.c.drawString(50, 600, "Cidade:")

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 630, self.telefoneRel)
        self.c.drawString(150, 600, self.cidadeRel)

        self.c.rect(20, 720, 550, 200, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()

class Funcs():
    def limpa_tela(self):
        for entry in self.entrys_frame_1:
            entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd"); print("Conectando ao banco de dados")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def montaTabelas(self):
        self.conecta_bd(); print("Conectando ao banco de dados")

        #Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)

        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.conecta_bd()
        self.variaveis()
        self.cursor.execute(""" INSERT INTO clientes(nome_cliente, telefone, cidade)
            VALUES(?,?,?)""", (self.nome, self.telefone, self.cidade))

        self.conn.commit()
        self.select_lista()
        self.limpa_tela()
        self.desconecta_bd()
    
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()

        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCli.insert("", END, values=i)

        self.desconecta_bd()

    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, "%")
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente""" % nome)
        buscaNomeCli = self.cursor.fetchall()
        
        for i in buscaNomeCli:
            self.listaCli.insert("", END, values=i)
            
        self.limpa_tela()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()

        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, 
            cidade = ? WHERE cod = ?;""", (self.nome, self.telefone, self.cidade, self.codigo))

        self.conn.commit()

        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu()
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit() : self.root.destroy()

        menubar.add_cascade(label = "Opções", menu = filemenu)
        menubar.add_cascade(label = "Sobre", menu = filemenu2)

        filemenu.add_command(label="Sair", command=quit)
        filemenu.add_command(label="Limpa Cliente", command=self.limpa_tela)
        filemenu.add_command(label="Ficha do cliente", command=self.geraRelatCliente)

class Application(Funcs, Relatorios):
    def __init__(self):
        #Cria equivalencia da variavel root
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.menus()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#1e3743")
        self.root.geometry("700x500")
        #Primeiro parametro de resizable define se a janela pode ser redimensionana na horizontal
        #Segundo parametro de resizable define se a janela pode ser redimensionana na vertical
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#dfe3ee", 
            highlightbackground="#759fe6", highlightthickness=3)

        self.frame_2 = Frame(self.root, bd=4, bg="#dfe3ee", 
            highlightbackground="#759fe6", highlightthickness=3)


        #relx e relx definem margin relativas
        #relwidth e relheight definem tamanhos relativos ao tamanho da janela
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        #Definindo a borda dos botões limpar e buscar
        self.canvas_bt = Canvas(self.frame_1, bd=0, bg="black", highlightbackground = "gray",
            highlightthickness=6)
        self.canvas_bt.place(relx = 0.19, rely=0.09, relwidth=0.22, relheight=0.19)

        self.btn_limpar = Button(self.frame_1, text="Limpar", command=self.limpa_tela)
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        """
        #Criação botao novo
        #imgNovo

        self.imgNovo = PhotoImage(file = "botaonovo.gif")
        self.imgNovo = self.imgNovo.subsample(2, 2)

        self.style = ttk.Style()
        self.style.configure("BW.TButton", relwidth=1, relheight=1, foreground="gray",
            borderwidth=0, bordercolor="gray", background="#dfe3ee",
            image=self.imgNovo)

        self.btn_novo = ttk.Button(self.frame_1, style="BW.TButton", command=self.add_cliente)
        self.btn_novo.config(image=self.imgNovo)"""   
 
        self.btn_buscar = Button(self.frame_1, text="Buscar", command=self.busca_cliente)
        self.btn_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.btn_novo = Button(self.frame_1, text="Novo", command=self.add_cliente)
        self.btn_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.btn_alterar = Button(self.frame_1, text="Alterar", command=self.altera_cliente)
        self.btn_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.btn_apagar = Button(self.frame_1, text="Apagar", command=self.deleta_cliente)
        self.btn_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lista_botoes_frame_1 = []

        #Adiciona todos os botões a uma lista
        self.lista_botoes_frame_1.extend([self.btn_limpar, self.btn_novo, self.btn_buscar,
            self.btn_apagar, self.btn_alterar])

        #Estiliza todos os botões da lista
        for btn in self.lista_botoes_frame_1:
            btn.config(bd=2, bg="#107db2", fg="white", font=("verdana", 8, "bold"),
            activebackground="#108ecb", activeforeground="white")

        #Criação da label e entrada do nome
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

        #Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        #Criação de label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone")
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        #Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

        #Adiciona todos as labels a uma lista
        self.labels_frame_1 = []
        self.labels_frame_1.extend([self.lb_codigo, self.lb_nome, self.lb_telefone,
             self.lb_cidade])

        #Adiciona todas as entrys a uma lista
        self.entrys_frame_1 = []
        self.entrys_frame_1.extend([self.codigo_entry, self.telefone_entry, 
            self.nome_entry, self.cidade_entry])
        
        #Define mesma cor de fundo do frame para todas as labels
        #Define mesma cor de fundo dos botoes para fonte das labels
        for label in self.labels_frame_1:
            label.config(bg=self.frame_1.cget("bg"), fg=self.btn_limpar.cget("bg"))

    def lista_frame2(self):
        self.listaCli =  ttk.Treeview(self.frame_2, height=3, 
            column=("Col1", "Col2","Col3","Col4"))

        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        #Cria scrollbar e adiciona ela a listaCli
        self.scrollLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scrollLista.set)

        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

Application()