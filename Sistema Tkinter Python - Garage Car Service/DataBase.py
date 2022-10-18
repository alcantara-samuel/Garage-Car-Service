import sqlite3

conn = sqlite3.connect('OficinaData.db') 

cursor = conn.cursor() 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Oficina(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Endereco TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Cpf TEXT NOT NULL,
    Email TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes(
    Nome TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Celular TEXT NOT NULL,
    Endereco TEXT NOT NULL,
    Cpf TEXT NOT NULL PRIMARY KEY,
    Cidade TEXT NOT NULL,
    Estado TEXT NOT NULL,
    Id_Oficina INTEGER NOT NULL,  
    FOREIGN KEY (Id_Oficina) REFERENCES Oficina(Id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Veiculos(
    Marca	TEXT NOT NULL,
	Placa	TEXT NOT NULL,
    Vincular INTEGER,
	Cor	    TEXT NOT NULL,
	Chassi	TEXT NOT NULL,
    Id_Oficina INTEGER NOT NULL,  
    
    FOREIGN KEY (Id_Oficina) REFERENCES Oficina(Id),
    FOREIGN KEY(Vincular) REFERENCES Clientes(Cpf)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Ordens(
    ID          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    CPF         TEXT NOT NULL,
    STATUS      TEXT NOT NULL,
    VEICULO     TEXT NOT NULL,
    KM          INTEGER NOT NULL,
    VALOR1      INTEGER NOT NULL,
    DATA        DATE NOT NULL,
    VALORTOTAL  INTEGER,
    Id_Oficina INTEGER NOT NULL,  
    
    FOREIGN KEY (Id_Oficina) REFERENCES Oficina(Id),
    FOREIGN KEY (VEICULO) REFERENCES Veiculos(Placa),
    FOREIGN KEY (CPF) REFERENCES Clientes(Cpf)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Servicos(
    DESCRICAO TEXT NOT NULL,
    CPF TEXT NOT NULL,
    QUANTIDADE INTEGER NOT NULL,
    VALOR2 INTEGER NOT NULL,
    ID INTEGER NOT NULL,
    Id_Oficina INTEGER NOT NULL, 

    FOREIGN KEY (Id_Oficina) REFERENCES Oficina(Id),
    FOREIGN KEY(CPF) REFERENCES Cliente(Cpf),
    FOREIGN KEY (ID) REFERENCES Ordens(ID)
);
""")

print('Conectado')
