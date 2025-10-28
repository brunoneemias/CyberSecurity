# Criado por: [Bruno Neemias Alves Mota]

# 1. Leitura das notas e declaração dos pesos 
n1 = float(input("Digite a nota da P1: "))
n2 = float(input("Digite a nota do trabalho 1: "))
n3 = float(input("Digite a nota da P2: "))
n4 = float(input("Digite a nota do trabalho 2: "))
peso_p1 = 2
peso_trabalho1 = 3
peso_p2 = 4
peso_trabalho2 = 1

#2. Calcula a média ponderada
Media = ((n1 * peso_p1) + (n2 * peso_trabalho1) +  (n3 * peso_p2) + (n4 * peso_trabalho2)) / (peso_p1 + peso_trabalho1 + peso_p2 + peso_trabalho2)

#3. Confere valor da média e mostra o resultado
if Media >= 7: 
    print(f"A média do aluno é: {Media:.2f} e ele foi APROVADO!")
elif 5 <= Media <= 7:
    EX = float(input("Digite a nota do Exame: "))
    NovaMedia = (Media + EX) / 2
    if NovaMedia >= 7:
        print(f"A média do aluno é: {NovaMedia:.2f} e ele foi APROVADO!")
    else:
        print(f"A média do aluno é: {NovaMedia:.2f} e ele foi REPROVADO!")
elif Media < 5:
    print(f"A média do aluno é: {Media:.2f} e ele foi REPROVADO!")
    