# Criado por: [Bruno Neemias Alves Mota]

# Leitura da idade do atleta
idade = int(input("Digite a idade do atleta: "))

# Exibição da idade digitada
print("Idade informada:", idade, "anos.")

# Verificação da categoria
if idade >= 5 and idade <= 10:
    print("Categoria: Infantil")
if idade >= 11 and idade <= 15:
    print("Categoria: Juvenil")
if idade >= 16 and idade <= 20:
    print("Categoria: Junior")
if idade >= 21 and idade <= 25:
    print("Categoria: Profissional")
if idade < 5 or idade > 25:
    print("Fora das faixas de categoria definidas pelo clube.")
    
