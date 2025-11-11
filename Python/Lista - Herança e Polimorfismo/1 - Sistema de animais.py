#Bruno Neemias Alves Mota
#Sistema de animais 

#Abstract Base Classes, para criar classes abstratas
from abc import ABC, abstractmethod

# Classe base abstrata
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod #decorador do módulo todas as subclasses terão o mesmo "contrato"
    def fazer_som(self):
        #placeholder quem vai escrever o que ele faz são as subclasses
        pass

# Classe derivada Cachorro
class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: Au Au!"

# Classe derivada Gato
class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: Miau!"

# Classe derivada Passarinho
class Passarinho(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: Piu Piu!"

# Função principal para demonstrar polimorfismo.
# um mesmo método pode ter diferentes comportamentos
def main():
    #Lista de animais(objetos)
    animais = [
        Cachorro("Bostinha"),
        Gato("Fredrico"),
        Passarinho("Chico")
    ]

    print("=== Sistema de Animais ===")
    # Percorre a lista de animais
    for animal in animais:
        # Para cada animal da lista, chama o método fazer_som()
        # e imprime o resultado na tela
        print(animal.fazer_som())

if __name__ == "__main__":
    main()
