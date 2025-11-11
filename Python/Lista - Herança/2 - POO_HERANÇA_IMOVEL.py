# Bruno Neemias Alves Mota

# Classe base Imovel
class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco  # Endereço do imóvel
        self.preco = preco        # Preço base do imóvel

    def imprimeDados(self):
        print(f"Endereço: {self.endereco}")
        print(f"Preço base: R$ {self.preco:.2f}")


# Classe Novo herda de Imovel e adiciona valor adicional
class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)  # Chama o construtor da classe Imovel
        self.adicional = adicional         # Valor adicional para imóveis novos

    def getAdicional(self):
        return self.adicional  # Retorna o valor adicional

    def imprimeAdicional(self):
        print(f"Adicional para imóvel novo: R$ {self.adicional:.2f}")

    def imprimeValorTotal(self):
        valor_total = self.preco + self.adicional
        print(f"Valor total do imóvel novo: R$ {valor_total:.2f}")


# Classe Velho herda de Imovel e aplica desconto
class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)  # Chama o construtor da classe Imovel
        self.desconto = desconto           # Valor de desconto para imóveis velhos

    def getDesconto(self):
        return self.desconto  # Retorna o valor do desconto

    def imprimeDesconto(self):
        print(f"Desconto para imóvel velho: R$ {self.desconto:.2f}")

    def imprimeValorFinal(self):
        valor_final = self.preco - self.desconto
        print(f"Valor final do imóvel velho: R$ {valor_final:.2f}")


# Exemplo de uso
print("=== Imóvel Novo ===")
imovel_novo = Novo("Rua das Flores, 123", 300000.00, 25000.00)
imovel_novo.imprimeDados()
imovel_novo.imprimeAdicional()
imovel_novo.imprimeValorTotal()

print("\n=== Imóvel Velho ===")
imovel_velho = Velho("Av. Central, 456", 280000.00, 30000.00)
imovel_velho.imprimeDados()
imovel_velho.imprimeDesconto()
imovel_velho.imprimeValorFinal()
