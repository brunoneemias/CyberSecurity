# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Carro em Python
# Descrição: Simulação de ações de um carro usando POO
# ============================================================

class Carro:
    # Método construtor: define os atributos iniciais do carro
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo      # Modelo do carro
        self.ano = ano            # Ano de fabricação
        self.cor = cor            # Cor do carro
        self.ligado = False       # Estado inicial: desligado
        self.velocidade = 0       # Velocidade inicial: 0 km/h

    # Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} está ligado.")
        else:
            print(f"O carro {self.modelo} já está ligado.")

    # Método para desligar o carro
    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # Ao desligar, zera a velocidade
            print(f"O carro {self.modelo} foi desligado.")
        else:
            print(f"O carro {self.modelo} já está desligado.")

    # Método para acelerar o carro
    def acelerar(self):
        if self.ligado:
            self.velocidade += 10  # Aumenta a velocidade em 10 km/h
            print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")
        else:
            print("Não é possível acelerar. O carro está desligado.")

    # Método para frear o carro
    def frear(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10  # Reduz a velocidade em 10 km/h
            print(f"O carro {self.modelo} reduziu para {self.velocidade} km/h.")
        elif self.ligado:
            print("O carro já está parado.")
        else:
            print("Não é possível frear. O carro está desligado.")

# ============================================================
# Exemplo de uso da classe Carro
# ============================================================

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota Corolla", 2020, "Prata")

# Chamando os métodos para simular ações
meu_carro.ligar()
meu_carro.acelerar()
meu_carro.frear()
meu_carro.desligar()