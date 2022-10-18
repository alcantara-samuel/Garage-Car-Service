from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase



def new(id_oficina):
    

    def SalvarDataBase():
        sql1 = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
        cliente = vincular_entry.get()
        status_1 = 0 
        for row in DataBase.cursor.execute(sql1, (cliente,id_oficina,)):
            status_1 = 1 
        sql2 = ('SELECT * FROM Veiculos WHERE Placa = ? AND Id_Oficina = ?') 
        cliente2 = placa_entry.get()
        status_2 = 0 
        for row in DataBase.cursor.execute(sql2, (cliente2,id_oficina,)):
            status_2 = 1 
        if status_1 == 1 and status_2 == 0: 
            Marca = marca_entry.get()
            Placa = placa_entry.get()
            Vincular = vincular_entry.get()
            Cor = cor_entry.get()
            Chassi = chassi_entry.get()
            
            

            
            
            if(Marca == "" or Placa == "" or Vincular == "" or Cor == "" or Chassi == ""):
                messagebox.showerror(title='Informação de Registro de Veículo', message='Preencha Todos os Campos!')
            else:
            
                marca_entry.delete("0",END)
                placa_entry.delete("0",END)
                vincular_entry.delete("0",END)
                cor_entry.delete("0",END)
                chassi_entry.delete("0",END)
            
                DataBase.cursor.execute("""
                INSERT INTO Veiculos(Marca, Placa, Vincular, Cor, Chassi, Id_Oficina) VALUES(?, ?, ?, ?, ?, ?)
                """,(Marca, Placa, Vincular, Cor, Chassi,id_oficina))
                DataBase.conn.commit()
                novo_veiculo.destroy()
                messagebox.showinfo(title='Informação de Registro de Veículo', message='Registro do Veículo foi realizado com sucesso')
                
        elif(status_1 == 0):
            messagebox.showerror(title='Informação de Registro de Veículo', message='CPF não encontrado')
            vincular_entry.delete("0",END)
        elif(status_2 == 1):
            messagebox.showerror(title='Informação de Registro de Veículo', message='Placa está cadastrada no sistema')
            placa_entry.delete("0",END)
        
            
    novo_veiculo = Tk()
    novo_veiculo.title('Oficina')
    novo_veiculo.geometry('630x500+100+50')
    novo_veiculo['background'] =  '#F8F8FF'
    novo_veiculo.resizable(width = False, height = False)
    #Frame 1
    Frame1 = Frame(novo_veiculo, width = 700, height = 60, bg= '#4682B4', relief='raise')
    Frame1.pack(side=TOP)
    logo = PhotoImage(file='icons/tela_novo_veiculo.png')
    novo_veiculo.iconbitmap(default='icons/icon.ico')
    #Logo = Label(image=logo, bg='#4682B4').place(x=0,y=0)
    titulo = Label(novo_veiculo,text = 'CADASTRAR VEÍCULO', font=('Franklin Gothic Medium',20),bg= '#4682B4', fg = 'white').place(x=80,y=10)


    marca = Label(novo_veiculo,text= 'Marca/Modelo', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=100)
    marca_entry = ttk.Entry(novo_veiculo,width= 40)
    marca_entry.place(x=30, y=130)

    placa = Label(novo_veiculo,text= 'Placa', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=160)
    placa_entry = ttk.Entry(novo_veiculo,width= 40)
    placa_entry.place(x=30, y=190)

    vincular = Label(novo_veiculo,text= 'Vincular ao Cliente/CPF', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=30,y=220)
    vincular_entry = ttk.Entry(novo_veiculo,width= 40)
    vincular_entry.place(x=30, y=250)

    cor = Label(novo_veiculo,text= 'Cor', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=100)
    cor_entry = ttk.Entry(novo_veiculo,width= 40)
    cor_entry.place(x=350, y=130)

    chassi = Label(novo_veiculo,text= 'Chassi', font=('Franklin Gothic Medium',13), bg = '#F8F8FF', fg = 'black').place(x=350,y=160)
    chassi_entry = ttk.Entry(novo_veiculo,width= 40)
    chassi_entry.place(x=350, y=190)







    SalvarButton = ttk.Button(novo_veiculo,text = 'Salvar', width=20,command=SalvarDataBase)
    SalvarButton.place(x=470,y=420)


    novo_veiculo.mainloop()