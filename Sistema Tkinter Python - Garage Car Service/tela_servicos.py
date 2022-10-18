from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import DataBase
      

def tela_servico(id_servico,id_oficina):        
    servico = Tk()
    servico.title('Oficina')
    servico.geometry('630x500+100+50')
    servico['background'] =  '#F8F8FF'
    servico.resizable(width = False, height = False)
    #Frame 1
    Frame1 = Frame(servico, width = 700, height = 60, bg= '#4682B4', relief='raise')
    Frame1.pack(side=TOP)
    servico.iconbitmap(default='icons/icon.ico')
    titulo = Label(servico,text = 'DETALHES DO SERVIÇO', font=('Franklin Gothic Medium',20),bg= '#4682B4', fg = 'white').place(x=80,y=10)

    #LISTAR SERVIÇOS
    scrollbaryS = Scrollbar(servico, orient=VERTICAL)
    scrollbarxS = Scrollbar(servico, orient=HORIZONTAL)
    treeS = ttk.Treeview(servico, columns=("DESCRIÇÃO", "CPF", "QUANTIDADE", "VALOR", "ID" ), selectmode="extended", height=500, yscrollcommand=scrollbaryS.set, xscrollcommand=scrollbarxS.set)
    scrollbaryS.config(command=treeS.yview)
    scrollbaryS.pack(side=RIGHT, fill=Y)
    scrollbarxS.config(command=treeS.xview)
    scrollbarxS.pack(side=BOTTOM, fill=X)
    treeS.heading('DESCRIÇÃO', text="DESCRIÇÃO", anchor=W)
    treeS.heading('CPF', text="CPF", anchor=W)
    treeS.heading('QUANTIDADE', text="QUANTIDADE", anchor=W)
    treeS.heading('VALOR', text="VALOR", anchor=W)
    treeS.heading('ID', text="ID", anchor=W)
    treeS.column('#0', stretch=NO, minwidth=0, width=0)
    treeS.column('#1', stretch=NO, minwidth=0, width=250)
    treeS.column('#2', stretch=NO, minwidth=0, width=70)
    treeS.column('#3', stretch=NO, minwidth=0, width=70)
    treeS.column('#4', stretch=NO, minwidth=0, width=70)
    treeS.column('#5', stretch=NO, minwidth=0, width=70)
    treeS.pack()


    treeS.delete(*treeS.get_children())
    sql = ("""SELECT DESCRICAO, CPF, QUANTIDADE, VALOR2, ID FROM Servicos WHERE ID = ? AND Id_Oficina = ?""")
    for data in DataBase.cursor.execute(sql,(id_servico,id_oficina)):
        treeS.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))
    servico.mainloop()
