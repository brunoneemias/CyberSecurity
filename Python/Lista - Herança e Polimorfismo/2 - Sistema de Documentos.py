# Bruno Neemias Alves Mota
# Sistema de Documentos

#Abstract Base Classes, para criar classes abstratas
from abc import ABC, abstractmethod

# Classe base abstrata
class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    @abstractmethod #decorador do módulo todas as subclasses terão o mesmo "contrato"
    def exibir_informacoes(self):
        #placeholder quem vai escrever o que ele faz são as subclasses
        pass

# Classe derivada Contrato
class Contrato(Documento):
    def __init__(self, titulo, empresa, prazo):
        super().__init__(titulo)
        self.empresa = empresa
        self.prazo = prazo

    def exibir_informacoes(self):
        return f"Contrato: {self.titulo}\nEmpresa: {self.empresa}\nPrazo: {self.prazo} meses"

# Classe derivada Relatorio
class Relatorio(Documento):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo)
        self.autor = autor
        self.paginas = paginas

    def exibir_informacoes(self):
        return f"Relatório: {self.titulo}\nAutor: {self.autor}\nTotal de páginas: {self.paginas}"

# Classe derivada Certificado
class Certificado(Documento):
    def __init__(self, titulo, aluno, curso):
        super().__init__(titulo)
        self.aluno = aluno
        self.curso = curso

    def exibir_informacoes(self):
        return f"Certificado: {self.titulo}\nAluno: {self.aluno}\nCurso: {self.curso}"

# Função principal para demonstrar polimorfismo
def main():
    documentos = [
        Contrato("Contrato de Trabalho", "Empresa XPTO", 12),
        Relatorio("Relatório Financeiro", "Carlos Silva", 30),
        Certificado("Certificado de Conclusão", "Bruno Neemias", "CompTIA Security+")
    ]

    print("=== Sistema de Documentos ===")
    for doc in documentos:
        print(doc.exibir_informacoes())
        print("-" * 40)

if __name__ == "__main__":
    main()
