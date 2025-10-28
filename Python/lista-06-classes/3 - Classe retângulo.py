# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Retângulo em Python
# Descrição: Calcula área e perímetro de um retângulo
# ============================================================

class Retangulo:
    # Método construtor: define largura e altura do retângulo
    def __init__(self, largura, altura):
        self.largura = largura  # Largura do retângulo
        self.altura = altura    # Altura do retângulo

    # Método para calcular a área do retângulo
    def calcular_area(self):
        area = self.largura * self.altura
        print(f"A área do retângulo é: {area} unidades²")
        return area

    # Método para calcular o perímetro do retângulo
    def calcular_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        print(f"O perímetro do retângulo é: {perimetro} unidades")
        return perimetro

# ============================================================
# Exemplo de uso da classe Retangulo
# ============================================================

# Criando um objeto da classe Retangulo
meu_retangulo = Retangulo(5, 3)

# Chamando os métodos para calcular área e perímetro
meu_retangulo.calcular_area()
meu_retangulo.calcular_perimetro()