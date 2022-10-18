from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

def new(id_oficina):
    def SalvarDataBase():
        sql = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
        cliente = cpf_cnpj_entry.get()
        status = 0 
        for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
            status = 1
        if status == 0:
            Name = nome_entry.get()
            Tele = telefone_entry.get()
            Celular = celular_entry.get()
            Endereco = endereco_entry.get()
            Cpf = cpf_cnpj_entry.get()
            Cidade = cidade_entry.get()
            Estado = estado_entry.get()
            Oficina = id_oficina
            
            nome_entry.delete("0",END) 
            telefone_entry.delete("0",END) 
            celular_entry.delete("0",END) 
            endereco_entry.delete("0",END) 
            cpf_cnpj_entry.delete("0",END) 
            cidade_entry.delete("0",END) 
            estado_entry.delete("0",END) 
            

            if(Name == "" or Tele == "" or Celular == "" or Endereco == "" or Cpf == "" or Cidade == "" or Estado == ""):
                messagebox.showerror(title='Informação de Registro de Cliente', message='Preencha Todos os Campos!')
            else:
                nome_entry.delete("0",END) 
                telefone_entry.delete("0",END) 
                celular_entry.delete("0",END) 
                endereco_entry.delete("0",END) 
                cpf_cnpj_entry.delete("0",END) 
                cidade_entry.delete("0",END) 
                estado_entry.delete("0",END) 
                
            
                DataBase.cursor.execute("""
                INSERT INTO Clientes(Nome, Telefone, Celular, Endereco, Cpf, Cidade, Estado, Id_Oficina) VALUES(?, ?, ?, ?, ?, ?, ? ,?)
                """,(Name, Tele, Celular, Endereco, Cpf, Cidade, Estado, Oficina))
                DataBase.conn.commit()
                novo_cliente.destroy()
                messagebox.showinfo(title='Informação de Registro de Cliente', message='Registro do Cliente foi realizado com sucesso')
          
        else:
            messagebox.showerror(title='Informação de Registro de Veículo', message='CPF já está cadastrado no sistema')
            cpf_cnpj_entry.delete("0",END)    
                
    novo_cliente = Tk()
    novo_cliente.title('Oficina')
    novo_cliente.geometry('630x500+100+50')
    novo_cliente['background'] =  '#F8F8FF'
    novo_cliente.resizable(width = False, height = False)
    #Frame 1
    Frame1 = Frame(novo_cliente, width = 700, height = 60, bg= '#4682B4', relief='raise')
    Frame1.pack(side=TOP)
    logo = PhotoImage(file='icons/tela_novo_cliente.png')
    novo_cliente.iconbitmap(default='icons/icon.ico')
    #Logo = Label(image=logo, bg='#4682B4').place(x=0,y=0)
    titulo = Label(novo_cliente,text = 'CADASTRAR CLIENTE', font=('Franklin Gothic Medium',20),bg= '#4682B4', fg = 'white').place(x=80,y=10)


    nome = Label(novo_cliente,text= 'Nome completo', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=100)
    nome_entry = ttk.Entry(novo_cliente,width= 40)
    nome_entry.place(x=30, y=130)

    telefone = Label(novo_cliente,text= 'Telefone', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=160)
    telefone_entry = ttk.Entry(novo_cliente,width= 40)
    telefone_entry.place(x=30, y=190)

    endereco = Label(novo_cliente,text= 'Endereço', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=220)
    endereco_entry = ttk.Entry(novo_cliente,width= 40)
    endereco_entry.place(x=30, y=250)

    cpf_cnpj = Label(novo_cliente,text= 'CPF/CNPJ', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=100)
    cpf_cnpj_entry = ttk.Entry(novo_cliente,width= 40)
    cpf_cnpj_entry.place(x=350, y=130)

    celular = Label(novo_cliente,text= 'Celular', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=160)
    celular_entry = ttk.Entry(novo_cliente,width= 40)
    celular_entry.place(x=350, y=190)

    cidade = Label(novo_cliente,text= 'Cidade', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=220)
    cidade_entry = ttk.Entry(novo_cliente,width= 25)
    cidade_entry.place(x=350, y=250)

    estado = Label(novo_cliente,text= 'Estado - UF', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=520,y=220)
    estado_entry = ttk.Entry(novo_cliente,width= 12)
    estado_entry.place(x=520, y=250)


    SalvarButton = ttk.Button(novo_cliente,text = 'Salvar', width=20,command=SalvarDataBase)
    SalvarButton.place(x=470,y=420)


    novo_cliente.mainloop()