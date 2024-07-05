from musicando.escala import escala


def test_escala_deve_funcionar_com_notas_minusculas():
    tonica = 'c'
    tonalidade = 'maior'

    resultado = escala(tonica, tonalidade)
    assert resultado


def test_escala_deve_funcionar_com_nome_de_escala_nao_sentivo():
    tonica = 'C'
    tonalidade = 'maIor'

    resultado = escala(tonica, tonalidade)
    assert resultado
