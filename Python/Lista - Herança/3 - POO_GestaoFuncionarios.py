# Bruno Silva dos Santos

# Classe base Funcionario
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def addAumento(self, valor):
        self.salario += valor  # Aplica aumento ao salário

    def ganhoAnual(self):
        return self.salario * 12  # Retorna o salário anual

    def exibeDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário mensal: R$ {self.salario:.2f}")
        print(f"Ganho anual: R$ {self.ganhoAnual():.2f}")


# Classe Assistente herda de Funcionario
class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, nova_matricula):
        self.matricula = nova_matricula

    def exibeDados(self):
        super().exibeDados()
        print(f"Matrícula: {self.matricula}")


# Classe Tecnico herda de Assistente e possui bônus salarial
class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.bonus = bonus

    def ganhoAnual(self):
        return (self.salario + self.bonus) * 12  # Salário com bônus

    def exibeDados(self):
        super().exibeDados()
        print(f"Bônus mensal: R$ {self.bonus:.2f}")
        print(f"Ganho anual com bônus: R$ {self.ganhoAnual():.2f}")


# Classe Administrativo herda de Assistente e possui turno e adicional noturno
class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno.lower()
        self.adicional_noturno = adicional_noturno

    def ganhoAnual(self):
        if self.turno == "noite":
            return (self.salario + self.adicional_noturno) * 12
        else:
            return self.salario * 12

    def exibeDados(self):
        super().exibeDados()
        print(f"Turno: {self.turno.capitalize()}")
        if self.turno == "noite":
            print(f"Adicional noturno: R$ {self.adicional_noturno:.2f}")
        print(f"Ganho anual: R$ {self.ganhoAnual():.2f}")


# Exemplo de uso
print("=== Funcionário ===")
f = Funcionario("Carlos", 3000)
f.addAumento(500)
f.exibeDados()

print("\n=== Assistente ===")
a = Assistente("Ana", 2800, "A123")
a.exibeDados()

print("\n=== Técnico ===")
t = Tecnico("Bruno", 3200, "T456", 400)
t.exibeDados()

print("\n=== Administrativo (Turno Noite) ===")
adm = Administrativo("Fernanda", 2900, "AD789", "noite", 350)
adm.exibeDados()

print("\n=== Administrativo (Turno Dia) ===")
adm_dia = Administrativo("João", 2900, "AD790", "dia", 350)
adm_dia.exibeDados()
