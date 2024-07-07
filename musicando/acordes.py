from musicando.constantes import FORMA_ACORDES, GRAUS
from musicando.escalas import escala


def transformar_string(s: str) -> str:
    s = s.upper()
    if len(s) > 1:
        s = s[:-1] + s[-1].lower()
    return s


def acorde(cifra: str):
    tonalidade = 'maior'
    if 'm' in cifra:
        tonalidade = 'menor'
        cifra = cifra.split('m')[0]

    # Escerver teste informando: minusco/maiusculo
    print('acorde nota', cifra)
    nota = transformar_string(cifra)

    # Escerver testes informando: tonalidade maiuscula e minusculo
    tonalidade = tonalidade.upper()

    # criar teste quando não encontra retornar error
    intervalos = FORMA_ACORDES[tonalidade]

    # Teste caso nota informada não exite
    escala_tonal = escala(tonica=nota, nomeEscala=tonalidade)

    notas = list()
    graus = list()
    grau = 0

    for intervalo in intervalos:
        indice = intervalo % len(escala_tonal['notas'])
        notaIndice = escala_tonal['notas'][indice]
        notas.append(notaIndice)
        graus.append(GRAUS[grau])
        grau += 2

    return {
        'notas': notas,
        'graus': graus,
    }
