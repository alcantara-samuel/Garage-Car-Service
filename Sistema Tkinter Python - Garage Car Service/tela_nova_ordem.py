from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import DataBase
import tela2_nova_ordem


def new(id_oficina):
    def SalvarDataBase():
        sql = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
        cliente = cpf_entry.get()
        status_1 = 0 
        for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
            status_1 = 1
        sql1 = ('SELECT * FROM Veiculos WHERE Placa = ? AND Id_Oficina = ?') 
        veiculo = veiculo_entry.get()
        status_2 = 0 
        for row in DataBase.cursor.execute(sql1, (veiculo,id_oficina,)):
            if row[2] == int(cliente):
                status_2 = 1
        if status_1 == 1 and status_2 == 1: 
            Cpf = cpf_entry.get()
            Status = combo_status.get()
            Veiculo = veiculo_entry.get()
            KM = km_entry.get()
            Valor1= valor1_entry.get()
            Data = data_entry.get()
     
            

            if(Cpf == "" or Status == "" or Veiculo == "" or KM == "" or Valor1 == "" or Data == ""):
                messagebox.showerror(title='Informação de Registro de Ordem', message='Preencha Todos os Campos!')
            else:
                cpf_entry.delete("0",END)
                veiculo_entry.delete("0",END)
                km_entry.delete("0",END)
                valor1_entry.delete("0",END)
                data_entry.delete("0",END)
     
                DataBase.cursor.execute("""
                INSERT INTO Ordens(CPF, STATUS, VEICULO, KM, VALOR1, DATA, Id_Oficina) VALUES(?,?, ?, ?, ?, ?, ?)
                """,(Cpf, Status, Veiculo, KM, Valor1, Data, id_oficina))
                DataBase.conn.commit()
                
                DataBase.cursor.execute(("SELECT * FROM Ordens WHERE CPF = ? AND Id_Oficina = ?"),(Cpf,id_oficina,))  
                for linha in DataBase.cursor.fetchall():
                    a = linha
                nova_ordem.destroy()
                tela2_nova_ordem.tela2(a[0],Valor1,Cpf,id_oficina)
                
                
               
        elif(status_1 == 0):
            cpf_entry.delete('0',END)
            messagebox.showerror(title='Informação de Ordem' ,message="O CPF inserido não foi encontrado no servidor")
        else:
            veiculo_entry.delete('0',END)
            messagebox.showerror(title='Informação de Ordem' ,message="A placa do veículo não corresponde ao cliente inserido")
            
            
            
    nova_ordem = Tk()
    nova_ordem.title('Oficina')
    nova_ordem.geometry('630x500+100+50')
    nova_ordem['background'] =  '#F8F8FF'
    nova_ordem.resizable(width = False, height = False)
    #Frame 1
    Frame1 = Frame(nova_ordem, width = 700, height = 60, bg= '#4682B4', relief='raise')
    Frame1.pack(side=TOP)
    logo = PhotoImage(file='icons/nova_ordem.png')
    nova_ordem.iconbitmap(default='icons/icon.ico')
    #Logo = Label(image=logo, bg='#4682B4').place(x=0,y=0)
    titulo = Label(nova_ordem,text = 'CADASTRAR ORDEM', font=('Franklin Gothic Medium',20),bg= '#4682B4', fg = 'white').place(x=80,y=10)


    cpf = Label(nova_ordem,text= 'CPF/CNPJ do Cliente', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=100)
    cpf_entry = ttk.Entry(nova_ordem,width= 40)
    cpf_entry.place(x=30, y=130)



    itens = ["Em Andamento","Concluido","Aprovado","Fechado"]
    combo_status = ttk.Combobox(nova_ordem)
    combo_status["values"] = itens
    combo_status.current(0)
    combo_status.bind("<<ComboboxSelected>>")
    combo_status.place(x=30, y=190)



    veiculo = Label(nova_ordem,text= 'Veículo/Placa', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=100)
    veiculo_entry = ttk.Entry(nova_ordem,width= 40)
    veiculo_entry.place(x=350, y=130)


    km = Label(nova_ordem,text= 'KM', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=160)
    km_entry = ttk.Entry(nova_ordem,width= 40)
    km_entry.place(x=350, y=190)

    descricao = Label(nova_ordem,text= 'Descrição dos itens', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=230)

    mao_obra = Label(nova_ordem,text= '           Mao de Obra           ', font=('Franklin Gothic Medium',13), bg = 'gold', fg = 'white').place(x=30,y=260)


    valor = Label(nova_ordem,text= 'Valor', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=250,y=260)
    valor1_entry = ttk.Entry(nova_ordem,width= 10)
    valor1_entry.place(x=300, y=263)


    data = Label(nova_ordem,text= 'Data', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=400,y=260)
    data_entry = ttk.Entry(nova_ordem,width= 10)
    data_entry.place(x=450, y=263)





    SalvarButton = ttk.Button(nova_ordem,text = 'Salvar', width=20,command=SalvarDataBase)
    SalvarButton.place(x=470,y=470)


    nova_ordem.mainloop()
