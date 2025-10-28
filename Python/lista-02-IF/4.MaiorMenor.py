# Criado por: [Bruno Neemias Alves Mota]

# Leitura dos três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificação do maior número
maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Exibição do resultado
print("Você digitou:", num1, ",", num2, "e", num3)
print("O maior número entre eles é:", maior)
