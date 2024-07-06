![logo do projeto](assets/logo.png){width="300" .center}

# Musicando

## Como usar

Você pode usar a aplicação executando o comando:

```sh
poetry run escalas

# ou informando uma nota tonica
poetry run escalas A#/Bb

# também é possivel informar o nome de uma escala
poetry run escalas F OCTATONIC-II
```

Exemplo de saída:

```txt
┏━━━┳━━━━┳━━━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━━┓
┃ I ┃ II ┃ III   ┃ IV ┃ V ┃ VI ┃ VII   ┃
┡━━━╇━━━━╇━━━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━━┩
│ D │ E  │ F#/Gb │ G  │ A │ B  │ C#/Db │
└───┴────┴───────┴────┴───┴────┴───────┘
```

## Dúvida

```sh
poetry run escalas --help
```

```txt
 Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                                                                                                                  
                                                                                                                                                                                 
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Nota tônica da escala [default: c]                                                                                                            │
│   tonalidade      [TONALIDADE]  Nome da escala [default: maior]                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                       │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                │
│ --help                        Show this message and exit.                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
