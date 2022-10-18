from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase
import tkinter as tk

#---------Janelas Extras-------------
import tela_servicos
import tela_alterastatus

import tela_nova_ordem
import tela_novo_cliente
import tela_novo_veiculo
import tela_confg


def usuario(id_oficina):

        
    #criando janela
    tela_usuario = Toplevel()
    tela_usuario.transient()
    tela_usuario.title('Oficina')
    tela_usuario.geometry('1000x600+350+50')
    tela_usuario['background'] = '#C0C0C0'
    tela_usuario.resizable(width = False, height = False)
    #imagem
    
    logo = PhotoImage(file='icons/logo2.png')
    tela_usuario.iconbitmap(default='icons/icon.ico')


    #FRAMES

    TopFrame = Frame(tela_usuario, width = 1000, height =  100,bd= 3,bg= 'black', relief='raise')
    TopFrame.pack(side=TOP)

    FrameLeft = Frame(tela_usuario, width = 195, height = 600, bg= 'white', relief='raise')
    FrameLeft.pack(side=LEFT)
    Logo = Label(FrameLeft, image=logo, bg='white')
    Logo.place(x=0,y=0)

    RightFrame = ttk.Notebook(tela_usuario, width = 800, height = 600)
    RightFrame.pack(side=RIGHT)


     


    #Pagina 1
    page1 = ttk.Frame(RightFrame, width = 800, height = 600)
    RightFrame.add(page1,text='Home           ')

    #-----------------PAGINA 2---------------------
    page2 = Frame(RightFrame, width = 800, height = 600)
    RightFrame.add(page2,text='Clientes           ')
    page2RightFrame = Frame(page2, width = 650, height = 600,bg='#D3D3D3')
    page2RightFrame.pack(side=RIGHT)


    #LISTAR CLIENTE PAGINA 2


    def pesquisa_cliente():
        
        def sair():
            nome_l.place_forget()
            nome_e.place_forget()
            tele_l.place_forget()
            tele_e.place_forget()
            celular_l.place_forget()
            cele_e.place_forget()
            endere_l.place_forget()
            ende_e.place_forget()
            cpf_e.place_forget()
            cpf_l.place_forget()
            estado_e.place_forget()
            estado_l.place_forget()
            cidade_e.place_forget()
            cidade_l.place_forget()
            alter_button.place_forget()
            sair_button.place_forget()

      
           
        def alterar_cliente():

            nome = nome_e.get()
            telefone = tele_e.get()
            celular = cele_e.get()
            endereco = ende_e.get()
            cpf = cpf_e.get()
            estado = estado_e.get()
            cidade = cidade_e.get()
            
            if(nome == "" or telefone == "" or celular == "" or endereco == "" or estado == "" or cidade == ""):
                messagebox.showerror(parent=tela_usuario,title='Informação de Alteração de Cliente', message='Preencha Todos os Campos!')
            else:
                DataBase.cursor.execute("""
                UPDATE Clientes
                SET Nome = ?, Telefone = ?, Celular = ?, Endereco = ?, Cpf = ?, Estado = ?, Cidade = ?
                WHERE Cpf = ? AND Id_Oficina = ?
                """, (nome,telefone,celular,endereco,cpf,estado,cidade,cpf,id_oficina))
                DataBase.conn.commit()
                messagebox.showinfo(parent=tela_usuario,title='Informação de Alteração de Cliente', message='Alteração do cliente realizado com sucesso')
                sair()
            
        
        sql = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
        cliente = pesquisaC_entry.get()
        pesquisaC_entry.delete('0',END)
        status = 0 
        for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
            status = 1 
            
         
        if status == 1: 
            DataBase.cursor.execute(("SELECT Nome, Telefone, Celular, Endereco, Cpf, Cidade, Estado FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?"),(cliente,id_oficina,))
                
            for linha in DataBase.cursor.fetchall():
                a = linha



            
            nome_e = ttk.Entry(page2RightFrame,width=25)
            nome_e.insert(0,a[0])
            nome_e.place(x=110,y=12)
            nome_l = Label(page2RightFrame,text= 'Nome:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            nome_l.place(x=30,y=10)
            
            tele_l = Label(page2RightFrame,text= 'Telefone:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            tele_l.place(x=30,y=50)
            tele_e = ttk.Entry(page2RightFrame,width=25)
            tele_e.insert(0,a[1])
            tele_e.place(x=110,y=52)
            
            celular_l = Label(page2RightFrame,text= 'Celular:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            celular_l.place(x=30,y=90)
            cele_e = ttk.Entry(page2RightFrame,width=25)
            cele_e.insert(0,a[2])
            cele_e.place(x=110,y=92)
            
            endere_l = Label(page2RightFrame,text= 'Endereço:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            endere_l.place(x=30,y=130)
            ende_e = ttk.Entry(page2RightFrame,width=25)
            ende_e.insert(0,a[3])
            ende_e.place(x=110,y=132)
            
            cpf_l = Label(page2RightFrame,text= 'CPF:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            cpf_l.place(x=30,y=170)
            cpf_e = ttk.Entry(page2RightFrame,width=25)
            cpf_e.insert(0,a[4])
            cpf_e['state'] = DISABLED
            cpf_e.place(x=110,y=172)
            
            cidade_l = Label(page2RightFrame,text= 'Cidade:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            cidade_l.place(x=30,y=210)
            cidade_e = ttk.Entry(page2RightFrame,width=25)
            cidade_e.insert(0,a[5])
            cidade_e.place(x=110,y=212)
            
            estado_l = Label(page2RightFrame,text= 'Estado:', font=('Franklin Gothic Medium',13), bg = '#D3D3D3', fg = 'black')
            estado_l.place(x=30,y=250)
            estado_e = ttk.Entry(page2RightFrame,width=25)
            estado_e.insert(0,a[6])
            estado_e.place(x=110,y=252)
            
            alter_button = ttk.Button(page2RightFrame,text='Alterar',width=15,command=alterar_cliente)
            alter_button.place(x=30,y=300)
            sair_button = ttk.Button(page2RightFrame,text='Sair',width=15,command=sair)
            sair_button.place(x=200,y=300)
        else: 
            messagebox.showerror(parent=tela_usuario,title="Informação de Cliente", message="Nenhum Dado Encontrado")

            
               
                
        
      
        
        
        
        
    def delete_cliente():

            sql = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
            cliente = deletaC_entry.get()
            deletaC_entry.delete('0',END)
            status = 0 
            for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
                status = 1 
             
            if status == 1: 
                DataBase.cursor.execute("""DELETE FROM Clientes
                                           WHERE Cpf = ? AND Id_Oficina = ?""",(cliente,id_oficina,))
                DataBase.conn.commit()
                messagebox.showinfo(parent=tela_usuario,title="Informação de Cliente",message="Registro Deletado")
            else: 
                messagebox.showerror(parent=tela_usuario,title="Informação de Cliente", message="Nenhum Dado Encontrado")

            


    pesquisaC_label = Label(page2,text = 'Pesquisar Cliente\nCPF',font=('Franklin Gothic Medium',12)).place(x=1,y=25)
    pesquisaC_entry = ttk.Entry(page2, width = 18)
    pesquisaC_entry.place(x = 5 , y = 70)
    pesquisaC_button = ttk.Button(page2, text='Pesquisar Cliente', width=15,command=pesquisa_cliente).place(x=10,y=100)
           

    """
    deletaC_label = Label(page2,text = 'Deletar Cliente\nCPF',font=('Franklin Gothic Medium',12)).place(x=1,y=175)
    deletaC_entry = ttk.Entry(page2, width = 18)
    deletaC_entry.place(x = 5 , y = 220)
    deletaC_button = ttk.Button(page2, text='Deletar Cliente', width=15,command=delete_cliente).place(x=10,y=250)
    """




    #--------------Pagina 3-------------------------------
    page3 = ttk.Frame(RightFrame, width = 800, height = 600)
    RightFrame.add(page3,text='Ordens           ')
    page3RightFrame = ttk.Frame(page3, width = 400, height = 600)
    page3RightFrame.pack(side=RIGHT)


    #BOTÕES
    def pesquisaO():
        sql = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
        cliente = pesquisaO_entry.get()
        status = 0 
        for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
            status = 1    
        if status == 1: 
            
            cliente = pesquisaO_entry.get()
            tree3.delete(*tree3.get_children())
            sql = ("""SELECT Clientes.Nome, Ordens.ID, Ordens.STATUS, Ordens.VEICULO, Ordens.KM, Ordens.VALOR1, Ordens.VALORTOTAL, Ordens.DATA
                                       FROM Ordens INNER JOIN Clientes
                                       ON Ordens.CPF = Clientes.Cpf
                                       WHERE Ordens.CPF = ? AND Ordens.Id_Oficina = ?""")
            for data in DataBase.cursor.execute(sql,(cliente,id_oficina,)):
                tree3.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
                pesquisaO_entry.delete("0",END)
        else:
            messagebox.showerror(parent=tela_usuario,title="Informação de Ordem",message="Nenhum Dado Encontrado")
        pesquisaO_entry.delete('0',END)
         
    def pesquisaS():
        sql = ('SELECT * FROM Servicos WHERE ID = ? AND Id_Oficina = ?') 
        cliente = int(pesquisaS_entry.get())
        status = 0 
        for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
            status = 1    
        if status == 1: 
            id_servico = int(pesquisaS_entry.get())
            pesquisaS_entry.delete('0',END)
            tela_servicos.tela_servico(id_servico,id_oficina)
        else:
            messagebox.showerror(parent=tela_usuario,title="Informação de Ordem",message="Nenhum Dado Encontrado")
            pesquisaS_entry.delete('0',END)
    def alterarstatus():
        sql = ('SELECT * FROM Servicos WHERE ID = ? AND Id_Oficina = ?') 
        cliente = int(alterastatus_entry.get())
        status = 0 
        for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
            status = 1    
        if status == 1: 
            id_servico = int(alterastatus_entry.get())
            alterastatus_entry.delete('0',END)
            tela_alterastatus.alterar_status(id_servico,id_oficina)
        else:
            messagebox.showerror(parent=tela_usuario,title="Informação de Ordem",message="Nenhum Dado Encontrado")
            alterastatus_entry.delete('0',END)
            
    pesquisaO_label = Label(page3,text = 'Pesquisar Ordens\CPF',font=('Franklin Gothic Medium',12)).place(x=1,y=25)
    pesquisaO_entry = ttk.Entry(page3, width = 18)
    pesquisaO_entry.place(x = 5 , y = 60)
    pesquisaO_button = ttk.Button(page3, text='Pesquisar Ordens', width=15,command=pesquisaO).place(x=10,y=85)

    pesquisaS_label = Label(page3,text = 'Pesquisar Detalhes\ndo Serviço/ID',font=('Franklin Gothic Medium',12)).place(x=1,y=130)
    pesquisaS_entry = ttk.Entry(page3, width = 18)
    pesquisaS_entry.place(x = 5 , y = 180)
    pesquisaS_button = ttk.Button(page3, text='Pesquisar Serviço', width=15,command=pesquisaS).place(x=10,y=210)       

    alterastatus_label = Label(page3,text = 'Alterar Status \ndo Serviço/ID',font=('Franklin Gothic Medium',12)).place(x=5,y=250)
    alterastatus_entry = ttk.Entry(page3, width = 18)
    alterastatus_entry.place(x = 5 , y = 300)
    alterastatus_button = ttk.Button(page3, text='Alterar Status', width=15,command=alterarstatus).place(x=10,y=330)  


    #LISTAR CLIENTE PAGINA 2
    scrollbary3 = Scrollbar(page3RightFrame, orient=VERTICAL)
    scrollbarx3 = Scrollbar(page3RightFrame, orient=HORIZONTAL)
    tree3 = ttk.Treeview(page3RightFrame, columns=("CLIENTE", "ID", "STATUS", "VEICULO", "KM", "VALOR DE MÃO DE OBRA", "VALOR TOTAL","DATA" ), selectmode="extended", height=500, yscrollcommand=scrollbary3.set, xscrollcommand=scrollbarx3.set)
    scrollbary3.config(command=tree3.yview)
    scrollbary3.pack(side=RIGHT, fill=Y)
    scrollbarx3.config(command=tree3.xview)
    scrollbarx3.pack(side=BOTTOM, fill=X)
    tree3.heading('CLIENTE', text="CLIENTE", anchor=W)
    tree3.heading('ID', text="ID", anchor=W)
    tree3.heading('STATUS', text="STATUS", anchor=W)
    tree3.heading('VEICULO', text="VEICULO", anchor=W)
    tree3.heading('KM', text="KM", anchor=W)
    tree3.heading('VALOR DE MÃO DE OBRA', text="VALOR DE MÃO DE OBRA", anchor=W)
    tree3.heading('VALOR TOTAL', text="VALOR TOTAL", anchor=W)
    tree3.heading('DATA', text="DATA", anchor=W)
    tree3.column('#0', stretch=NO, minwidth=0, width=0)
    tree3.column('#1', stretch=NO, minwidth=0, width=90)
    tree3.column('#2', stretch=NO, minwidth=0, width=40)
    tree3.column('#3', stretch=NO, minwidth=0, width=50)
    tree3.column('#4', stretch=NO, minwidth=0, width=60)
    tree3.column('#5', stretch=NO, minwidth=0, width=50)
    tree3.column('#6', stretch=NO, minwidth=0, width=170)
    tree3.column('#7', stretch=NO, minwidth=0, width=80)
    tree3.column('#8', stretch=NO, minwidth=0, width=70)
    tree3.pack()

















    #------------------ PAGINA 4 ---------------------------------
    page4 = ttk.Frame(RightFrame, width = 800, height = 600)
    RightFrame.add(page4,text='Veículos           ')
    page4RightFrame = ttk.Frame(page4, width = 400, height = 600)
    page4RightFrame.pack(side=RIGHT)


    #BOTÕES

    def pesquisa_veiculo():
            sql = ('SELECT * FROM Clientes WHERE Cpf = ? AND Id_Oficina = ?') 
            cliente = pesquisaV_entry.get()
            status = 0 
            for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
                status = 1 
            if status == 1: 
                cliente = pesquisaV_entry.get()
                tree4.delete(*tree4.get_children())
                sql = ("""SELECT Veiculos.Marca, Veiculos.Placa, Clientes.Nome, Veiculos.Cor, Veiculos.Chassi 
                                    FROM Veiculos INNER JOIN Clientes
                                    ON Veiculos.Vincular = Clientes.Cpf
                                    WHERE Veiculos.Vincular = ? AND Veiculos.Id_Oficina = ?""")
                status = 0
                for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
                    status = 1
                if status == 1:
                    for data in DataBase.cursor.execute(sql,(cliente,id_oficina,)):
                        tree4.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))
                        pesquisaV_entry.delete("0",END)
                else:
                    pesquisaV_entry.delete('0',END)
                    messagebox.showerror(parent=tela_usuario,title='Informação de Veículo' ,message="O cliente não possui nenhum veículo so sistema")
            else:
                pesquisaV_entry.delete('0',END)
                messagebox.showerror(parent=tela_usuario,title='Informação de Veículo' ,message="O CPF inserido não foi encontrado no servidor")
            
    def delete_veiculo():
            sql = ('SELECT * FROM Veiculos WHERE Placa = ? AND Id_Oficina = ?') 
            cliente = deletaV_entry.get()
            status = 0 
            for row in DataBase.cursor.execute(sql, (cliente,id_oficina,)):
                status = 1 
            if status == 1: 
                veiculo = deletaV_entry.get()
                DataBase.cursor.execute("""DELETE FROM Veiculos
                                           WHERE Placa = ? AND Id_Oficina = ?""",(veiculo,id_oficina,))
                DataBase.conn.commit()
                deletaV_entry.delete("0",END)
                messagebox.showinfo(parent=tela_usuario,title='Informação de Veículo' ,message="Veículo Deletado")
            else:
                deletaV_entry.delete('0',END)
                messagebox.showerror(parent=tela_usuario,title='Informação de Veículo' ,message="Nenhum Dado Encontrado")

                
    pesquisaV_label = Label(page4,text = 'Buscar CPF', width = 10,font=('Franklin Gothic Medium',12)).place(x=1,y=10)
    pesquisaV_entry = ttk.Entry(page4, width = 30)
    pesquisaV_entry.place(x = 1 , y = 40)
    pesquisaV_button = ttk.Button(page4, text='Pesquisa Cliente', width=15,command=pesquisa_veiculo).place(x=1,y=70)

    deletaV_label = Label(page4,text = 'Deletar Veículo/Placa',font=('Franklin Gothic Medium',12)).place(x=1,y=100)
    deletaV_entry = ttk.Entry(page4, width = 30)
    deletaV_entry.place(x = 1 , y = 130)
    deletaV_button = ttk.Button(page4, text='Deletar Veículo', width=15,command=delete_veiculo).place(x=1,y=160)

    #LISTAR CLIENTE PAGINA 4
    scrollbary4 = Scrollbar(page4RightFrame, orient=VERTICAL)
    scrollbarx4 = Scrollbar(page4RightFrame, orient=HORIZONTAL)
    tree4 = ttk.Treeview(page4RightFrame, columns=("MARCA", "PLACA", "CLIENTE", "COR", "CHASSI"), selectmode="extended", height=500, yscrollcommand=scrollbary4.set, xscrollcommand=scrollbarx4.set)
    scrollbary4.config(command=tree4.yview)
    scrollbary4.pack(side=RIGHT, fill=Y)
    scrollbarx4.config(command=tree4.xview)
    scrollbarx4.pack(side=BOTTOM, fill=X)
    tree4.heading('MARCA', text="MARCA", anchor=W)
    tree4.heading('PLACA', text="PLACA", anchor=W)
    tree4.heading('CLIENTE', text="CLIENTE", anchor=W)
    tree4.heading('COR', text="COR", anchor=W)
    tree4.heading('CHASSI', text="CHASSI", anchor=W)
    tree4.column('#0', stretch=NO, minwidth=0, width=0)
    tree4.column('#1', stretch=NO, minwidth=0, width=120)
    tree4.column('#2', stretch=NO, minwidth=0, width=100)
    tree4.column('#3', stretch=NO, minwidth=0, width=140)
    tree4.column('#4', stretch=NO, minwidth=0, width=100)
    tree4.column('#5', stretch=NO, minwidth=0, width=130)
    tree4.pack()








    #BOTÕES
    
    
    def confg():
        tela_confg.new(id_oficina)
    
    def novocliente():
        tela_novo_cliente.new(id_oficina)

    def novoveiculo():
        tela_novo_veiculo.new(id_oficina)

    def novaordem():
        tela_nova_ordem.new(id_oficina)
    
    def Sair():
        tela_usuario.destroy()
        
        
    
    config= PhotoImage(file='icons/config.png')
    B_config = ttk.Button(TopFrame, image=config, width=20,command=confg).place(x=20,y=10)
    L_config= Label(TopFrame,text= 'Configurações', font=('Franklin Gothic Medium',12), bg = 'black', fg = 'white').place(x=0,y=70)

    novo_cliente= PhotoImage(file='icons/novo_cliente.png')
    B_novo_cliente = ttk.Button(TopFrame,image=novo_cliente,width=20,command=novocliente)
    B_novo_cliente.place(x=137,y=10)
    L_novo_cliente= Label(TopFrame,text= 'Novo Cliente', font=('Franklin Gothic Medium',12), bg = 'black', fg = 'white').place(x=120,y=70)

    nova_ordem= PhotoImage(file='icons/nova_ordem.png')
    B_novo_servico = ttk.Button(TopFrame, image=nova_ordem, width=20,command=novaordem).place(x=245,y=10)
    L_novo_servico= Label(TopFrame,text= 'Nova Ordem', font=('Franklin Gothic Medium',12), bg = 'black', fg = 'white').place(x=230,y=70)

    novo_veiculo= PhotoImage(file='icons/novo_veiculo.png')
    B_novo_servico = ttk.Button(TopFrame, image=novo_veiculo, width=20,command=novoveiculo).place(x=360,y=10)
    L_novo_servico= Label(TopFrame,text= 'Novo Veículo', font=('Franklin Gothic Medium',12), bg = 'black', fg = 'white').place(x=345,y=70)

    """novo_orçamento= PhotoImage(file='icons/novo_orçamento.png')
    B_novo_servico = ttk.Button(TopFrame, image=novo_orçamento, width=20,command=Deletar).place(x=480,y=10)
    L_novo_servico= Label(TopFrame,text= 'Novo Orçamento', font=('Franklin Gothic Medium',12), bg = 'black', fg = 'white').place(x=455,y=70)
    """

    sair= PhotoImage(file='icons/sair.png')
    B_sair = ttk.Button(TopFrame, image=sair, width=20,command=Sair).place(x=920,y=10)
    L_sair= Label(TopFrame,text= 'Sair', font=('Franklin Gothic Medium',12), bg = 'black', fg = 'white').place(x=930,y=70)

    tela_usuario.mainloop()