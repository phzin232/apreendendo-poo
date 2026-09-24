from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Produto():
    lista_produto=[]
    def __init__(self, nome ,preco):
        self.nome = nome
        self.preco = preco
        

    def etiqueta(self):
        conteudo =(
            f"[bold white]Item:[/]{self.nome}\n"
            f"[bold yellow]Preço:[/] R$ {self.preco}"
        )

        return Panel(
            conteudo,
            title="[bold magenta] ETIQUETA DE PRODUTO",
            border_style="cyan",
            expand=False,
        )

def cadatrarprodutos():

    quantity = 0
    print("Quantos produtos gostaria de cadastrar?" )
    quantity = int(input())

    while quantity > 0:
        print("[bold]Nome do produto por favor")
        nome = input(" ")

        print("Valor dos produtos")
        valor = input(" ")

        quantity -=1
        p = Produto(nome, valor)    
        Produto.lista_produto.append(p)
    for p in Produto.lista_produto:
        print(p.etiqueta())

cadatrarprodutos()