import sqlite3
from pathlib import Path 

# rootpath for the database file
# This assumes the script is located in the same directory as the database file
ROOT_PATH = Path(__file__).parent

# Connect to the SQLite database
# If the database file does not exist, it will be created
conexao = sqlite3.connect(ROOT_PATH / "data_base.db")

# Create a cursor object using the connection
# The cursor is used to execute SQL commands
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row  # This allows us to access columns by name

def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), status VARCHAR(150))"
    )
criar_tabela(cursor)

def limpar_tabela(cursor, conexao):
    # Clear the table
    cursor.execute("DELETE FROM clientes;")
    conexao.commit()
    # Reset the auto-incrementing id
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='clientes';")
    conexao.commit()
limpar_tabela(cursor, conexao)

def inserir(cursor, conexao, *args):
    # Permite inserir um único cliente (nome, status) ou vários clientes [(nome, status), ...]
    if len(args) == 1 and isinstance(args[0], list):
        # Lista de tuplas [(nome, status), ...]
        cursor.executemany("INSERT INTO clientes (nome, status) VALUES (?, ?);", args[0])
    else:
        # Inserção única
        cursor.execute("INSERT INTO clientes (nome, status) VALUES (?, ?);", args)
    conexao.commit()
data = ('Heloisa','gatinha')
inserir(cursor, conexao, [data])
inserir(cursor, conexao, [data])

data2 = ('Artorias','the Abysswalker')
data3 = ('Gwyn', 'Lord of Cinder')

inserir(cursor, conexao, [data2, data3])

def update_status(cursor, conexao, novo_status, id):
    cursor.execute("UPDATE clientes SET status=? WHERE id=?;", (novo_status, id))
    conexao.commit()
update_status(cursor, conexao, "Gatinha", 1)

def remove(cursor, conexao, id):
    #delete
    cursor.execute("DELETE FROM clientes WHERE id=?;", (id,))
    #isnt ideal update the ids of the remaining records
    #update the ids of the remaining records
    cursor.execute("UPDATE clientes SET id = id - 1 WHERE id > ?;", (id,))
    #update the auto-increment sequence
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='clientes';")
    resultado = cursor.fetchone()
    if resultado:
        cursor.execute("UPDATE sqlite_sequence SET seq = seq - 1 WHERE name='clientes';")
    conexao.commit()
remove(cursor, conexao, 2)

def listar(cursor):
    cursor.execute("SELECT * FROM clientes;")
    return cursor.fetchall()
clientes = listar(cursor)
for cliente in clientes:
    print(dict(cliente))


# def criar_tabela(conexao, cursor):
#     cursor.execute(
#         "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
#     )
#     conexao.commit()


# def inserir_registro(conexao, cursor, nome, email):
#     data = (nome, email)
#     cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
#     conexao.commit()


# def atualizar_registro(conexao, cursor, nome, email, id):
#     data = (nome, email, id)
#     cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
#     conexao.commit()


# def excluir_registro(conexao, cursor, id):
#     data = (id,)
#     cursor.execute("DELETE FROM clientes WHERE id=?;", data)
#     conexao.commit()


# def inserir_muitos(conexao, cursor, dados):
#     cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
#     conexao.commit()


# def recuperar_cliente(cursor, id):
#     cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
#     return cursor.fetchone()


# def listar(cursor):
#     return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# clientes = listar(cursor)
# for cliente in clientes:
#     print(dict(cliente))

# cliente = recuperar_cliente(cursor, 2)
# print(dict(cliente))
# print(cliente["id"], cliente["nome"], cliente["email"])
# print(f'Seja bem vindo ao sistema {cliente["nome"]}')

# # dados = [
# #     ("Guilherme", "guilherme@gmail.com"),
# #     ("Chappie", "chappie@gmail.com"),
# #     ("Melaine", "melaine@gmail.com"),
# # ]
# # inserir_muitos(conexao, cursor, dados)
