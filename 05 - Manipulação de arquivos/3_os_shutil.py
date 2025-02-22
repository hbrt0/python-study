import os
import shutil
from pathlib import Path

# Define the root path as the parent directory of the current file
ROOT_PATH = Path(__file__).parent

# Create a new directory named "novo-diretorio"
os.mkdir(ROOT_PATH / "novo-diretorio")

# Create a new file named "novo.txt" and then close it
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Rename the file "novo.txt" to "alterado.txt"
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") 

# Remove the file "alterado.txt"
os.remove(ROOT_PATH / "alterado.txt")

# Move the file "novo.txt" to the directory "novo-diretorio"
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

# Remove the directory "novo-diretorio" and all its contents
shutil.rmtree(ROOT_PATH / "novo-diretorio")