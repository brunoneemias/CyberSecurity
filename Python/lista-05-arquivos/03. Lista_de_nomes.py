# Criado por: [Bruno Neemias Alves Mota]

# Função para adicionar nomes ao arquivo
def adicionar_nomes():
    while True:
        nome = input("Digite um nome: ")

        # Abre o arquivo 'nomes.txt' em modo de adição ('a') e escreve o nome
        with open("nomes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(nome + "\n")

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja adicionar outro nome? (s/n): ").strip().lower()
        # .strip() remove espaços extras antes/depois da resposta
        # .lower() transforma a resposta em minúsculas para facilitar a comparação
        if continuar != 's':
            break


# Função para ler e exibir os nomes em ordem alfabética
def exibir_nomes_ordenados():
    try:
        # Abre o arquivo para leitura
        with open("nomes.txt", "r", encoding="utf-8") as arquivo:
            nomes = arquivo.readlines()

        # Remove quebras de linha e espaços extras de cada nome
        nomes = [nome.strip() for nome in nomes if nome.strip()]

        # Ordena os nomes em ordem alfabética
        nomes.sort()

        # Exibe os nomes
        print("\nNomes em ordem alfabética:")
        for nome in nomes:
            print(nome)
    except FileNotFoundError:
        print("O arquivo 'nomes.txt' ainda não existe.")


# Executa o programa
adicionar_nomes()
exibir_nomes_ordenados()
