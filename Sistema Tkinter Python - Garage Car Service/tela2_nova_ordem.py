from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import DataBase


def tela2(id_,Valor1,C,id_oficina):

    ListaDescricao = []
    def Adicionar():

            D = des_entry.get()
            Q = qtd_entry.get()
            V = valor2_entry.get()
            if(C == "" or D == "" or Q == "" or V == ""):
                messagebox.showerror(title='Informação de Registro de Ordem', message='Preencha a Entrada do CPF')
            else:
                ListaDescricao.append(int(V))
                DataBase.cursor.execute("""
                INSERT INTO Servicos(CPF, DESCRICAO, QUANTIDADE, VALOR2, ID, Id_Oficina) VALUES(?,?, ?, ?, ?, ?)
                """,(C,D,Q,V,id_,id_oficina))
                DataBase.conn.commit()
                des_entry.delete("0",END)
                qtd_entry.delete("0",END)
                valor2_entry.delete("0", END)


    def Salvar():
        messagebox.showinfo(title='Informação de Registro de Ordem', message='Registro do Ordem foi realizado com sucesso')
        ValorTotal = 0
        for x in ListaDescricao:
            ValorTotal += x
        ValorTotal += int(Valor1)

        DataBase.cursor.execute("""
        UPDATE Ordens 
        SET VALORTOTAL = ? 
        WHERE ID = ?
        """,(ValorTotal,id_))
        DataBase.conn.commit()
        nova_ordem2.destroy()
        


     
    nova_ordem2 = Tk()
    nova_ordem2.title('Oficina')
    nova_ordem2.geometry('630x250+100+50')
    nova_ordem2['background'] =  '#F8F8FF'
    nova_ordem2.resizable(width = False, height = False)
    #Frame 1
    Frame1 = Frame(nova_ordem2, width = 700, height = 60, bg= '#4682B4', relief='raise')
    Frame1.pack(side=TOP)
    logo = PhotoImage(file='icons/nova_ordem.png')
    nova_ordem2.iconbitmap(default='icons/icon.ico')
    #Logo = Label(image=logo, bg='#4682B4').place(x=0,y=0)
    titulo = Label(nova_ordem2,text = 'CADASTRAR SERVIÇOS', font=('Franklin Gothic Medium',20),bg= '#4682B4', fg = 'white').place(x=80,y=10)


    descricao = Label(nova_ordem2,text= 'Descrição', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=100)
    des_entry = ttk.Entry(nova_ordem2,width= 40)
    des_entry.place(x=30, y=130)

    qtd = Label(nova_ordem2,text= 'Quantidade', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=300,y=100)
    qtd_entry = ttk.Entry(nova_ordem2,width= 14)
    qtd_entry.place(x=300, y=130)

    valor2 = Label(nova_ordem2,text= 'Valor', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=420,y=100)
    valor2_entry = ttk.Entry(nova_ordem2,width= 10)
    valor2_entry.place(x=420, y=130)

    AdicionarButton = ttk.Button(nova_ordem2,text = 'Adicionar', width=10,command=Adicionar)
    AdicionarButton.place(x=530,y=128)


    Salvar_Button = ttk.Button(nova_ordem2,text = 'Salvar Aqui', width=20,command=Salvar)
    Salvar_Button.place(x=470,y=200)




    nova_ordem2.mainloop()
