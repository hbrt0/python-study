import os 
import shutil
from pathlib import Path

# Método para pegar o caminho do arquivo atual de forma dinâmica
ROOTH_PATH = Path(__file__).parent # parent remove o arquivo atual e pega o caminho do diretório

# Abre o arquivo 'teste.txt' no modo de escrita ('w')
file = open(
    ROOTH_PATH / "teste.txt", "w" 
)

# Escreve uma string no arquivo
file.write("Escrevendo dados em um novo arquivo.")

# Escreve múltiplas linhas no arquivo
file.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

# Fecha o arquivo
file.close()