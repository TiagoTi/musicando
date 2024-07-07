from musicando.constantes import ESCALA_CROMATICA, ESCALAS, GRAUS


def transformar_string(s: str) -> str:
    s = s.upper()
    if len(s) > 1:
        s = s[:-1] + s[-1].lower()
    return s


def escala(tonica: str, nomeEscala: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma nota tonica e de um nome de escala

    Parameters:
        tonica: Nota que sera a tônica da escala. Ex: C, C#/Db, D, D#/Eb .
        nomeEscala: o nome de uma escala cadastrada na ferramenta Ex: maior, Tritone, Iwato.

    Returns:
        Um dicionario com  as notas da escala e os graus.

    Raises:
        KeyError: caso o nome da escala / intervalo não existe.
        ValueError: caso a nota não seja uma nota válida.

    Examples:
        >>> escala('C', 'MAIOR')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G#/Ab'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('D', 'Iwato')
        {'notas': ['D', 'D#/Eb', 'G', 'G#/Ab', 'C'], 'graus': ['I', 'II', 'III', 'IV', 'V']}
    """
    try:
        tonicaIndex = ESCALA_CROMATICA.index(transformar_string(tonica))
    except ValueError as e:
        raise ValueError(
            f'Essa nota não existe, tente uma dessas {ESCALA_CROMATICA}'
        )

    try:
        intervalos = ESCALAS[nomeEscala.upper()]
    except KeyError as e:
        raise KeyError(
            f'Essa escala não existe ou não foi implementada, tente uma dessas {list(ESCALAS.keys())}'
        )

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
