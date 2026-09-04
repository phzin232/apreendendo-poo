from rich import print
from rich.table import Table
from rich.traceback import install

install()

class Funcionario:
    lista_funcionario =[]
    def __init__(self, nome, setor, cargo):

        self.nome = nome
        self.setor = setor
        self.cargo = cargo

def testepqsoburro():
    quantity = 0;
    table = Table(title="Funcionarios", style=("Cyan"))

    quantity = int(input("quantos funcionarios sera necessario o cadastro?"))

    table.add_column("Nome",justify="right")
    table.add_column("Setor",justify="center")
    table.add_column("Cargo",justify="left")


    while(quantity>0):
        quantity -=1
   
        print("[bold]Escreva o nome do funcionario completo[/] ")
        nome = input(" ")

        print("Setor")
        setor = input(" ")

        print("Cargo")
        cargo = input("")

        f = Funcionario(nome=" ",setor=" ",cargo=" ")     

        table.add_row(nome,setor,cargo)

        Funcionario.lista_funcionario.append(f)
        
    if(quantity<=0):
        print(table)


    

testepqsoburro()