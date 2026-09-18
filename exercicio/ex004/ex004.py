from rich import print, inspect


class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

        def fazer_aniversario(self):         
            self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula():
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula():
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto():
        pass




a1 = Aluno("josé", 17, "informatica", "T01")

inspect(a1)