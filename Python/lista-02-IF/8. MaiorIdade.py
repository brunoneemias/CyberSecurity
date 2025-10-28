# Criado por: [Bruno Neemias Alves Mota]

# Leitura da idade
idade = int(input("Digite sua idade: "))

# Exibição da idade digitada
print("Você digitou:", idade, "anos.")

# Verificações
if idade < 18:
    print("Você é menor de idade.")
if idade >= 18:
    print("Você é maior de idade.")
if idade > 65:
    print("Você é maior de 65 anos.")
