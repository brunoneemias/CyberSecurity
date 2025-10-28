# Nome: BRUNO NEEMIAS ALVES MOTA

import random  # Importa o módulo para gerar números aleatórios

class Dado:
    
    # Método estático para rolar um dado padrão de 6 lados
    @staticmethod
    def rolar_dado_padrao():
        # Gera um número aleatório entre 1 e 6
        resultado = random.randint(1, 6)
        # Exibe o resultado do lançamento
        print(f"O dado foi rolado e caiu no número: {resultado}")
        return resultado

    # Método estático para fazer uma aposta em um número de 1 a 6
    @staticmethod
    def aposta_dado_padrao(aposta):
        # Rola o dado
        resultado = Dado.rolar_dado_padrao()
        # Verifica se o número apostado foi o sorteado
        if aposta == resultado:
            print(f"Parabéns! Você apostou no número {aposta} e ele foi sorteado!")
            return True
        else:
            print(f"Que pena! Você apostou no número {aposta}, mas o sorteado foi {resultado}.")
            return False

    # Método estático para rolar um dado com número de lados personalizado
    @staticmethod
    def rolar_dado(numero_lados):
        # Gera um número aleatório entre 1 e o número de lados informado
        resultado = random.randint(1, numero_lados)
        # Exibe o resultado do lançamento
        print(f"O dado de {numero_lados} lados foi rolado e caiu no número: {resultado}")
        return resultado

# Exemplos de uso dos métodos estáticos

Dado.rolar_dado_padrao()         # Rola um dado de 6 lados
Dado.aposta_dado_padrao(3)       # Faz uma aposta no número 3 e verifica se foi sorteado
Dado.rolar_dado(20)              # Rola um dado de 20 lados