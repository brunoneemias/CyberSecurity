# Criado por: [Bruno Neemias Alves Mota]

#Exibição do título
print("=== Analisador de Números ===")
print("Digite números inteiros. Digite 0 para encerrar.\n")

# Inicializa variáveis e atribui none, ausencia de valor para maior e menor
soma = 0
quantidade = 0

maior = None
menor = None

#Laço de repetição que continua executando até que seja interrompido manualmente.
while True:
    # Tratamento de erros try except.
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")
        continue

    if numero == 0:
        break
    # Adiciona o valor atual à soma total e incrementa o contador de números lidos
    soma += numero
    quantidade += 1

    #Se ainda não há valor definido ou se o número atual é maior/menor, atualiza as variáveis
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

# Exibe os resultados
if quantidade == 0:
    print("\nNenhum número foi digitado.")
else:
    media = soma / quantidade
    print(f"\nMaior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média dos números: {media:.2f}")
