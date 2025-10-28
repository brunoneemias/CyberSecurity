# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Jogo em Python
# Descrição: Simula uma partida de par ou ímpar entre usuário e sistema
# ============================================================

import random  # Biblioteca para gerar número aleatório

class Jogo:
    # Método construtor: recebe a escolha do usuário (P ou I) e o número de 0 a 5
    def __init__(self, escolha_usuario, numero_usuario):
        self.escolha_usuario = escolha_usuario.upper()  # Converte para maiúsculo
        self.numero_usuario = numero_usuario
        self.numero_sistema = random.randint(0, 5)  # Sistema escolhe aleatoriamente

    # Método para jogar e mostrar o resultado
    def jogar(self):
        soma = self.numero_usuario + self.numero_sistema
        resultado = "P" if soma % 2 == 0 else "I"

        print(f"Você escolheu: {self.escolha_usuario} e jogou {self.numero_usuario}")
        print(f"Sistema jogou: {self.numero_sistema}")
        print(f"Soma: {soma} → {'Par' if resultado == 'P' else 'Ímpar'}")

        if self.escolha_usuario == resultado:
            print("Você venceu!")
        else:
            print("O sistema venceu!")

# ============================================================
# Exemplo de uso da classe Jogo
# ============================================================
# Criando um objeto da classe Jogo
partida = Jogo("P", 3)

# Executando o jogo
partida.jogar()