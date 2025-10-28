# Criado por: [Bruno Neemias Alves Mota]

# 1. Cotação do dólar
cotacao = float(input("Digite a cotação atual do dólar em reais (ex: 5.25): "))

# 2. Valor em dólares
valor_dolar = float(input("Digite o valor em dólares a ser convertido (ex: 100): "))

# 3. Converte o valor para Real
valor_reais = valor_dolar * cotacao

 # 4. Mostre o resultado com 2 casas decimais

print(f"\nO valor de ${valor_dolar:.2f} dólares equivale a R$ {valor_reais:.2f} reais.")
