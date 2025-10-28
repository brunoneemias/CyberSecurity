# Criado por: [Bruno Neemias Alves Mota]

print("(-) Calculadora de Divisão Inteira (+)")

# Solicita ao usuário o dividendo
dividendo = int(input("Digite o dividendo (número a ser dividido): "))

# Solicita ao usuário o divisor
divisor = int(input("Digite o divisor: "))

# Calcula o quociente
quociente = dividendo // divisor

# Calcula o resto da divisão
resto = dividendo % divisor

# Resultado
print(f"\nQuociente: {quociente}")
print(f"Resto: {resto}")