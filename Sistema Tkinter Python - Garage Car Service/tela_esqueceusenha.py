from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as t
import DataBase
import time
import smtplib    
from email.mime.text import MIMEText
    

def new():
    def carrega():
        
        sql = ('SELECT * FROM Oficina WHERE Email = ?') 
        cliente = email_entry.get()
        status = 0 
        for row in DataBase.cursor.execute(sql, (cliente,)):
            status = 1
        if status == 1:
            recuperar()
        else:
            email_entry.delete("0",END)
            messagebox.showerror(parent=tela_novasenha,title='Informação de Recuperação de Senha', message='Email Invalido')

    def recuperar():
            cliente = email_entry.get()
            email_entry.delete("0",END)
            if(cliente == ""):
                messagebox.showerror(parent=tela_novasenha,title='Informação de Recuperação de Senha', message='Campo Invalido')
            else:
                DataBase.cursor.execute(("SELECT Nome, Senha, Email FROM Oficina WHERE Email = ?"),(cliente,))
                for linha in DataBase.cursor.fetchall():
                    a = linha
                
                # conexão com os servidores do google
                smtp_ssl_host = 'smtp.gmail.com'
                smtp_ssl_port = 465
                # username ou email para logar no servidor
                username = 'CarService.ROBO@gmail.com'
                password = 'G@rage1234'

                from_addr = 'CarService.ROBO@gmail.com'
                to_addrs = [a[2]]

                # a biblioteca email possuí vários templates
                # para diferentes formatos de mensagem
                # neste caso usaremos MIMEText para enviar
                # somente texto
                message = MIMEText(f'Olá, segue a abaixo suas informações para recuperar seus dados,\n\nNome: {a[0]}\nSenha: {a[1]}\n\nA equipe do software Car Garage Service agradece sua escolha!')
                message['subject'] = 'Recuperação de conta'
                message['from'] = from_addr
                message['to'] = ', '.join(to_addrs)

                # conectaremos de forma segura usando SSL
                server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                # para interagir com um servidor externo precisaremos
                # fazer login nele
                server.login(username, password)
                server.sendmail(from_addr, to_addrs, message.as_string())
                server.quit()
                

        
    
    
    tela_novasenha = Toplevel()
    tela_novasenha.transient()
    tela_novasenha.title('Oficina')
    tela_novasenha.geometry('400x400+100+50')
    tela_novasenha['background'] = 'white'
    tela_novasenha.resizable(width = False, height = False)
    #imagem
    logo = PhotoImage(file='icons/logo2.png')
    tela_novasenha.iconbitmap(default='icons/icon.ico')


    LogoLabel = Label(tela_novasenha,image=logo, bg='white')
    LogoLabel.place(x=0,y=0)



    titulo = Label(tela_novasenha,text= 'Recuperar Senha', font=('Franklin Gothic Medium',15), bg = 'white', fg = 'black')
    titulo.place(x=200,y=130)

    email = Label(tela_novasenha,text= 'Email Cadastrado', font=('Franklin Gothic Medium',10), bg = 'white', fg = 'black')
    email.place(x=10,y=180)
    email_entry = ttk.Entry(tela_novasenha,width= 40)
    email_entry.place(x=120,y=180)

    
    #Botões
    SalvarButton = ttk.Button(tela_novasenha,text = 'Recuperar', width=20,command=carrega)
    SalvarButton.place(x=260,y=360)



    tela_novasenha.mainloop()