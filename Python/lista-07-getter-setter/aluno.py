# Nome: BRUNO NEEMIAS ALVES MOTA

class Aluno:
    def __init__(self, nome, idade):
        # Atributos privados
        self.__nome = nome
        self.__idade = idade
        self.__nota_p1 = None
        self.__nota_p2 = None

    # Getter e Setter para nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        print(f"Nome atualizado para: {novo_nome}")

    # Getter e Setter para idade
    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
            print(f"Idade atualizada para: {nova_idade} anos")
        else:
            print("Erro: Idade inválida.")

    # Setter para nota da P1
    def set_nota_p1(self, nota):
        if 0 <= nota <= 10:
            self.__nota_p1 = nota
            print(f"Nota da P1 registrada: {nota}")
        else:
            print("Erro: Nota inválida. Deve estar entre 0 e 10.")

    # Setter para nota da P2
    def set_nota_p2(self, nota):
        if 0 <= nota <= 10:
            self.__nota_p2 = nota
            print(f"Nota da P2 registrada: {nota}")
        else:
            print("Erro: Nota inválida. Deve estar entre 0 e 10.")

    # Método para calcular a média final
    def calcular_media(self):
        if self.__nota_p1 is not None and self.__nota_p2 is not None:
            media = (self.__nota_p1 + self.__nota_p2) / 2
            print(f"Média final: {media:.2f}")
            return media
        else:
            print("Erro: As duas notas devem estar registradas para calcular a média.")
            return None

    # Método para verificar situação do aluno
    def verificar_situacao(self):
        media = self.calcular_media()
        if media is not None:
            if media >= 6:
                print("Situação: ✅ Aprovado")
            else:
                print("Situação: ❌ Reprovado")

    # Método para exibir os detalhes do aluno
    def exibir_detalhes(self):
        print("🎓 Detalhes do Aluno:")
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade} anos")
        print(f"Nota P1: {self.__nota_p1 if self.__nota_p1 is not None else 'Não registrada'}")
        print(f"Nota P2: {self.__nota_p2 if self.__nota_p2 is not None else 'Não registrada'}")

# Exemplo de uso
aluno1 = Aluno("Lucas Silva", 17)

aluno1.exibir_detalhes()
aluno1.set_nota_p1(7.5)
aluno1.set_nota_p2(6.0)
aluno1.calcular_media()
aluno1.verificar_situacao()
aluno1.set_idade(18)
aluno1.set_nome("Lucas S. Oliveira")
aluno1.exibir_detalhes()