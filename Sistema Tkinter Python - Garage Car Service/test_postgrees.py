import postgresql
db = postgresql.open(user = 'postgres', database = 'Oficina', port = 5432, password = '1234')
# OR
# db = postgresql.open("pq://user:password@host/name_of_database")

db.execute("CREATE TABLE tb_user (ds_user varchar(20) PRIMARY KEY, ds_passwd text)")

.execute("""
CREATE TABLE IF NOT VEXISTS Oficina(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Endereco TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Cpf TEXT NOT NULL,
    Email TEXT NOT NULL
);
""")