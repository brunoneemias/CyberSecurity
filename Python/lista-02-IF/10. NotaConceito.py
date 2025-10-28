# Criado por: [Bruno Neemias Alves Mota]

# Leitura da nota
nota = int(input("Digite a nota do aluno (0 a 10): "))

# Exibição da nota digitada
print("Nota informada:", nota)

# Verificação do conceito
if nota < 3:
    print("Conceito: E")
if nota >= 3 and nota <= 5:
    print("Conceito: D")
if nota == 6 or nota == 7:
    print("Conceito: C")
if nota == 8 or nota == 9:
    print("Conceito: B")
if nota == 10:
    print("Conceito: A")
if nota < 0 or nota > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
