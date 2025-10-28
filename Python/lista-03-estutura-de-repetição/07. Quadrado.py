# Criado por: [Bruno Neemias Alves Mota]

#Exibição do título
print("=== Gerador de Quadrado com Asteriscos ===")

# Leitura do tamanho do lado
lado = int(input("Digite o tamanho do lado do quadrado (entre 1 e 20): "))

# Verifica se está dentro do intervalo permitido
if lado < 1 or lado > 20:
    print("Tamanho inválido. Digite um valor entre 1 e 20.")
else:
    print("\nQuadrado gerado:\n")
    for i in range(lado):
        print("* " * lado)
