from datetime import datetime

# Obtém a data e hora atual
data_hora_atual = datetime.now()

# Define uma string de data e hora
data_hora_str = "2023-10-20 10:20"

# Define um formato de máscara para a data e hora no padrão brasileiro
mascara_ptbr = "%d/%m/%Y %a"

# Define um formato de máscara para a data e hora no padrão internacional
mascara_en = "%Y-%m-%d %H:%M"

# Formata a data e hora atual usando a máscara brasileira e imprime
print(data_hora_atual.strftime(mascara_ptbr))

# Converte a string de data e hora para um objeto datetime usando a máscara internacional
data_convertida = datetime.strptime(data_hora_str, mascara_en)

# Imprime o objeto datetime convertido
print(data_convertida)

# Imprime o tipo do objeto datetime convertido
print(type(data_convertida))
