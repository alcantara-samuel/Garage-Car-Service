import sqlite3

conn = sqlite3.connect('OFICINA.db')
cursor = conn.cursor()

def DataBase():
	
	cursor.execute("""
CREATE TABLE IF NOT EXISTS OficinaRegistro(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Endereco TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Cpf TEXT NOT NULL,
    Rg TEXT NOT NULL,
    Email TEXT NOT NULL
);

""")