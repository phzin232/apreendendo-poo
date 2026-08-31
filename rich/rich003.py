from rich import print
from rich.table import Table

tabea = Table(title="tabela de preço")

tabea.add_column("nome",justify='right',style="cyan")
tabea.add_column("preço", justify='center')

tabea.add_row("cabeã", "R$ 10,00"
)

print(tabea)