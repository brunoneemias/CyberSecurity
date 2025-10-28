# Criado por: [Bruno Neemias Alves Mota]

# 1. Leitura das notas trabalho, prova e declaração do peso para ambas.
nota_trabalho = float(input("Digite a nota do trabalho: "))
nota_prova = float(input("Digite a nota da prova: "))
peso_trabalho = 4
peso_prova = 6

# Calcula a média
Media = ((nota_trabalho * peso_trabalho) + (nota_prova * peso_prova)) / (peso_trabalho + peso_prova)

# Resultado
print(f"A média do aluno é: {Media:.2f}")
