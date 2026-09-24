from rich.traceback import install
from rich import print
from rich.panel import Panel

install()


class BahTcheChurras():
    lista_cornos = []
    def __init__(self, pessoas, quantia, valorkg, titulo):
        self.pessoas = pessoas
        self.quantia = quantia
        self.valorkg = valorkg
        self.valor = 0
        self.quantity = 0
        self.titulo = titulo

    def detalhamento(self):



        conteudo = (
            f"[bold yellow]Quantidade de pessoas[/] {self.pessoas}\n"
            f"[bold red]Valor necessario[/] R$ {self.valor}\n"
            f"[bold]Quantia de carne necessaria[/] {self.quantity}\n"
        )

        return Panel(
            conteudo,
            expand=False,
            title=f"[bold purple]{self.titulo}",
            border_style="red",

        )



def churasnemeo():

    print("Qual o nome do churrasco?")
    titulo = input("")

    print("Quantas pessoas?")
    pessoas = int(input(""))

    print("Qual o Valor do kg da Carne?")
    valorkg = float(input(""))

    print("Qual a media de carne (em kilo) para cada um?")
    mediacarne = float(input())

    c = BahTcheChurras(
        pessoas=pessoas, quantia=mediacarne, valorkg=valorkg, titulo=titulo
    )

    c.quantity = c.pessoas * c.quantia

    c.valor = c.quantity * c.valorkg

    BahTcheChurras.lista_cornos.append(c)
    print(c.detalhamento())

churasnemeo()