# Bruno Neemias Alves Mota

# Classe base
class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibirDados(self):
        print(f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}")


# Professor
class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina, salario, carga_horaria):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina
        self.salario = salario
        self.carga_horaria = carga_horaria

    def registrarPresenca(self):
        print(f"Presença registrada como professor da disciplina {self.disciplina}.")

    def calcularSalario(self):
        print(f"Salário mensal: R$ {self.salario:.2f}")


# Funcionário
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, email, setor, cargo, salario):
        super().__init__(nome, cpf, email)
        self.setor = setor
        self.cargo = cargo
        self.salario = salario

    def registrarPresenca(self):
        print(f"Presença registrada como funcionário do setor {self.setor}.")

    def calcularSalario(self):
        print(f"Salário mensal: R$ {self.salario:.2f}")


# Aluno
class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, ra, curso, notas):
        super().__init__(nome, cpf, email)
        self.ra = ra
        self.curso = curso
        self.notas = notas

    def registrarPresenca(self):
        print(f"Presença registrada como aluno do curso {self.curso}.")

    def calcularMedia(self):
        media = sum(self.notas) / len(self.notas)
        print(f"Média do aluno: {media:.2f}")


# Candidato
class Candidato(Pessoa):
    def __init__(self, nome, cpf, email, curso_pretendido, nota_vestibular):
        super().__init__(nome, cpf, email)
        self.curso_pretendido = curso_pretendido
        self.nota_vestibular = nota_vestibular

    def verificarAprovacao(self):
        if self.nota_vestibular >= 600:
            print(f"Candidato aprovado para o curso {self.curso_pretendido}.")
        else:
            print(f"Candidato não aprovado para o curso {self.curso_pretendido}.")

# Teste de Professor
print("=== Teste: Professor ===")
prof = Professor("Marcos", "123.456.789-00", "marcos@fatec.br", "Matemática", 5000.00, 20)
prof.exibirDados()
prof.registrarPresenca()
prof.calcularSalario()

# Teste de Funcionário
print("\n=== Teste: Funcionário ===")
func = Funcionario("Luciana", "987.654.321-00", "luciana@fatec.br", "Biblioteca", "Auxiliar", 3200.00)
func.exibirDados()
func.registrarPresenca()
func.calcularSalario()

# Teste de Aluno
print("\n=== Teste: Aluno ===")
aluno = Aluno("Carlos", "111.222.333-44", "carlos@fatec.br", "RA2023123", "ADS", [8.5, 7.0, 9.0])
aluno.exibirDados()
aluno.registrarPresenca()
aluno.calcularMedia()

# Teste de Candidato
print("\n=== Teste: Candidato ===")
cand = Candidato("Fernanda", "555.666.777-88", "fernanda@fatec.br", "Gestão Empresarial", 620)
cand.exibirDados()
cand.verificarAprovacao()

# Teste de Candidato reprovado
print("\n=== Teste: Candidato Reprovado ===")
cand2 = Candidato("João", "999.888.777-66", "joao@fatec.br", "Logística", 580)
cand2.exibirDados()
cand2.verificarAprovacao()
