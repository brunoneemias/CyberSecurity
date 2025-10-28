# Criado por: [Bruno Neemias Alves Mota]

# Leitura dos dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Exibição dos valores digitados
print("Você digitou:", valor1, "e", valor2)

# Verificação de igualdade ou diferença
if valor1 == valor2:
    print("Os valores são iguais.")
if valor1 != valor2:
    print("Os valores são diferentes.")
    if valor1 > valor2:
        print("O maior valor é:", valor1)
    if valor2 > valor1:
        print("O maior valor é:", valor2)
