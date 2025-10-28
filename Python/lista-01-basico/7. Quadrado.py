# Criado por: [Bruno Neemias Alves Mota]

print("--- Calculadora de Quadrado ---")

# Solicita o lado do quadrado ao usuário e converte para um número decimal
lado = float(input("Digite o lado do quadrado: "))

# Calcula o perímetro
perimetro = lado * 4

# Calcula a área
area = lado ** 2

# Calcula a diagonal
diagonal = lado * (2 ** 0.5)

# Exibe resultados, formatando para duas casas decimais
print(f"\nPerímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")
print(f"Diagonal (hipotenusa): {diagonal:.2f}")