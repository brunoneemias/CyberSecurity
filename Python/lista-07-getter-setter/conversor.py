# Nome: BRUNO NEEMIAS ALVES MOTA

class Conversor:
    
    # Método estático para converter metros em centímetros
    @staticmethod
    def metros_para_centimetros(metros):
        # Multiplica o valor em metros por 100 para obter centímetros
        centimetros = metros * 100
        # Exibe uma mensagem clara com o resultado da conversão
        print(f"{metros} metros equivalem a {centimetros} centímetros.")
        # Retorna o valor convertido
        return centimetros

    # Método estático para converter quilogramas em gramas
    @staticmethod
    def quilogramas_para_gramas(quilogramas):
        # Multiplica o valor em quilogramas por 1000 para obter gramas
        gramas = quilogramas * 1000
        # Exibe uma mensagem clara com o resultado da conversão
        print(f"{quilogramas} quilogramas equivalem a {gramas} gramas.")
        # Retorna o valor convertido
        return gramas

    # Método estático para converter litros em mililitros
    @staticmethod
    def litros_para_mililitros(litros):
        # Multiplica o valor em litros por 1000 para obter mililitros
        mililitros = litros * 1000
        # Exibe uma mensagem clara com o resultado da conversão
        print(f"{litros} litros equivalem a {mililitros} mililitros.")
        # Retorna o valor convertido
        return mililitros

    # Método estático para converter horas em minutos
    @staticmethod
    def horas_para_minutos(horas):
        # Multiplica o valor em horas por 60 para obter minutos
        minutos = horas * 60
        # Exibe uma mensagem clara com o resultado da conversão
        print(f"{horas} horas equivalem a {minutos} minutos.")
        # Retorna o valor convertido
        return minutos

# Exemplos de uso dos métodos estáticos da classe Conversor
# não é necessário criar um objeto da classe, pois os métodos são estáticos

Conversor.metros_para_centimetros(2.5)       # Converte 2.5 metros em centímetros
Conversor.quilogramas_para_gramas(3)         # Converte 3 kg em gramas
Conversor.litros_para_mililitros(1.2)        # Converte 1.2 litros em mililitros
Conversor.horas_para_minutos(1.5)            # Converte 1.5 horas em minutos