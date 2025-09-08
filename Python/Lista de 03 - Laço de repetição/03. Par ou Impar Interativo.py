# Criado por: [Bruno Neemias Alves Mota]

#Apresentação do título e condição para encerrar o programa
print("=== Par ou Ímpar ===")
print("Digite 0 para encerrar o programa.\n")

#Laço de repetição que continua executando até que seja interrompido manualmente.
while True:
    # Tratamento de erros try except.
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")
        continue

    if numero == 0:
        print("Programa encerrado. Até mais!")
        break

    if numero % 2 == 0:
        print(f"{numero} é PAR.\n")
    else:
        print(f"{numero} é ÍMPAR.\n")
