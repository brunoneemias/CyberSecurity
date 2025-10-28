# Criado por: [Bruno Neemias Alves Mota]
import random
# --- Funções dos Exercícios ---

def exercicio1():
    """
    Preenche um vetor com 15 números aleatórios e
    informa se cada número é par ou ímpar.
    """
    vetor = [] # declaração do vetor
    print("Preenchendo o vetor com 15 números aleatórios...")
    for _ in range(15): # usando o underscore para rodar em loop executando o código 15 vezes.
        numero = random.randint(1, 100)  # Gera um número inteiro aleatório entre 1 e 100
        vetor.append(numero) # Adiciona o número ao final do vetor.
    
    print("\n--- Analisando o Vetor ---")
    
    for i, num in enumerate(vetor): # Enumerate percorre a lista e traz o indice(posição) para "i" e o valor para "num"
        if num % 2 == 0:
            print(f"Posição {i+1}: O número {num} é PAR.")
        else:
            print(f"Posição {i+1}: O número {num} é ÍMPAR.")
 
def exercicio2():
    """
    Preenche um vetor com 30 números aleatórios e
    exibe apenas os múltiplos de 6.
    """
   
    vetor = [] # declaração do vetor
    print("Preenchendo o vetor com 30 números aleatórios...")
    for _ in range(30): # usando o underscore para rodar o código em loop 30 vezes.
        numero = random.randint(1, 200) # Gerando números em um range maior que o ex1 para ter mais chances de encontrar múltiplos de 6
        vetor.append(numero) # Adiciona o número ao final do vetor.
        
        print("\n--- Analisando o Vetor em busca de múltiplos de 6 ---")
        
        # Flag para verificar se algum múltiplo foi encontrado
        encontrou_multiplos = False
        
        for i, num in enumerate(vetor):
            if num % 6 == 0:
                print(f"Posição {i+1}: O número {num} é um múltiplo de 6.")
                encontrou_multiplos = True
            
    if not encontrou_multiplos:
        print("Nenhum múltiplo de 6 foi encontrado no vetor.")
        
def exercicio3():
    """
    Preenche um vetor de 10 posições com números aleatórios,
    cria um vetor inverso e exibe ambos.
    """
    vetor_original = [] 
    print("Preenchendo o vetor original com 10 números aleatórios...")
    for _ in range(10):
        numero = random.randint(1, 100)
        vetor_original.append(numero)
    
    # Criando o vetor inverso
    vetor_inverso = vetor_original[::-1] #fatiamento de lista -1 para percorrer a lista de trás para a frente.
    
    print("\n--- Vetores ---")
    print(f"Vetor Original: {vetor_original}")
    print(f"Vetor Inverso: {vetor_inverso}")

def exercicio4():
    """
    Preenche dois vetores de 10 posições, cria um terceiro
    intercalando os dois primeiros e exibe todos.
    """
    # Preenche o vetor 1 com 10 números aleatórios entre 1 e 50
    vetor1 = [random.randint(1, 50) for _ in range(10)]
    # Preenche o vetor 2 com 10 números aleatórios entre 51 e 100
    vetor2 = [random.randint(51, 100) for _ in range(10)]
    
    vetor3 = [] # Inicializa o vetor que receberá a intercalação
    
     # Loop para percorrer os vetores de 0 a 9
    for i in range(10):
        # Adiciona o elemento da posição 'i' do vetor 1
        vetor3.append(vetor1[i])
        # Adiciona o elemento da mesma posição 'i' do vetor 2
        vetor3.append(vetor2[i])
    
    print("\n--- Vetores ---")
    print(f"Vetor 1: {vetor1}")
    print(f"Vetor 2: {vetor2}")
    print(f"Vetor 3 (Intercalado): {vetor3}")

def exercicio5():
    """
    Lê dois vetores, um vetor de operações e gera um quarto vetor
    com os resultados das operações.
    """
    print("Preenchendo os vetores de entrada com números aleatórios...")
    vetor_a = [random.randint(1, 20) for _ in range(5)]
    vetor_b = [random.randint(1, 20) for _ in range(5)]
    
    # Vetor com as operações básicas
    vetor_operacoes = ['+', '-', '*', '/', '*'] # mais de uma operação para ter 5
    
    vetor_resultado = [] #armazena os resultados.
    
    print("\nRealizando as operações...")
    # Loop para percorrer os vetores e aplicar as operações
    for i in range(5):
        num_a = vetor_a[i]
        num_b = vetor_b[i]
        op = vetor_operacoes[i]
        resultado = 0

        if op == '+':
            resultado = num_a + num_b
        elif op == '-':
            resultado = num_a - num_b
        elif op == '*':
            resultado = num_a * num_b
        elif op == '/':
            # Tratamento para evitar divisão por zero
            if num_b != 0: 
                resultado = num_a / num_b
            else:
                resultado = "Erro: Divisão por zero" # Mensagem de erro para divisão por zero
        
        vetor_resultado.append(resultado)
        
    print("\n--- Relatório de Operações ---")
    for i in range(5):
        # Exibe cada operação e seu resultado de forma organizada
        num_a = vetor_a[i]
        num_b = vetor_b[i]
        op = vetor_operacoes[i]
        res = vetor_resultado[i]
        print(f"Operação {i+1}: {num_a} {op} {num_b} = {res}")
        
    print("\n--- Resumo dos Vetores ---")
    print(f"Vetor A: {vetor_a}")
    print(f"Vetor B: {vetor_b}")
    print(f"Vetor de Operações: {vetor_operacoes}")
    print(f"Vetor de Resultados: {vetor_resultado}")

def exercicio6():
    """
    Preenche uma matriz 5x5 com números relativos à sua posição
    e a exibe.
    """
    # A matriz é uma lista de listas
    matriz = []
    
    # Loop externo para percorrer as linhas (de 1 a 5)
    for linha in range(1, 6):
        # Cria uma lista para representar a linha atual da matriz
        linha_atual = []
        # Loop interno para percorrer as colunas (de 1 a 5)
        for coluna in range(1, 6):
            # O valor do elemento é a combinação da linha e da coluna (Ex: 11, 12, etc.)
            valor = linha * 10 + coluna
            linha_atual.append(valor)
        # Adiciona a linha completa à matriz
        matriz.append(linha_atual)

    print("\n--- Matriz 5x5 ---")
    # Loop para exibir a matriz
    for linha in matriz:
        # Usa 'join' para formatar a saída com espaços entre os números
        # O str(num) converte o número para string para que 'join' possa funcionar
        print(" ".join(map(str, linha)))
        
def exercicio7(string_original):
    """
    Recebe uma string e a transforma em maiúsculas.
    """
    string_maiuscula = string_original.upper() # Método upper retorna todas as letras em maiuscula.
    print(f"String Original: {string_original}")
    print(f"String em Maiúsculas: {string_maiuscula}")
    
def exercicio8(string_texto, caractere_busca):
    """
    Recebe uma string e um caractere, e conta a frequência do caractere.
    """
    contador = 0
    # Itera sobre cada letra na string
    for letra in string_texto:
        # Se a letra for igual ao caractere que estamos buscando...
        if letra == caractere_busca:
            contador += 1  # Incrementa o contador

    print(f"A string original é: '{string_texto}'")
    print(f"O caractere a ser buscado é: '{caractere_busca}'")
    print(f"O caractere '{caractere_busca}' aparece {contador} vez(es) na string.")

def exercicio9(string_original, caractere_apagar):
    """
    Recebe uma string e um caractere, e apaga todas as ocorrências
    desse caractere na string.
    """
    string_limpa = string_original.replace(caractere_apagar, "")
    print(f"String Original: '{string_original}'")
    print(f"Caractere a apagar: '{caractere_apagar}'")
    print(f"String Resultante: '{string_limpa}'")
    
def exercicio10(escolha_usuario, numero_usuario):
    """
    Joga par ou ímpar com o usuário e determina o vencedor.
    """
    numero_sistema = random.randint(0, 5)
    soma = numero_usuario + numero_sistema
    resultado_par = soma % 2 == 0
    
    if resultado_par:
        vencedor = 'Sistema' if escolha_usuario == 'I' else 'Usuário'
        par_ou_impar = 'PAR'
    else:
        vencedor = 'Sistema' if escolha_usuario == 'P' else 'Usuário'
        par_ou_impar = 'ÍMPAR'
    
    print("\n--- Resultado do Jogo ---")
    print(f"Você escolheu: {escolha_usuario}")
    print(f"Você jogou: {numero_usuario}")
    print(f"O sistema jogou: {numero_sistema}")
    print(f"A soma dos números é: {soma}")
    print(f"O resultado da soma é {par_ou_impar}.")
    print("-------------------------")
    print(f"O vencedor é o {vencedor}!")
        
def exercicio11(aposta_usuario):
    """
    Simula um dado, gera um número aleatório de 1 a 6 e
    verifica se o usuário acertou.
    """
    # Lançamento do dado
    dado = random.randint(1, 6)
    
    print("\n--- Resultado do Jogo do Dado ---")
    print(f"Seu palpite foi: {aposta_usuario}")
    print(f"O dado foi lançado e o resultado é: {dado}")
    
    # Verifica se o usuário acertou
    if aposta_usuario == dado:
        print("Parabéns! Você acertou o número!")
    else:
        print("Que pena! Não foi desta vez.")
    print("----------------------------------")
    
def exercicio12(ano):
    """
    Verifica se um ano é bissexto de acordo com as regras especificadas.
    """
    # Um ano é bissexto se for divisível por 4, exceto se for divisível por 100,
    # a menos que também seja divisível por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} NÃO é bissexto.")

# --- Menu Principal ---
def menu():
    """
    Exibe o menu principal e gerencia a navegação entre os exercícios.
    """
    while True:
        print("\n--- Menu de Exercícios ---")
        print("1. Exercício 1: Vetor Aleatório (Par/Ímpar)")
        print("2. Exercício 2: Múltiplos de 6")
        print("3. Exercício 3: Vetor Inverso")
        print("4. Exercício 4: Vetores Intercalados")
        print("5. Exercício 5: Vetor de Operações")
        print("6. Exercício 6: Matriz de Posições")
        print("7. Exercício 7: Transformar String em Maiúsculas")
        print("8. Exercício 8: Contar Caractere em String")
        print("9. Exercício 9: Apagar Caractere em String")
        print("10. Exercício 10: Jogo Par ou Ímpar")
        print("11. Exercício 11: Jogo do Dado")
        print("12. Exercício 12: Verificar Ano Bissexto")
        print("0. Sair")
        print("--------------------------")

        opcao = input("Escolha um exercício (digite o número): ")

        if opcao == '1':
            exercicio1()
        elif opcao == '2':
            exercicio2()
        elif opcao == '3':
            exercicio3()
        elif opcao == '4':
            exercicio4()
        elif opcao == '5':
            exercicio5()
        elif opcao == '6':
            exercicio6()
        elif opcao == '7':
            texto = input("Digite uma string para ser transformada: ")
            exercicio7(texto)
        elif opcao == '8':
            texto = input("Digite a string: ")
            caractere = input("Digite o caractere que deseja contar: ")
            exercicio8(texto, caractere[0])
        elif opcao == '9':
            texto = input("Digite a string: ")
            caractere = input("Digite o caractere que deseja apagar: ")
            exercicio9(texto, caractere[0])
        elif opcao == '10':
            escolha = input("Escolha Par ou Ímpar (P/I): ").upper()
            if escolha not in ['P', 'I']:
                print("Escolha inválida. Por favor, digite P ou I.")
                continue
            try:
                numero_usuario = int(input("Digite um número de 0 a 5: "))
                if not (0 <= numero_usuario <= 5):
                    print("Número inválido. Por favor, digite um número entre 0 e 5.")
                    continue
                exercicio10(escolha, numero_usuario)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue
        elif opcao == '11':
            try:
                aposta = int(input("Digite sua aposta (um número de 1 a 6): "))
                if not (1 <= aposta <= 6):
                    print("Aposta inválida. O número deve ser entre 1 e 6.")
                    continue
                exercicio11(aposta)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue
        elif opcao == '12':
            try:
                ano = int(input("Digite um ano para verificar se é bissexto: "))
                exercicio12(ano)
            except ValueError:
                print("Entrada inválida. Por favor, digite um ano válido.")
                continue
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# --- Programa Principal ---
if __name__ == "__main__":
    menu()