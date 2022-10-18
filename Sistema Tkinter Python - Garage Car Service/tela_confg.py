from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase



def new(id_oficina):
    def alterar_oficina():

            nome = nome_entry.get()
            senha = senha_entry.get()
            telefone = telefone_entry.get()
            endereco = endereco_entry.get()
            cpf = cpf_entry.get()
            email = email_entry.get()
            
            if(nome == "" or telefone == "" or senha == "" or endereco == "" or cpf == "" or email == ""):
                messagebox.showerror(parent=tela_confg,title='Informação de Alteração', message='Preencha Todos os Campos!')
            else:
                DataBase.cursor.execute("""
                UPDATE Oficina
                SET Nome = ?, Senha = ?, Telefone = ?, Endereco = ?, Cpf = ?, Email = ?
                WHERE Cpf = ? AND Id= ?
                """, (nome,senha,telefone,endereco,cpf,email,cpf,id_oficina))
                DataBase.conn.commit()
                tela_confg.destroy()
                messagebox.showinfo(parent=tela_confg,title='Informação de Alteração', message='Alteração da Oficina realizado com sucesso')
                
            

    #criando janela
    tela_confg = Toplevel()
    tela_confg.transient()
    tela_confg.title('Oficina')
    tela_confg.geometry('400x500+100+50')
    tela_confg['background'] = 'white'
    tela_confg.resizable(width = False, height = False)
    #imagem
    logo = PhotoImage(file='icons/logo2.png')
    tela_confg.iconbitmap(default='icons/icon.ico')


    LogoLabel = Label(tela_confg,image=logo, bg='white')
    LogoLabel.place(x=0,y=0)

    

    titulo = Label(tela_confg,text= 'Registro', font=('Franklin Gothic Medium',20), bg = 'white', fg = 'black')
    titulo.place(x=200,y=130)

    DataBase.cursor.execute(('SELECT Nome, Senha, Endereco, Telefone, Cpf, Email FROM Oficina WHERE Id = ?'),(id_oficina,))
    status = 0 
    for linha in DataBase.cursor.fetchall():
       a = linha
    print(a)
    nome = Label(tela_confg,text= 'Nome da Oficina', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    nome.place(x=10,y=180)
    nome_entry = ttk.Entry(tela_confg,width= 45)
    nome_entry.insert(0,a[0])
    nome_entry.place(x=120,y=180)

    senha = Label(tela_confg,text= 'Senha de Usuário', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    senha.place(x=10,y=210)
    senha_entry = ttk.Entry(tela_confg,width= 45)
    senha_entry.insert(0,a[1])
    senha_entry.place(x=120,y=210)

    endereco = Label(tela_confg,text= 'Endereço', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    endereco.place(x=10,y=240)
    endereco_entry = ttk.Entry(tela_confg,width= 45)
    endereco_entry.insert(0,a[2])
    endereco_entry.place(x=120,y=240)

    telefone = Label(tela_confg,text= 'Telefone', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    telefone.place(x=10,y=270)
    telefone_entry = ttk.Entry(tela_confg,width= 45)
    telefone_entry.insert(0,a[3])
    telefone_entry.place(x=120,y=270)

    cpf = Label(tela_confg,text= 'CNPJ/CPF', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    cpf.place(x=10,y=300)
    cpf_entry = ttk.Entry(tela_confg,width= 45)
    cpf_entry.insert(0,a[4])
    cpf_entry['state'] = DISABLED
    cpf_entry.place(x=120,y=300)

    email = Label(tela_confg,text= 'E-mail', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    email.place(x=10,y=330)
    email_entry = ttk.Entry(tela_confg,width= 45)
    email_entry.insert(0,a[5])
    email_entry.place(x=120,y=330)

    #Botões
    SalvarButton = ttk.Button(tela_confg,text = 'Alterar', width=20,command=alterar_oficina)
    SalvarButton.place(x=10,y=380)



    tela_confg.mainloop()
