# Nome: BRUNO NEEMIAS ALVES MOTA

class Produto:
    # Metodo construtor, para criar um novo objeto. Neste caso um produto
    def __init__(self, nome, preco, descricao, estoque):
        # Atributos privados "__"
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
        self.__estoque = estoque

    # Getter para nome
    def get_nome(self):
        return self.__nome

    # Setter para nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        print(f"Nome do produto atualizado para: {novo_nome}")

    # Getter para preço
    def get_preco(self):
        return self.__preco

    # Setter para preço
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
            print(f"Preço atualizado para: R$ {novo_preco:.2f}")
        else:
            print("Erro: O preço não pode ser negativo.")

    # Getter para descrição
    def get_descricao(self):
        return self.__descricao

    # Setter para descrição
    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao
        print("Descrição atualizada.")

    # Getter para estoque
    def get_estoque(self):
        return self.__estoque

    # Setter para estoque
    def set_estoque(self, novo_estoque):
        if novo_estoque >= 0:
            self.__estoque = novo_estoque
            print(f"Estoque atualizado para: {novo_estoque} unidades.")
        else:
            print("Erro: Estoque não pode ser negativo.")

    # Método para aplicar desconto
    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            desconto = self.__preco * (percentual / 100)
            novo_preco = self.__preco - desconto
            print(f"Desconto de {percentual}% aplicado. Novo preço: R$ {novo_preco:.2f}")
            return novo_preco
        else:
            print("Erro: Percentual de desconto inválido.")
            return self.__preco

    # Método para comprar (aumentar estoque)
    def comprar(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            print(f"{quantidade} unidades compradas. Estoque atual: {self.__estoque}")
        else:
            print("Erro: Quantidade inválida para compra.")

    # Método para vender (reduzir estoque)
    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
            total = quantidade * self.__preco
            print(f"{quantidade} unidades vendidas. Total: R$ {total:.2f}. Estoque restante: {self.__estoque}")
        else:
            print("Erro: Estoque insuficiente para realizar a venda.")

    # Método para exibir detalhes do produto
    def exibir_detalhes(self):
        print("📦 Detalhes do Produto:")
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Estoque: {self.__estoque} unidades")

# Exemplo de uso
produto1 = Produto("Fone Bluetooth", 150.00, "Fone sem fio com cancelamento de ruído", 10)

produto1.exibir_detalhes()
produto1.aplicar_desconto(20)
produto1.vender(3)
produto1.comprar(5)
produto1.set_preco(140.00)
produto1.set_descricao("Fone com bateria de longa duração")
produto1.exibir_detalhes()