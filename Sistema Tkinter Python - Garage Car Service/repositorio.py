from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase
import registro


def Registro():
    RightFrame = Frame(jan_principal, width = 800, height = 600, bg= '#4F4F4F', relief='raise')
    RightFrame.pack(side=RIGHT)
    def limpar():
        titulo.place_forget()
        nome.place_forget()
        nome_entry.place_forget()
        senha.place_forget()
        senha_entry.place_forget()
        endereco.place_forget()
        endereco_entry.place_forget()
        telefone.place_forget()
        telefone_entry.place_forget()
        cpf.place_forget()
        cpf_entry.place_forget()
        rg.place_forget()
        rg_entry.place_forget()
        email.place_forget()
        email_entry.place_forget()
        SairButton.place_forget()
        SalvarButton.place_forget()
        
    def SalvarDataBase():
        Name = nome_entry.get()
        Pass = senha_entry.get()
        Endere = endereco_entry.get()
        Fone = telefone_entry.get()
        Cpf = cpf_entry.get()
        Rg = rg_entry.get()
        Email = email_entry.get()

        if(Name == "" or Pass == "" or Endere == "" or Fone == "" or Cpf == "" or Rg == "" or Email == ""):
            messagebox.showerror(title='Informação de Registro', message='Preencha Todos os Campos!')
        else:
            DataBase.cursor.execute("""
            INSERT INTO Oficina(Nome, Senha, Endereco, Telefone, Cpf, Rg, Email) VALUES(?, ?, ?, ?, ?, ? ,?)
            """,(Name, Pass, Endere, Fone, Cpf, Rg, Email))
            DataBase.conn.commit()
            messagebox.showinfo(title='Informação de Registro', message='Registro foi realizado com sucesso')
    
    titulo = Label(RightFrame,text= 'Registro', font=('Franklin Gothic Medium',20), bg = '#4F4F4F', fg = 'white')
    titulo.place(x=200,y=10)
   
    nome = Label(RightFrame,text= 'Nome de Usuário', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    nome.place(x=10,y=50)
    nome_entry = ttk.Entry(RightFrame, width= 45)
    nome_entry.place(x=120,y=50)

    senha = Label(RightFrame,text= 'Senha de Usuário', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    senha.place(x=10,y=90)
    senha_entry = ttk.Entry(RightFrame, width= 45)
    senha_entry.place(x=120,y=90)

    endereco = Label(RightFrame,text= 'Endereço', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    endereco.place(x=10,y=130)
    endereco_entry = ttk.Entry(RightFrame, width= 45)
    endereco_entry.place(x=120,y=130)

    telefone = Label(RightFrame,text= 'Telefone', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    telefone.place(x=10,y=180)
    telefone_entry = ttk.Entry(RightFrame, width= 45)
    telefone_entry.place(x=120,y=180)

    cpf = Label(RightFrame,text= 'CPF', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    cpf.place(x=10,y=230)
    cpf_entry = ttk.Entry(RightFrame, width= 45)
    cpf_entry.place(x=120,y=230)

    rg = Label(RightFrame,text= 'RG', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    rg.place(x=10,y=280)
    rg_entry = ttk.Entry(RightFrame, width= 45)
    rg_entry.place(x=120,y=280)

    email = Label(RightFrame,text= 'E-mail', font=('Franklin Gothic Medium',10), bg = 'black', fg = 'white')
    email.place(x=10,y=320)
    email_entry = ttk.Entry(RightFrame, width= 45)
    email_entry.place(x=120,y=320)

    #Botões
    SalvarButton = ttk.Button(RightFrame, text = 'Salvar', width=20,command=SalvarDataBase)
    SalvarButton.place(x=10,y=380)
    
    SairButton = ttk.Button(RightFrame, text = 'Sair', width=20,command=limpar)
    SairButton.place(x=300,y=380)
    
    return RightFrame
    
def Login():

    
    email = UserEntry.get()
    senha = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Oficina
    WHERE (Email == ? and Senha == ?)
    """,(email, senha))
    print('selecionou')
    
    VerificaLogin = DataBase.cursor.fetchone()
    try:
        if(email in VerificaLogin and senha in VerificaLogin):
            #messagebox.showinfo(title='Informação de Login', message='Acesso Confirmado\nBem Vindo!')
            RightFrame.pack_forget()
            a = Frame(jan_principal, width = 800, height = 600, bg= '#4F4F4F', relief='raise')
            a.pack(side=RIGHT)
            
            
    except:
        messagebox.showerror(title='Informação de Login', message='Acesso Negado\nVerifique se está cadastrado no sistema')
    


#criando janela
jan_principal = Tk()
jan_principal.title('Oficina')
jan_principal.geometry('1000x600+100+50')
jan_principal['background'] = '#C0C0C0'
jan_principal.resizable(width = False, height = False)
#imagem
logo = PhotoImage(file='icons/logo2.png')
jan_principal.iconbitmap(default='icons/icon.ico')
#WIDGETS



LeftFrame = Frame(jan_principal, width = 195, height = 600, bg= 'white', relief='raise')
LeftFrame.pack(side=LEFT)
LogoLabel = Label(LeftFrame, image=logo, bg='white')
LogoLabel.place(x=0,y=0)

"--------ENTRADA DE USUÁRIO-----------"
UserLabel = Label(LeftFrame,text= 'Nome de usuário', font=('Franklin Gothic Medium',10), bg = '#4F4F4F', fg = 'white')
UserLabel.place(x=0,y=200)
UserEntry = ttk.Entry(LeftFrame, width= 35)
UserEntry.place(x=0,y=225)

PassLabel = Label(LeftFrame, text = 'Senha de usuário', font=('Franklin Gothic Medium',10), bg='#4F4F4F', fg = 'white')
PassLabel.place(x=0,y=250)
PassEntry = ttk.Entry(LeftFrame, width= 35,show = '•')
PassEntry.place(x=0,y=275)

LoginButton = ttk.Button(LeftFrame, text = 'Login', width=20, command=Login)
LoginButton.place(x=30,y=300)

OU_Label = Label(LeftFrame, text = 'OU', font=('Franklin Gothic Medium',10), bg='white', fg = 'black')
OU_Label.place(x=85,y=330)

ResgiterButton = ttk.Button(LeftFrame, text = 'Registro', width=20, command=Registro)
ResgiterButton.place(x=30,y=360)





jan_principal.mainloop()
