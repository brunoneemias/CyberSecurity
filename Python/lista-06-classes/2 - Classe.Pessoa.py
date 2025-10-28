# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Pessoa em Python
# Descrição: Armazena dados de uma pessoa e verifica se o ano de nascimento é bissexto
# ============================================================

class Pessoa:
    # Método construtor: inicializa os atributos da pessoa
    def __init__(self, nome, ano_nascimento, profissao):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.profissao = profissao

    # Método para verificar se o ano de nascimento é bissexto
    def ano_bissexto(self):
        ano = self.ano_nascimento
        # Regra para ano bissexto:
        # - Divisível por 4
        # - Não pode ser divisível por 100, exceto se for por 400
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False

    # Método para exibir as informações da pessoa
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Ano de nascimento: {self.ano_nascimento}")
        print(f"Profissão: {self.profissao}")
        if self.ano_bissexto():
            print("O ano de nascimento foi bissexto.")
        else:
            print("O ano de nascimento NÃO foi bissexto.")

# ============================================================
# Exemplo de uso da classe Pessoa
# ============================================================

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Ana Souza", 1996, "Engenheira")

# Exibindo as informações da pessoa
pessoa1.exibir_informacoes()
