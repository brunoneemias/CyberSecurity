# Criado por: [Bruno Neemias Alves Mota]

#Exibição do título
print("=== Calculadora de Média ===")

# Solicita a quantidade de números
quantidade = int(input("Quantos números você deseja inserir? "))

# Inicializa a soma
soma = 0

# Loop para ler os números e somá-los
for i in range(1, quantidade + 1):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

# Calcula a média
media = soma / quantidade

# Exibe o resultado
print(f"\nA média dos {quantidade} números é: {media:.2f}")
