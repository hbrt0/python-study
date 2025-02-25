from pathlib import Path

# Define o caminho raiz como o diretório onde o script está localizado
ROOT_PATH = Path(__file__).parent

# Tenta abrir e ler o arquivo "1lorem.txt"
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
# Captura e imprime qualquer erro de I/O que possa ocorrer
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

# Código comentado que escreve uma string em um arquivo "arquivo-utf-8.txt"
# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

# Tenta abrir e ler o arquivo "arquivo-utf-8.txt" com codificação UTF-8
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
# Captura e imprime qualquer erro de I/O que possa ocorrer
except IOError as exc:  # IOError serve para erros gerais de I/O
    print(f"Erro ao abrir o arquivo {exc}")
# Captura e imprime erros específicos de decodificação Unicode
except UnicodeDecodeError as exc:
    print(exc)
