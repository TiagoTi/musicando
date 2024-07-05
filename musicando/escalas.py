ESCALA_CROMATICA = 'A A#/Bb B C C#/Db D D#/Eb E F F#/Gb G G#/Ab'.split()

ESCALAS = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'Iwato': (0, 1, 5, 6, 10),
    'Tritone': (0, 1, 4, 6, 7, 10),
    'Octatonic-I': (0, 2, 3, 5, 6, 8, 9, 11),
    'Octatonic-II': (0, 1, 3, 4, 6, 7, 9, 10),
}

GRAUS = 'I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII'.split()


def escala(tonica: str, nomeEscala: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma nota tonica e de um nome de escala

    Parameters:
        tonica: Nota que sera a tônica da escala. Ex: C, C#/Db, D, D#/Eb .
        nomeEscala: o nome de uma escala cadastrada na ferramenta Ex: maior, Tritone, Iwato.

    Returns:
        Um dicionario com  as notas da escala e os graus.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('A', 'maior')
        {'notas': ['A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G#/Ab'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('D', 'Iwato')
        {'notas': ['D', 'D#/Eb', 'G', 'G#/Ab', 'C'], 'graus': ['I', 'II', 'III', 'IV', 'V']}
    """
    tonicaIndex = ESCALA_CROMATICA.index(tonica)
    intervalos = ESCALAS[nomeEscala]

    notasDaEscala = list()
    graus = list()
    grau = 0
    for intervalo in intervalos:
        indicideDaNota = intervalo + tonicaIndex
        if indicideDaNota >= len(ESCALA_CROMATICA):
            indicideDaNota = indicideDaNota % len(ESCALA_CROMATICA)
        notasDaEscala.append(ESCALA_CROMATICA[indicideDaNota])
        graus.append(GRAUS[grau])
        grau = grau + 1
    return {'notas': notasDaEscala, 'graus': graus}


if __name__ == '__main__':
    a = escala('A', 'maior')
    print(a)

    c = escala('C#/Db', 'Iwato')
    print(c)

    db = escala('C#/Db', 'Tritone')
    print(db)

    f = escala('F', 'Octatonic-I')
    print(f)

    g = escala('G', 'Octatonic-II')
    print(g)
