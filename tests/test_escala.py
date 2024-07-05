from pytest import mark, raises

from musicando.escalas import ESCALA_CROMATICA, ESCALAS, escala


def test_escala_deve_funcionar_com_notas_minusculas():
    tonica = 'c'
    nomeEscala = 'maior'

    resultado = escala(tonica, nomeEscala)
    assert resultado


def test_escala_deve_funcionar_com_nome_de_escala_nao_sentivo():
    tonica = 'C'
    nomeEscala = 'maIor'

    resultado = escala(tonica, nomeEscala)
    assert resultado


def test_retorna_erro_nota_nao_existe():
    tonica = '3X'
    nomeEscala = 'MAIOR'
    mensagem_erro = (
        f'Essa nota não existe, tente uma dessas {ESCALA_CROMATICA}'
    )

    with raises(ValueError) as error:
        escala(tonica, nomeEscala)
    assert mensagem_erro == error.value.args[0]


def test_retorna_erro_escala_nao_existe():
    tonica = 'C'
    nomeEscala = 'XX'
    mensagem_erro = f'Essa escala não existe ou não foi implementada, tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, nomeEscala)
    assert mensagem_erro == error.value.args[0]


@mark.parametrize(
    'notaTonica,nomeEscala,esperado',
    [
        ('C', 'MAIOR', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        (
            'C#/Db',
            'MAIOR',
            ['C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C'],
        ),
        ('A', 'MAIOR', ['A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G#/Ab']),
        ('D', 'MAIOR', ['D', 'E', 'F#/Gb', 'G', 'A', 'B', 'C#/Db']),
        ('G', 'MAIOR', ['G', 'A', 'B', 'C', 'D', 'E', 'F#/Gb']),
    ],
)
def test_retorna_notas_corretas(notaTonica, nomeEscala, esperado):
    print(notaTonica, nomeEscala, esperado)
    resultado = escala(notaTonica, nomeEscala)
    assert resultado['notas'] == esperado


@mark.parametrize(
    'notaTonica,nomeEscala,escalaEsperada,grausEsperados',
    [
        (
            'C',
            'MAIOR',
            ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
        ),
        (
            'D',
            'Iwato',
            ['D', 'D#/Eb', 'G', 'G#/Ab', 'C'],
            ['I', 'II', 'III', 'IV', 'V'],
        ),
    ],
)
def test_retorna_os_graus_corretas(
    notaTonica, nomeEscala, escalaEsperada, grausEsperados
):
    print(notaTonica, nomeEscala, escalaEsperada)
    resultado = escala(notaTonica, nomeEscala)
    assert resultado['notas'] == escalaEsperada
    assert resultado['graus'] == grausEsperados
