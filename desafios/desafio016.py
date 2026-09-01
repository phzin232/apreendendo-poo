from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Funcionario:
    lista_funcionario =[]
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        Funcionario.lista_funcionario.append(self)

    