from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase
import tela_registro
import tele_usuario
import tela_esqueceusenha



def Login():

    
    nome = UserEntry.get()
    senha = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Oficina
    WHERE (Nome == ? and Senha == ?)
    """,(nome, senha))
    print('selecionou')
    
    VerificaLogin = DataBase.cursor.fetchone()

    if(nome in VerificaLogin and senha in VerificaLogin):
        messagebox.showinfo(title='Informação de Login', message='Acesso Confirmado\nBem Vindo!')
        DataBase.cursor.execute(("SELECT Id FROM Oficina WHERE Nome = ?"),(nome,))  
        for linha in DataBase.cursor.fetchall():
                    a = linha
        tele_usuario.usuario(a[0])
    else:
        messagebox.showerror(title='Informação de Login', message='Acesso Negado\nVerifique se está cadastrado no sistema')

def Registro():
    tela_registro.new()

def Esqueci_Senha():
    tela_esqueceusenha.new()


#criando janela
jan_principal = Tk()
jan_principal.title('Oficina')
jan_principal.geometry('700x600+100+50')
jan_principal['background'] = '#C0C0C0'
jan_principal.resizable(width = False, height = False)
#imagem
logo = PhotoImage(file='icons/logo2.png')
carro = PhotoImage(file='icons/carro.png')
jan_principal.iconbitmap(default='icons/icon.ico')
#WIDGETS


LeftFrame = Frame(jan_principal, width = 195, height = 600, bg= 'white', relief='raise')
LeftFrame.pack(side=LEFT)
LogoLabel = Label(LeftFrame, image=logo, bg='white')
LogoLabel.place(x=0,y=0)

RightFrame = Frame(jan_principal, width = 800, height = 600, bg= '#4F4F4F', relief='raise')
RightFrame.pack(side=RIGHT)
Logocarro = Label(RightFrame, image=carro)
Logocarro.place(x=0,y=0)

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

#OU_Label = Label(LeftFrame, text = 'OU', font=('Franklin Gothic Medium',10), bg='white', fg = 'black')
#OU_Label.place(x=85,y=520)

ResgiterButton = ttk.Button(LeftFrame, text = 'Novo Registro', width=20,command=Registro)
ResgiterButton.place(x=30,y=330)

Esqueci_SenhaButton = ttk.Button(LeftFrame, text= "Esqueci Senha", width = 20 ,command=Esqueci_Senha)
Esqueci_SenhaButton.place(x=30, y = 360)


jan_principal.mainloop()

