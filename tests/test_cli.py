from pytest import mark
from typer.testing import CliRunner

from musicando.cli import app

runner = CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout():
    result = runner.invoke(app, 'escala')
    assert result.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_deve_content_as_notas_na_resposta(nota):
    result = runner.invoke(app)
    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_deve_content_as_notas_na_resposta(grau):
    result = runner.invoke(app, ['escala', 'E', 'Maior'])
    assert grau in result.stdout


@mark.parametrize(
    'nota', ['B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A#/Bb']
)
def test_deve_content_as_notas_na_resposta_escala_B_maior(nota):
    result = runner.invoke(app, ['escala', 'B', 'Maior'])
    print(result)
    assert nota in result.stdout
