# Criado por: [Bruno Neemias Alves Mota]

print("---> Conversor de Segundos para Horas, Minutos e Segundos <---")
total_segundos = int(input("Digite o número de segundos: "))

# Calculo de horas usando a divisão inteira
# 1 hora = 3600 segundos
horas = total_segundos // 3600

# Calculo dos segundos restantes usando o resto da divisão
segundos_restantes = total_segundos % 3600

# Calculo de minutos a partir dos segundos restantes
minutos = segundos_restantes // 60

# Calculo dos segundos  restantes
segundos = segundos_restantes % 60

# Exibe o resultado
print(f"\n{total_segundos} segundos correspondem a:")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")