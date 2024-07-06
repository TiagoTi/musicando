from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musicando.escalas import escala

app = Typer()
console = Console()


@app.command()
def escalas(
    tonica=Argument('c', help='Nota tônica da escala'),
    tonalidade=Argument('maior', help='Nome da escala'),
):
    notas, graus = escala(tonica, tonalidade).values()
    table = Table()
    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)


if __name__ == '__main__':
    app.run(escalas)
