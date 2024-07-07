from pytest import mark

from musicando.conversores import intervaloTxtNotacaoInt, intervaloTxtNum


@mark.parametrize(
    'intervaloTexto,notacaoInteiro',
    [
        ('T T S T T T', [0, 2, 4, 5, 7, 9, 11]),  # escala maior natural
        ('T S T T S T', [0, 2, 3, 5, 7, 8, 10]),  # escala menor natural
        (
            'T S T T T+S S',
            [0, 2, 3, 5, 7, 10, 11],
        ),  # escala menor harmonica
        (
            '3S T T T S S',
            [0, 3, 5, 7, 9, 10, 11],
        ),  # Escala Enigmática
    ],
)
def test_deve_converter_intevalo_em_texto_para_integer_notation(
    intervaloTexto, notacaoInteiro
):
    resultado = intervaloTxtNotacaoInt(intervaloTexto.split())

    assert resultado == notacaoInteiro


@mark.parametrize(
    'intervaloTexto,intervaloNumerico',
    [
        ('T T S T T T', [0, 1, 2, 2.5, 3.5, 4.5, 5.5]),  # escala maior natural
        ('T S T T S T', [0, 1, 1.5, 2.5, 3.5, 4, 5]),  # escala menor natural
        (
            'T S T T T+S S',
            [0, 1, 1.5, 2.5, 3.5, 5, 5.5],
        ),  # escala menor harmonica
        (
            '3S T T T S S',
            [0, 1.5, 2.5, 3.5, 4.5, 5, 5.5],
        ),  # Escala Enigmática
    ],
)
def test_deve_converter_intevalo_em_texto_para_numerico(
    intervaloTexto, intervaloNumerico
):
    resultado = intervaloTxtNum(intervaloTexto.split())

    assert resultado == intervaloNumerico
