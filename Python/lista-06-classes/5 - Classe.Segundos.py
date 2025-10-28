# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Segundos em Python
# Descrição: Converte horas, minutos e segundos em segundos totais
# ============================================================

class Segundos:
    # Método construtor: define os atributos de tempo
    def __init__(self, horas, minutos, segundos):
        self.horas = horas        # Número de horas
        self.minutos = minutos    # Número de minutos
        self.segundos = segundos  # Número de segundos

    # Método para calcular o total de segundos
    def calcular_total_segundos(self):
        total = self.horas * 3600 + self.minutos * 60 + self.segundos
        print(f"Total de segundos: {total}")
        return total

# ============================================================
# Exemplo de uso da classe Segundos
# ============================================================

# Criando um objeto da classe Segundos
tempo = Segundos(1, 49, 3)

# Chamando o método para calcular o total de segundos
tempo.calcular_total_segundos()