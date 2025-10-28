# Criado por: [Bruno Neemias Alves Mota]

# Lê o conteúdo do arquivo 'mensagem.txt'
with open("mensagem.txt", "r", encoding="utf-8") as origem:
    conteudo = origem.read()

# Escreve o conteúdo no arquivo 'copia.txt'
with open("copia.txt", "w", encoding="utf-8") as destino:
    destino.write(conteudo)

# Lê e exibe o conteúdo do arquivo 'copia.txt'
with open("copia.txt", "r", encoding="utf-8") as copia:
    conteudo_copia = copia.read()

print("Conteúdo do arquivo 'copia.txt':")
print(conteudo_copia)
