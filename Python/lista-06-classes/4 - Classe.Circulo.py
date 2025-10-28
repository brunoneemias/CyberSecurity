# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Círculo em Python
# Descrição: Calcula área e circunferência de um círculo
# ============================================================

import math  # Importa a biblioteca para usar o valor de pi

class Circulo:
    # Método construtor: define o raio do círculo
    def __init__(self, raio):
        if raio < 0:
            raise ValueError("O raio não pode ser negativo.")  # Validação
        self.raio = raio

    # Método para calcular a área do círculo
    def calcular_area(self):
        area = math.pi * (self.raio ** 2)
        print(f"A área do círculo é: {area:.2f} unidades²")
        return area

    # Método para calcular a circunferência do círculo
    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"A circunferência do círculo é: {circunferencia:.2f} unidades")
        return circunferencia

# ============================================================
# Exemplo de uso da classe Circulo
# ============================================================

# Criando um objeto da classe Circulo
meu_circulo = Circulo(4)

# Chamando os métodos para calcular área e circunferência
meu_circulo.calcular_area()
meu_circulo.calcular_circunferencia()