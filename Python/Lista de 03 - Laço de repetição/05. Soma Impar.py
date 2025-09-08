# Criado por: [Bruno Neemias Alves Mota]

#Exibição do título
print("=== Soma dos Números Ímpares entre X e Y ===")

# Leitura dos valores x e y
x: int = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Condição para fazer a troca de valores caso x maior e y o menor
if x > y:
   x, y = y, x

# Inicializa a soma
soma = 0

# Loop para somar os ímpares entre x e y excluindo x e y
for i in range(x + 1, y):
    if i % 2 != 0:
        soma += i

# Exibe o resultado
print(f"A soma dos números ímpares entre {x} e {y} é: {soma}")
