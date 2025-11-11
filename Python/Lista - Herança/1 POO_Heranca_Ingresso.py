# Bruno Neemias Alves Mota

# classe base 
class Ingresso:
    # Método construtor que recebe o valor do ingresso
    def __init__(self, valor):
        self.valor = valor  # Armazena o valor do ingresso como atributo da instância

    # Método que imprime o valor do ingresso comum
    def imprimeValor(self):
        print(f"Valor do ingresso comum: R$ {self.valor:.2f}")
        # Exibe o valor formatado com duas casas decimais e uma mensagem clara
        

# Definição da classe VIP, que herda da classe Ingresso
class VIP(Ingresso):
    # Método construtor que recebe o valor base e o valor adicional
    def __init__(self, valor, adicional):
        super().__init__(valor)  # Chama o construtor da classe Ingresso para definir o valor base
        self.adicional = adicional  # Armazena o valor adicional como atributo da instância

    # Método que calcula e retorna o valor total do ingresso VIP
    def valorVIP(self):
        valor_total = self.valor + self.adicional  # Soma o valor base com o adicional
        print(f"Valor do ingresso VIP (com adicional): R$ {valor_total:.2f}")
        # Exibe o valor total com uma mensagem explicativa
        return valor_total  # Retorna o valor total para uso posterior, se necessário


# Exemplo de uso das classes

# Cria um ingresso comum com valor de R$ 50,00
ingresso_comum = Ingresso(50.00)
ingresso_comum.imprimeValor()  # Chama o método para imprimir o valor do ingresso comum

# Cria um ingresso VIP com valor base de R$ 50,00 e adicional de R$ 30,00
ingresso_vip = VIP(50.00, 30.00)
ingresso_vip.valorVIP()  # Chama o método para imprimir o valor total do ingresso VIP
