# ============================================================
# Autor: BRUNO NEEMIAS ALVES MOTA
# Projeto: Classe Livro em Python
# Descrição: Gerencia o empréstimo e devolução de livros
# ============================================================

class Livro:
    # Método construtor: define os atributos do livro
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True  # O livro começa como disponível

    # Método para emprestar o livro
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    # Método para devolver o livro
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    # Método para verificar se o livro está disponível
    def verificar_disponibilidade(self):
        if self.disponivel:
            print(f"O livro '{self.titulo}' está disponível para empréstimo.")
        else:
            print(f"O livro '{self.titulo}' está emprestado no momento.")

# ============================================================
# Exemplo de uso da classe Livro
# ============================================================

# Criando um objeto da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)

# Verificando disponibilidade, emprestando e devolvendo
livro1.verificar_disponibilidade()
livro1.emprestar()
livro1.verificar_disponibilidade()
livro1.devolver()
livro1.verificar_disponibilidade()