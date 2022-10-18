from tkinter import ttk
from tkinter import *
import DataBase
from tkinter import messagebox

def alterar_status(id_servico,id_oficina):
    def salvar():
        status_e = combo_status.get()
        DataBase.cursor.execute("""
                UPDATE Ordens
                SET STATUS = ?
                WHERE ID = ? AND Id_Oficina = ?
                """, (status_e,id_servico,id_oficina))
        DataBase.conn.commit()
        status.destroy()
        messagebox.showinfo(title='Informação de Alteração de Status', message='Alteração realizado com sucesso')
                
    status = Tk()
    status.title('Oficina')
    status.geometry('200x100+100+50')
    status['background'] =  '#F8F8FF'
    status.resizable(width = False, height = False)
    

    itens = ["Em Andamento","Concluido","Aprovado","Fechado"]
    combo_status = ttk.Combobox(status)
    combo_status["values"] = itens
    combo_status.current(0)
    combo_status.bind("<<ComboboxSelected>>")
    combo_status.place(x=30, y=30)

    salvar_button = ttk.Button(status,text = 'Salvar', width=22,command=salvar)
    salvar_button.place(x=30,y=60)
                
                
    status.mainloop()
