from tkinter import *

from tkinter import ttk


root = Tk()
# Titulo da janela 2

root.title("Carregando aplicação...")
root["bg"] = "white"

# Tamanho da janela default 2

root.geometry("230x100+500+500")
progressbar = ttk.Progressbar(root,orient=HORIZONTAL, length=200, mode='determinate')
progressbar.place(x=15,y=25)

progressbar.start(50)

def fechar():
    root.destroy()


bt_root_close = Button(root,width=20,text="Fechar", command=fechar)
bt_root_close.pack(side="bottom")

root.mainloop()