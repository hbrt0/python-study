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

#CREATE a table if it does not exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), status VARCHAR(150))"
)

#INSERT a record into the table
cursor.execute("INSERT INTO clientes (nome, status) VALUES (?,?);", ("Heloisa", "gatinha"))

# Commit the changes to the database
conexao.commit()

#update a record in the table
cursor.execute("UPDATE clientes SET status=? WHERE id=?;", ("Gatinha", 1))
conexao.commit()

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


# def listar_clientes(cursor):
#     return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# clientes = listar_clientes(cursor)
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
