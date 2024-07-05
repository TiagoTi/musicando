poetry shell

pytest
poetry add --group develop pytest pytest-cov

pytest-cov
cobertura: sever para acompanhar se esquecemos de cobrir algum fluxo nos testes.

padronização de código (code style)
    vertical hanging indent (alinhamento vetical) entre as coisas com virgula no final
    pep8
        aspas simples no lugar de dupla
        79 caracteres por linha
    (lint) tem um cara chamado blue que serve tanto para formar arquivo, tanto para verificar se o

    importes ordenados:
        isort (lint)
            baixa visão ou que não enxerga
---
doc - mkdocs
    estrturura de documentação, serve-live, exporta
    mkdostrings busca a doc na docstring no código fonte
        ele leve qualquer doc string (não apenas de python)
        então é necessáro instalar uma ferramenta que trata python: mkdostrings-python