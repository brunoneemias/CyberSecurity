# Criado por: [Bruno Neemias Alves Mota]

#Apresentação do cardápio
#/t usado para tabular
print("********** CARDÁPIO **********")
print("CÓDIGO\tESPECIFICAÇÃO\t\tPREÇO UNITÁRIO")
print("1\t\tCachorro Quente\t\tR$ 20.00")
print("2\t\tX-Salada\t\t\tR$ 25.50")
print("3\t\tX-Bacon\t\t\t\tR$ 35.00")
print("4\t\tTorrada Simples\t\tR$ 12.00")
print("5\t\tRefrigerante\t\tR$ 7.50")
print("0\t\tFinalizar a conta\n")

## Inicializa as variaveis
total = 0
preco = 0
item  = 0

#Laço de repetição que continua executando até que seja interrompido manualmente.
while True:
    # Tratamento de erros try except.
    try:
        codigo = int(input("Digite o código do item (0 para finalizar): "))
    except ValueError:
        print("Código inválido. Digite um número de 0 a 5.\n")
        continue

    if codigo == 0:
        break

    if codigo < 1 or codigo > 5:
        print("Código inexistente. Tente novamente.\n")
        continue

    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro.\n")
        continue

    if codigo == 1:
        preco = 20.00
        item = "Cachorro Quente"
    elif codigo == 2:
        preco = 25.50
        item = "X-Salada"
    elif codigo == 3:
        preco = 35.00
        item = "X-Bacon"
    elif codigo == 4:
        preco = 12.00
        item = "Torrada Simples"
    elif codigo == 5:
        preco = 7.50
        item = "Refrigerante"

    subtotal = preco * quantidade
    total += subtotal
    print(f"{quantidade}x {item} adicionados. Subtotal: R$ {subtotal:.2f}\n")

#Exibição da conta
print(f"Valor total a pagar: R$ {total:.2f}")
print("Obrigado pela preferência!")
