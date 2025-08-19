import sqlite3

# 1. Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um cursor
cursor = conn.cursor()

# 3. Criar uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")

# 4. Inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Bob", 25))

# 5. Inserir vários dados de uma vez
usuarios = [("Carol", 22), ("David", 28)]
cursor.executemany("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", usuarios)

# 6. Consultar dados
cursor.execute("SELECT * FROM usuarios")
for row in cursor.fetchall():
    print(row)

# 7. Consultar com filtro
cursor.execute("SELECT nome FROM usuarios WHERE idade > ?", (25,))
print(cursor.fetchall())

# 8. Atualizar dados
cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (35, "Alice"))

# 9. Deletar dados
cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Bob",))

# 10. Usar transações (commit/rollback)
try:
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Eve", 40))
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Erro:", e)

# 11. Fechar cursor