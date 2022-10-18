from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase



def new():
    def SalvarDataBase():
        Name = nome_entry.get()
        Pass = senha_entry.get()
        Endere = endereco_entry.get()
        Fone = telefone_entry.get()
        Cpf = cpf_entry.get()
        Email = email_entry.get()

        if(Name == "" or Pass == "" or Endere == "" or Fone == "" or Cpf == "" or Email == ""):
            messagebox.showerror(title='Informação de Registro', message='Preencha Todos os Campos!')
        else:
            DataBase.cursor.execute("""
            INSERT INTO Oficina(Nome, Senha, Endereco, Telefone, Cpf, Email) VALUES(?, ?, ?, ?, ?, ? )
            """,(Name, Pass, Endere, Fone, Cpf, Email))
            DataBase.conn.commit()
            messagebox.showinfo(title='Informação de Registro', message='Registro foi realizado com sucesso')
            

    #criando janela
    tela_registro = Toplevel()
    tela_registro.transient()
    tela_registro.title('Oficina')
    tela_registro.geometry('400x500+100+50')
    tela_registro['background'] = 'white'
    tela_registro.resizable(width = False, height = False)
    #imagem
    logo = PhotoImage(file='icons/logo2.png')
    tela_registro.iconbitmap(default='icons/icon.ico')


    LogoLabel = Label(tela_registro,image=logo, bg='white')
    LogoLabel.place(x=0,y=0)



    titulo = Label(tela_registro,text= 'Registro', font=('Franklin Gothic Medium',20), bg = 'white', fg = 'black')
    titulo.place(x=200,y=130)

    nome = Label(tela_registro,text= 'Nome da Oficina', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    nome.place(x=10,y=180)
    nome_entry = ttk.Entry(tela_registro,width= 45)
    nome_entry.place(x=120,y=180)

    senha = Label(tela_registro,text= 'Senha de Usuário', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    senha.place(x=10,y=210)
    senha_entry = ttk.Entry(tela_registro,width= 45)
    senha_entry.place(x=120,y=210)

    endereco = Label(tela_registro,text= 'Endereço', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    endereco.place(x=10,y=240)
    endereco_entry = ttk.Entry(tela_registro,width= 45)
    endereco_entry.place(x=120,y=240)

    telefone = Label(tela_registro,text= 'Telefone', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    telefone.place(x=10,y=270)
    telefone_entry = ttk.Entry(tela_registro,width= 45)
    telefone_entry.place(x=120,y=270)

    cpf = Label(tela_registro,text= 'CNPJ/CPF', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    cpf.place(x=10,y=300)
    cpf_entry = ttk.Entry(tela_registro,width= 45)
    cpf_entry.place(x=120,y=300)

    email = Label(tela_registro,text= 'E-mail', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    email.place(x=10,y=330)
    email_entry = ttk.Entry(tela_registro,width= 45)
    email_entry.place(x=120,y=330)

    #Botões
    SalvarButton = ttk.Button(tela_registro,text = 'Salvar', width=20,command=SalvarDataBase)
    SalvarButton.place(x=10,y=380)



    tela_registro.mainloop()