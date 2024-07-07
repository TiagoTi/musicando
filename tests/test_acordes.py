from pytest import mark

from musicando.acordes import acorde

"""
entrada C, maior


esperado
I - III - V
C E G
"""


@mark.parametrize(
    'nota,esperado,graus',
    [
        (
            'C',
            ['C', 'E', 'G'],
            ['I', 'III', 'V'],
        ),
        ('Cm', ['C', 'D#/Eb', 'G'], ['I', 'III', 'V']),
        ('C#/Db', ['C#/Db', 'F', 'G#/Ab'], ['I', 'III', 'V']),
    ],
)
def test_deve_retornar_notas_correspondentes(nota, esperado, graus):
    result = acorde(nota)
    assert result['notas'] == esperado
    assert result['graus'] == graus
