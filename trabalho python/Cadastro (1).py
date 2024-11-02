from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

janela = Tk()

class Funcoes():
    def conecta_bd(self):
        self.connect = sqlite3.connect("Clientes.bd")
        self.cursor = self.connect.cursor()

    def desconecta_bd(self):
        self.connect.close()

    def monta_tabelas(self):
        self.conecta_bd()
        
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Clientes (
                cpf INTEGER PRIMARY KEY,
                nome_cliente CHAR (40) NOT NULL,
                Email_cliente CHAR (60) NOT NULL,
                telefone INTEGER (20) NOT NULL,
                data_nascimento INTEGER (8) NOT NULL,
                idade_cliente INTEGER (3) NOT NULL,
                sexo_cliente CHAR (15) NOT NULL
            ); 
        """)
        
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_produto CHAR (40) NOT NULL,
                quantidade INTEGER NOT NULL,
                valor REAL NOT NULL,
                usuario_inclusao CHAR (40),
                usuario_alteracao CHAR (40)
            ); 
        """)
        self.connect.commit()
        self.desconecta_bd()


class JanelaMain(Funcoes):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame_tela()
        self.botoes()
        self.monta_tabelas()
        janela.mainloop()

    def tela(self):
        self.janela.title("Alunos CT Pontões Barra sul")
        self.janela.geometry("1500x950")
        self.janela.resizable(True, True)
        self.janela.minsize(width=600, height=400)

        self.background_image = Image.open("teste 3.png")
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = Label(self.janela, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

    def frame_tela(self):
        self.frame = Frame(self.janela, bd=4, bg="#F0F8FF",
                           highlightbackground="#FF69B4", highlightthickness=4)
        self.frame.place(relx=0.25, rely=0.2, relwidth=0.50, relheight=0.69)

    def botoes(self):
        self.botao_login = Button(self.frame, text="Login", bd=2, font=(
            "Lexend", 9, "bold"), bg="#1E90FF", fg="white", activebackground="#87CEEB", command=self.abrir_menu)
        self.botao_login.place(relx=0.2, rely=0.63,
                               relwidth=0.28, relheight=0.07)

        self.botao_cadastrar = Button(self.frame, text="Cadastrar", bd=2, bg="#32CD32", fg="white", font=(
            "Lexend", 9, "bold"), command=self.janela_cadastro, activebackground="#98FB98")
        self.botao_cadastrar.place(
            relx=0.5, rely=0.63, relwidth=0.28, relheight=0.07)

        self.lb_titulo = Label(self.frame, text="Faça aqui seu Login:", bg="#F0F8FF", font=(
            "Lexend", 24, "bold"), fg="#6A0DAD")
        self.lb_titulo.place(relx=0.22, rely=0.16)

        self.lb_login = Label(self.frame, text="Login:", bg="#F0F8FF", font=(
            "Lexend", 10, "bold"), fg="#6A0DAD")
        self.lb_login.place(relx=0.2, rely=0.3)

        self.lb_senha = Label(self.frame, text="Senha:", bg="#F0F8FF", font=(
            "Lexend", 9, "bold"), fg="#6A0DAD")
        self.lb_senha.place(relx=0.2, rely=0.46)

        self.entry_login = Entry(self.frame, bd=2)
        self.entry_login.place(relx=0.2, rely=0.37,
                               relheight=0.09, relwidth=0.58)

        self.entry_senha = Entry(self.frame, bd=2, show="•")
        self.entry_senha.place(relx=0.2, rely=0.52,
                               relheight=0.09, relwidth=0.58)

    def abrir_menu(self):
        self.janela.withdraw()
        self.menu_janela = JanelaMenu(self.entry_login.get())  
    def janela_cadastro(self):
        self.janela.withdraw()
        self.janela_cad = Toplevel(self.janela)
        self.janela_cad.title("Cadastro")
        self.janela_cad.geometry("900x900")
        self.janela_cad.resizable(True, True)
        self.janela_cad.minsize(width=600, height=400)

        self.background_image_cad = Image.open("imagem 2.jpg")
        self.background_image_cad = ImageTk.PhotoImage(self.background_image_cad)
        self.background_label_cad = Label(
            self.janela_cad, image=self.background_image_cad)
        self.background_label_cad.place(relwidth=1, relheight=1)

        self.frame_janela_cad()

        self.botao_voltar = Button(self.janela_cad, text="Voltar", command=self.voltar_login,
                                   bg="red", fg="black", font=("Lexend", 12, "bold"))
        self.botao_voltar.place(
            relx=0.32, rely=0.7, relwidth=0.35, relheight=0.06)

    def voltar_login(self):
        self.janela_cad.destroy()
        self.janela.deiconify()

    def frame_janela_cad(self):
        self.frame_cad = Frame(self.janela_cad, bg="#F0F8FF",
                               highlightbackground="#FF69B4", highlightthickness=4)
        self.frame_cad.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        self.label_titulo_cad = Label(self.frame_cad, text="Realize seu Cadastro:", bg="#F0F8FF", font=(
            "Lexend", 24, "bold"), fg="#6A0DAD")
        self.label_titulo_cad.place(relx=0.22, rely=0.1)

        self.label_nome_cad = Label(self.frame_cad, text="Login:", bg="#F0F8FF", font=(
            "Lexend", 14, "bold"), fg="#6A0DAD")
        self.label_nome_cad.place(relx=0.2, rely=0.25)
        self.entry_nome_cad = Entry(self.frame_cad, bd=3)
        self.entry_nome_cad.place(
            relx=0.2, rely=0.31, relwidth=0.58, relheight=0.09)

        self.label_senha_cad = Label(self.frame_cad, text="Senha:", bg="#F0F8FF", font=(
            "Lexend", 14, "bold"), fg="#6A0DAD")
        self.label_senha_cad.place(relx=0.2, rely=0.42)
        self.entry_senha_cad = Entry(self.frame_cad, bd=3, show="•")
        self.entry_senha_cad.place(
            relx=0.2, rely=0.47, relwidth=0.58, relheight=0.09)

        self.botao_cadastrar = Button(self.frame_cad, text="Cadastrar", bd=2, bg="#32CD32", fg="white", font=(
            "Lexend", 12, "bold"), command=self.salvar_cadastro, activebackground="#98FB98")
        self.botao_cadastrar.place(
            relx=0.2, rely=0.6, relwidth=0.58, relheight=0.09)

    def salvar_cadastro(self):
        nome = self.entry_nome_cad.get()
        senha = self.entry_senha_cad.get()
        print(f"Nome: {nome}, Senha: {senha}")
        self.janela_cad.destroy()
        self.janela.deiconify()


class JanelaMenu(Funcoes):
    def __init__(self, usuario_logado):
        self.usuario_logado = usuario_logado  
        self.janela_menu = Toplevel(janela)
        self.janela_menu.title("Menu de Produtos")
        self.janela_menu.geometry("1700x600")
        self.janela_menu.resizable(True, True)

        self.frame_menu = Frame(self.janela_menu, bg="#F0F8FF",
                                highlightbackground="#FF69B4", highlightthickness=4)
        self.frame_menu.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.label_titulo_menu = Label(self.frame_menu, text="Menu de Produtos", bg="#F0F8FF", font=(
            "Lexend", 24, "bold"), fg="#6A0DAD")
        self.label_titulo_menu.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_menu, columns=("ID", "Produto", "Quantidade", "Valor", "Usuário Inclusão", "Usuário Alteração"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Valor", text="Valor")
        self.tree.heading("Usuário Inclusão", text="Usuário Inclusão")
        self.tree.heading("Usuário Alteração", text="Usuário Alteração")
        self.tree.pack(fill=BOTH, expand=True)

        self.botao_adicionar = Button(self.frame_menu, text="Adicionar Produto", command=self.adicionar_produto)
        self.botao_adicionar.pack(pady=5)

        self.botao_alterar = Button(self.frame_menu, text="Alterar Produto", command=self.alterar_produto)
        self.botao_alterar.pack(pady=5)

        self.botao_deletar = Button(self.frame_menu, text="Deletar Produto", command=self.deletar_produto)
        self.botao_deletar.pack(pady=5)

        self.carregar_produtos()

    def adicionar_produto(self):
        self.janela_adicionar = Toplevel(self.janela_menu)
        self.janela_adicionar.title("Adicionar Produto")
        self.janela_adicionar.geometry("400x300")

        Label(self.janela_adicionar, text="Nome do Produto:").pack()
        self.entry_produto = Entry(self.janela_adicionar)
        self.entry_produto.pack()

        Label(self.janela_adicionar, text="Quantidade:").pack()
        self.entry_quantidade = Entry(self.janela_adicionar)
        self.entry_quantidade.pack()

        Label(self.janela_adicionar, text="Valor:").pack()
        self.entry_valor = Entry(self.janela_adicionar)
        self.entry_valor.pack()

        Button(self.janela_adicionar, text="Salvar", command=self.salvar_produto).pack(pady=10)

    def salvar_produto(self):
        produto = self.entry_produto.get()
        quantidade = self.entry_quantidade.get()
        valor = self.entry_valor.get()
        
        if produto and quantidade.isdigit() and valor.replace('.', '', 1).isdigit():
            self.conecta_bd()
            self.cursor.execute("INSERT INTO Produtos (nome_produto, quantidade, valor, usuario_inclusao) VALUES (?, ?, ?, ?)",
                                (produto, int(quantidade), float(valor), self.usuario_logado))
            self.connect.commit()
            self.desconecta_bd()
            self.carregar_produtos()
            self.janela_adicionar.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

    def carregar_produtos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.conecta_bd()
        self.cursor.execute("SELECT * FROM Produtos")
        produtos = self.cursor.fetchall()
        for produto in produtos:
            self.tree.insert("", "end", values=produto)
        self.desconecta_bd()

    def alterar_produto(self):
        try:
            selected_item = self.tree.selection()[0]
            produto_data = self.tree.item(selected_item, "values")

            self.janela_alterar = Toplevel(self.janela_menu)
            self.janela_alterar.title("Alterar Produto")
            self.janela_alterar.geometry("400x300")

            Label(self.janela_alterar, text="Nome do Produto:").pack()
            self.entry_produto_alterar = Entry(self.janela_alterar)
            self.entry_produto_alterar.insert(0, produto_data[1])
            self.entry_produto_alterar.pack()

            Label(self.janela_alterar, text="Quantidade:").pack()
            self.entry_quantidade_alterar = Entry(self.janela_alterar)
            self.entry_quantidade_alterar.insert(0, produto_data[2])
            self.entry_quantidade_alterar.pack()

            Label(self.janela_alterar, text="Valor:").pack()
            self.entry_valor_alterar = Entry(self.janela_alterar)
            self.entry_valor_alterar.insert(0, produto_data[3])
            self.entry_valor_alterar.pack()

            Button(self.janela_alterar, text="Salvar", command=lambda: self.salvar_alteracao(produto_data[0])).pack(pady=10)
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um produto para alterar.")

    def salvar_alteracao(self, produto_id):
        produto = self.entry_produto_alterar.get()
        quantidade = self.entry_quantidade_alterar.get()
        valor = self.entry_valor_alterar.get()

        if produto and quantidade.isdigit() and valor.replace('.', '', 1).isdigit():
            self.conecta_bd()
            self.cursor.execute("UPDATE Produtos SET nome_produto=?, quantidade=?, valor=?, usuario_alteracao=? WHERE id=?",
                                (produto, int(quantidade), float(valor), self.usuario_logado, produto_id))
            self.connect.commit()
            self.desconecta_bd()
            self.carregar_produtos()
            self.janela_alterar.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

    def deletar_produto(self):
        try:
            selected_item = self.tree.selection()[0]
            produto_data = self.tree.item(selected_item, "values")
            self.conecta_bd()
            self.cursor.execute("DELETE FROM Produtos WHERE id=?", (produto_data[0],))
            self.connect.commit()
            self.desconecta_bd()
            self.carregar_produtos()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um produto para deletar.")


JanelaMain()

