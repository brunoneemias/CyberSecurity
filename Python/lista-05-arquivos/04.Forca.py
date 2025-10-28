# Criado por: [Bruno Neemias Alves Mota]

import random

# Função para adicionar palavras ao arquivo
def adicionar_palavras():
    try:
        qtd = int(input("Quantas palavras deseja adicionar? "))
        with open("palavras.txt", "a", encoding="utf-8") as arquivo:
            for _ in range(qtd):
                palavra = input("Digite uma palavra: ").strip().lower()
                # .strip() remove espaços extras
                # .lower() garante que todas as letras fiquem minúsculas
                arquivo.write(palavra + "\n")
    except ValueError:
        print("Por favor, digite um número válido.")

# Função para carregar palavras do arquivo
def carregar_palavras():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as arquivo:
            palavras = [linha.strip() for linha in arquivo if linha.strip()]
        return palavras
    except FileNotFoundError:
        print("O arquivo 'palavras.txt' não existe.")
        return []

# Função para jogar o jogo da forca
def jogar_forca(palavra):
    letras_descobertas = ["_" for _ in palavra]
    letras_usadas = set()
    tentativas = 6

    print("\nVamos jogar a forca!")
    while tentativas > 0 and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Letras usadas:", ", ".join(sorted(letras_usadas)))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").strip().lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra válida.")
            continue

        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Boa! A letra está na palavra.")
        else:
            tentativas -= 1
            print("Ops! A letra não está na palavra.")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        print("\nFim de jogo! A palavra era:", palavra)

# Executa o programa
adicionar_palavras()
lista_palavras = carregar_palavras()

if lista_palavras:
    palavra_sorteada = random.choice(lista_palavras)
    jogar_forca(palavra_sorteada)