# Nome: BRUNO NEEMIAS ALVES MOTA

class TransportePublico:
    # Metodo construtor, para criar um novo objeto. Neste caso um trem
    def __init__(self, capacidade, horario_partida, tarifa):
        # Atributos privados
        self.__capacidade = capacidade
        self.__horario_partida = horario_partida
        self.__tarifa = tarifa
        self.__passageiros = 0
        self.__total_tarifas = 0.0

    #Getter e Setter Acessa e modifica atributos privados.
    # Getter para capacidade, mostra o valor. 
    def get_capacidade(self):
        return self.__capacidade

    # Setter para capacidade, atualiza o valor da capacidade.
    def set_capacidade(self, nova_capacidade):
        if nova_capacidade >= self.__passageiros:
            self.__capacidade = nova_capacidade
            print(f"Capacidade atualizada para {nova_capacidade} passageiros.")
        else:
            print("Erro: A nova capacidade não pode ser menor que o número atual de passageiros.")

    # Getter para horário de partida
    def get_horario_partida(self):
        return self.__horario_partida

    # Setter para horário de partida
    def set_horario_partida(self, novo_horario):
        self.__horario_partida = novo_horario
        print(f"Horário de partida atualizado para {novo_horario}.")

    # Getter para tarifa
    def get_tarifa(self):
        return self.__tarifa

    # Setter para tarifa
    def set_tarifa(self, nova_tarifa):
        if nova_tarifa >= 0:
            self.__tarifa = nova_tarifa
            print(f"Tarifa atualizada para R$ {nova_tarifa:.2f}.")
        else:
            print("Erro: A tarifa não pode ser negativa.")

    # Métodos de simulação 
    # Método para embarcar passageiros
    # Adiciona passageiros, se houver espaço
    def embarcar(self, quantidade):
        if self.__passageiros + quantidade <= self.__capacidade:
            self.__passageiros += quantidade
            self.__total_tarifas += quantidade * self.__tarifa
            print(f"{quantidade} passageiros embarcaram. Total atual: {self.__passageiros}")
        else:
            print("Erro: Capacidade excedida! Não é possível embarcar todos os passageiros.")

    # Método para desembarcar passageiros
    # Remove passageiros, se houver passageiros suficientes
    def desembarcar(self, quantidade):
        if quantidade <= self.__passageiros:
            self.__passageiros -= quantidade
            print(f"{quantidade} passageiros desembarcaram. Total atual: {self.__passageiros}")
        else:
            print("Erro: Não há passageiros suficientes para desembarcar.")

    # Método para simular movimentação
    # Simula a partida do transporte
    def mover(self):
        print(f"O transporte partiu às {self.__horario_partida} com {self.__passageiros} passageiros.")

    # Método para mostrar relatório de tarifas
    # Mostra quanto foi arrecadado em tarifas no dia
    def relatorio_tarifas(self):
        print(f"Total arrecadado em tarifas hoje: R$ {self.__total_tarifas:.2f}")

# Exemplo de uso
metro = TransportePublico(capacidade=100, horario_partida="08:00", tarifa=4.50)

metro.embarcar(30)
metro.mover()
metro.desembarcar(10)
metro.embarcar(50)
metro.embarcar(30)  # Deve mostrar erro por exceder a capacidade
metro.desembarcar(20)
metro.set_tarifa(5.00)
metro.embarcar(10)
metro.relatorio_tarifas()