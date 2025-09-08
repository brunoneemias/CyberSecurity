# Criado por: [Bruno Neemias Alves Mota]

opcao = 0

#Laço de repetição que é interrompido quando pelo número 5
while opcao != 5:
    print("=== MENU DE EXERCÍCIOS ===")
    print("1 - Número vs Número")
    print("2 - Verificador de Maioridade")
    print("3 - Faixa Etária Esportiva")
    print("4 - Classificação de Notas")
    print("5 - Sair")

#Tratamento de erros try except.
    try:
        opcao = int(input("Escolha uma opção (1-5): "))
    except ValueError:
        print("Por favor, digite um número válido.\n")
        continue

    if opcao == 1:
        print("\nExecutando Exercício 1 -  Número vs Número...")
        # Leitura dos dois valores
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        # Exibição dos valores digitados
        print("Você digitou:", valor1, "e", valor2)

        # Verificação de igualdade ou diferença
        if valor1 == valor2:
            print("Os valores são iguais.")
        if valor1 != valor2:
            print("Os valores são diferentes.")
            if valor1 > valor2:
                print("O maior valor é:", valor1)
            if valor2 > valor1:
                print("O maior valor é:", valor2)
        print("\nExercício 1 concluído.\n")

    elif opcao == 2:
        print("\nExecutando Exercício 2 - Verificador de Maioridade...")
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
            print("Você também é maior de 65 anos.")
        print("\nExercício 2 concluído.\n")

    elif opcao == 3:
        print("\nExecutando Exercício 3 - Faixa Etária Esportiva...")
        # Leitura da idade do atleta
        idade = int(input("Digite a idade do atleta: "))

        # Exibição da idade digitada
        print("Idade informada:", idade, "anos.")

        # Verificação da categoria
        if 5 <= idade <= 10:
            print("Categoria: Infantil")
        if 11 <= idade <= 15:
            print("Categoria: Juvenil")
        if 16 <= idade <= 20:
            print("Categoria: Junior")
        if 21 <= idade <= 25:
            print("Categoria: Profissional")
        if idade < 5 or idade > 25:
            print("Fora das faixas de categoria definidas pelo clube.")
        print("\nExercício 3 concluído.\n")

    elif opcao == 4:
        print("\nExecutando Exercício 4 - Classificação de Notas...")
        # Leitura da nota
        nota = int(input("Digite a nota do aluno (0 a 10): "))

        # Exibição da nota digitada
        print("Nota informada:", nota)

        # Verificação do conceito
        if nota < 3:
            print("Conceito: E")
        if 3 <= nota <= 5:
            print("Conceito: D")
        if nota == 6 or nota == 7:
            print("Conceito: C")
        if nota == 8 or nota == 9:
            print("Conceito: B")
        if nota == 10:
            print("Conceito: A")
        if nota < 0 or nota > 10:
            print("Nota inválida. Digite um valor entre 0 e 10.")
        print("\nExercício 4 concluído.\n")

    elif opcao == 5:
        print("Saindo do programa. Até mais!")

    else:
        print("Opção inválida. Tente novamente.\n")
