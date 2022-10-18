from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import DataBase


ListaDescricao = []
def Adicionar():
    sql = ('SELECT * FROM Clientes WHERE Cpf = ?') 
    cliente = cpf_entry.get()
    status = 0 
    for row in DataBase.cursor.execute(sql, (cliente,)):
        status = 1 
    if status == 1: 
        C = cpf_entry.get()
        D = des_entry.get()
        Q = qtd_entry.get()
        V = valor2_entry.get()
        if(C == "" or D == "" or Q == "" or V == ""):
            messagebox.showerror(title='Informação de Registro de Orçamento', message='Preencha a Entrada do CPF')
        else:
            ListaDescricao.append(int(V))
            DataBase.cursor.execute("""
            INSERT INTO Servicos(CPF, DESCRICAO, QUANTIDADE, VALOR2) VALUES(?, ?, ?, ?)
            """,(C,D,Q,V))
            DataBase.conn.commit()
            des_entry.delete("0",END)
            qtd_entry.delete("0",END)
            valor2_entry.delete("0", END)
    else:
        cpf_entry.delete('0',END)
        messagebox.showerror(title='Informação de Orçamento' ,message="O CPF inserido não foi encontrado no servidor")


def SalvarDataBase():
    sql = ('SELECT * FROM Clientes WHERE Cpf = ?') 
    cliente = cpf_entry.get()
    status = 0 
    for row in DataBase.cursor.execute(sql, (cliente,)):
        status = 1 
    if status == 1: 
        ValorTotal = 0
        for x in ListaDescricao:
            ValorTotal += x
        Cpf = cpf_entry.get()
        Status = status_entry.get()
        Veiculo = veiculo_entry.get()
        KM = km_entry.get()
        Valor1= valor1_entry.get()
        ValorTotal += int(Valor1)
        

        if(Cpf == "" or Status == "" or Veiculo == "" or KM == "" or Valor1 == ""):
            messagebox.showerror(title='Informação de Registro de Ordem', message='Preencha Todos os Campos!')
        else:
            DataBase.cursor.execute("""
            INSERT INTO Ordens(CPF, STATUS, VEICULO, KM, VALOR1, VALORTOTAL) VALUES(?, ?, ?, ?, ?, ?)
            """,(Cpf, Status, Veiculo, KM, Valor1, ValorTotal))
            DataBase.conn.commit()
            messagebox.showinfo(title='Informação de Registro de Ordem', message='Registro do Ordem foi realizado com sucesso')
            novo_orcamento.exit()
    else:
        cpf_entry.delete('0',END)
        messagebox.showerror(title='Informação de Orçamento' ,message="O CPF inserido não foi encontrado no servidor")
        
novo_orcamento = Tk()
novo_orcamento.title('Oficina')
novo_orcamento.geometry('630x500+100+50')
novo_orcamento['background'] =  '#F8F8FF'
novo_orcamento.resizable(width = False, height = False)
#Frame 1
Frame1 = Frame(novo_orcamento, width = 700, height = 60, bg= '#4682B4', relief='raise')
Frame1.pack(side=TOP)
logo = PhotoImage(file='icons/novo_orçamento.png')
novo_orcamento.iconbitmap(default='icons/icon.ico')
Logo = Label(image=logo, bg='#4682B4').place(x=0,y=0)
titulo = Label(text = 'CADASTRAR ORÇAMENTO', font=('Franklin Gothic Medium',20),bg= '#4682B4', fg = 'white').place(x=80,y=10)


cpf = Label(text= 'CPF/CNPJ do Cliente', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=100)
cpf_entry = ttk.Entry(width= 40)
cpf_entry.place(x=30, y=130)

status = Label(text= 'Status', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=160)
status_entry = ttk.Entry(width= 40)
status_entry.place(x=30, y=190)

veiculo = Label(text= 'Veículo/Placa', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=100)
veiculo_entry = ttk.Entry(width= 40)
veiculo_entry.place(x=350, y=130)


km = Label(text= 'KM', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=160)
km_entry = ttk.Entry(width= 40)
km_entry.place(x=350, y=190)

descricao = Label(text= 'Descrição dos itens', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=230)

mao_obra = Label(text= '           Mao de Obra           ', font=('Franklin Gothic Medium',13), bg = 'gold', fg = 'white').place(x=30,y=260)


valor = Label(text= 'Valor', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=250,y=260)
valor1_entry = ttk.Entry(width= 10)
valor1_entry.place(x=300, y=263)



descricao = Label(text= 'Descrição', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=320)
des_entry = ttk.Entry(width= 40)
des_entry.place(x=30, y=350)

qtd = Label(text= 'Quantidade', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=300,y=320)
qtd_entry = ttk.Entry(width= 14)
qtd_entry.place(x=300, y=350)

valor2 = Label(text= 'Valor', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=420,y=320)
valor2_entry = ttk.Entry(width= 10)
valor2_entry.place(x=420, y=350)

AdicionarButton = ttk.Button(text = 'Adicionar', width=10,command=Adicionar)
AdicionarButton.place(x=530,y=348)


SalvarButton = ttk.Button(text = 'Salvar', width=20,command=SalvarDataBase)
SalvarButton.place(x=470,y=470)


novo_orcamento.mainloop()

print(ListaDescricao)