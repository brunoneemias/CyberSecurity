# Criado por: [Bruno Neemias Alves Mota]

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

# Abre o arquivo 'mensagem.txt' em modo de adição ('a') e escreve a frase
with open("mensagem.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(frase + "\n")

# Abre o arquivo em modo de leitura ('r') e exibe o conteúdo
with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("\nConteúdo do arquivo 'mensagem.txt':")
print(conteudo)
