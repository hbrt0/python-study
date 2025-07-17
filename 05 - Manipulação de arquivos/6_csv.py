import csv
from pathlib import Path

# Define o caminho raiz como o diretório onde o script está localizado
ROOT_PATH = Path(__file__).parent

# Define constantes para os índices das colunas
COLUNA_ID = 0
COLUNA_NOME = 1

# Tenta abrir (ou criar) o arquivo "usuarios.csv" para escrita
try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        # Escreve o cabeçalho no arquivo CSV
        escritor.writerow(["id", "nome"])
        # Escreve algumas linhas de exemplo no arquivo CSV
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
# Captura e imprime qualquer erro de I/O que ocorra durante a escrita do arquivo
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

# Tenta abrir o arquivo "usuarios.csv" para leitura
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        # Itera sobre as linhas do arquivo CSV
        for idx, row in enumerate(leitor):
            # Pula a primeira linha (cabeçalho)
            if idx == 0:
                continue
            # Imprime o ID e o Nome de cada linha
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}\n")
# Captura e imprime qualquer erro de I/O que ocorra durante a leitura do arquivo
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

# EFICIENTE
# Tenta abrir o arquivo "usuarios.csv" para leitura usando DictReader
try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        # Itera sobre as linhas do arquivo CSV como dicionários
        for row in reader:
            # Imprime o ID e o Nome de cada linha
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}\n")
# Captura e imprime qualquer erro de I/O que ocorra durante a leitura do arquivo
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
