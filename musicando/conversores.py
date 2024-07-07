def intervaloTxtNum(intervalos: list):
    tons_acumulados = 0
    notacao_decimal = [tons_acumulados]
    for posicao in intervalos:
        if posicao == 'T':
            tons_acumulados += 1
        if posicao == 'S':
            tons_acumulados += 0.5
        if (
            posicao == 'ST'
            or posicao == 'TS'
            or posicao == 'T+S'
            or posicao == '3S'
        ):
            tons_acumulados += 1.5
        notacao_decimal.append(tons_acumulados)
    return notacao_decimal


def intervaloTxtNotacaoInt(intervalos: list):
    t = intervaloTxtNum(intervalos)
    return [int(i * 2) for i in t]
