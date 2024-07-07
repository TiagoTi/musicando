from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musicando.acordes import acorde as _acorde
from musicando.escalas import escala as _escala

app = Typer()
console = Console()


@app.command()
def escala(
    tonica: str = Argument('c', help='Nota tônica da escala'),
    tonalidade: str = Argument('maior', help='Nome da escala'),
):
    notas, graus = _escala(tonica, tonalidade).values()
    table = Table()
    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)


@app.command()
def acorde(
    cifra: str = Argument('Cm', help='Cifra de um acorde'),
):
    notas, graus = _acorde(cifra).values()
    table = Table()
    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)


if __name__ == '__main__':
    app.run(escalas)
