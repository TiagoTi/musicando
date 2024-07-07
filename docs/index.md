# Musicando

![logo do projeto](assets/logo.png){width="300" .center}

## Tudo é intervalo

Há pouco mais de um ano começei a estuar música, até então
o foco principal estava em adptar o corpo com o instrumento
agora nas aulas começamos a ter uma carga de estudos teórico

no começo, eu não tentendia com profundidade (não que hoje eu entenda rs)
o que era escala, campo harmonico, acordes,
embora que quando começamos a fazer exercicios de mobilidade no piano/teclado já
fazemos uma escala que ganhamos pronta, a escala de DÓ maior ...

Agora revisitando alguns conceitos estou acreditando que o fundamento de tudo
são os intervalos, o resto são abstrações montandas em cida deste conceito.

Escrever este programa foi uma forma que encontrei de revisar e criar uma estrutura de 
conhecimento mais solido para que eu pudesse enxergar com maior claresa esses assuntos

Um intervalo, é a distancia entre duas coisas, no caso de múscia é a distancia entre dois sons
(não importa agora se são executados ao mesmo tempo, ou seja no conceito harmonico, ou melódigo aonde são executados um após o outro).

A base de estudo e materias que buscam como base o metodo europeu
compreende que exitem 12--- intervalos que são distintos entre si
e que são perceptivies aos ouvidos humanos
(quero dizer que estamos falando de frequencias preestabelecidas pelo estudo da música, dado que fisicamente falando 0,001hz entre dois sons já é um intervalo)
por falar em hz não vai ser necessário trabalhar o assunto neste nivel,

Então podemos pensar da seguinte forma, dado uma nota
executada seguidamente vamos ter o mesmo som que tem distancia zero de si mesma
Essa mesma primeira nota recebe um nome que define sua qualidade e outra a sua quantidade, a quntidade e uma qualidade
este experimento não visa detalhar/ explica e nem revisar este conceito por hora
vamos entender que a caracteristica quantitativa serve para que seja possivel rativisar 
essas distancia, iniciando de qualquer nota,
Já a qualidade, tem a funcionalidade de garantir a montagem de conceitos formais a cerca de certas caracteristicas musicias...

Na tabela abaixo representando meio tom como uma unidade de medida
ou seja 4 é equivante a 2 Tons por exemplo

|Distancia Inteira|Relativizada  a Tons|Grau|Qualidade|Detalhes|
|--|---|----|----------|-----------------------------------|
|0 |0  |I   |Justo    |primera, Tonica, chamada de Unisono|
|1 |0.5|ii  |Menor    |segunda menor|
|2 |1  |II  |Maior    |segunda maior|
|3 |1.5|iii |Menor    |terça menor|
|4 |2  |III |Maior    |terça maior|
|5 |2.5|iv  |Menor    |quarta menor (livros antigos)|
|*5|2.5|IV  |Justo    |quarta justa|
|6 |3  |IV+ |Aumentado|quarta aumentada|
|6 |3  |V-  |Diminuto |quinta diminuto|
|7 |3.5|V   |Justo    |quinta justa|
|*8|4  |V+  |Aumentado|quinta aumentada|
|8 |4  |vi  |Menor    |sexta menor|
|9 |4.5|VI  |Maior    |sexta maior|
|10|5  |vii |Menor    |sétima menor|
|11|5.5|VII |Maior    |sétima maior|
|12|6  |VIII|Justo    |oitava, justa|

|Qualidade|Notações|
|-|-|
|Maior    |M      |
|Menor    |m      |
|Justo    |J      |
|Diminuto |dim d °|
|Aumentado|Aum A  |

Bom agora dados que temos uma tabela que mede os intervalos e qualifica os mesmo

### Notações

Estudos, observações e experimentos compreendem trazem agrupamentos
de intervaloas, presumo que pra facilitar a comunicação e ensino
alguma notações não fazem (e nem precisam fazer) alusão a tabela acima
por exemplo quando estamos falando sobre escala eu encontrei a notação
que me ensinaram , que utiliza a letra T para representar tom e st semiton
ex: escala natural maior
T T ST T T T

(alguma represetam o oitvo grau)
T T ST T T T S

Tambem encontre algo muito similar em material em ingles, aonde W é um tom e H meio ton
ex: escala natural menor
W-H-W-W-H-W-W

Aqui tem uma notação que chegei nela a partir do estudo da tabela acima ...
depois vi que já exista uso da mesma, é uma presentação que leva em consideração
a distancia em unidade de semitons, sendo cada unidade um valor inteiro

assim partindo do unisono podemos representar quaiquers conjuntos de intervalos
permitida pela tabela acima

0 2 4 5 7 9 11 escala natural maior
0 2 4 5 7 9 11 12  escala natural maior com o oitavo grau

o legal dessa forma de notar é que fica muita fácil de entender o pepel da nota numa escala

escala natural maior é composta

|I     |II              |III           |IV             | V             |VI            |VII            |
|------|----------------|--------------|---------------|---------------|--------------|---------------|
|Tonica|segunda<br>maior|terça<br>maior|quarta<br>justa|quinta<br>justa|sexta<br>maior|sétima<br>maior|
|0     |2               |4             |5              |7              |9             |11             |
|C     |D               |E             |F              |G              |A             |B              |


Com isso podemos concluir que esta escala é formada apenas por intervalos justos e maiores.

### Formando escala X da nota Y

Aproveitando que nossa tabela começa do valor zero, e que pra o computador faze sentido inciar contagem de elementos em conjunto a partir do zero
vamos montar uma tabela ao qual dado a notação numerica de qualquer escala, é possivel identificar
as notas que a formam

|0|1       |2|3|4       |5|
|-|--------|-|-|--------|-|
|A|A#<br>Bb|B|C|C#<br>Db|D|

|6       |7|8|9       |10|11      |
|--------|-|-|--------|--|--------|
|D#<br>Eb|E|F|F#<br>Gb|G |G#<br>Ab|

apesar de ter 12 notas, os indices de identificação vão de zero até 11

escala natural maior de A

|I |II |III|IV|V  |VI  |VII|
|--|--|----|--|---|----|---|
|0 |2 |4   |5 |7  |9   |11 |
|A |B |C#  |D |E  |F#  |G# |

Um ponto interessante é que como peguei a primeira nota do conjunto
fica fácil pois todas as notas seguintes tem um indice de localização
menor que o intervalo máximo da escala. Porém se tiver uma escala aonde os saltos extrapolam
a quantidade notas ou então se escolhermos uma nota próxmo ao final da tabela
vamos precisar de uma estratégia para lidar com o a volta para o inicio da tabela

a operação de modulo, é o resto da divisão inteira de um número por outro. A lógica por trás do operador de módulo é baseada na definição matemática do resto. 

|I |II |III|IV|V  |VI  |VII|
|--|--|----|--|---|----|---|
|0 |2 |4   |5 |7  |9   |11 |
|10 |12 |14   |15 |17  |19   |21 |
|G |B |C#  |D |E  |F#  |G# |

10%12=10=G  
12%12=0=A  
14%12=2=B  
15%12=3=C  
17%12=5=D  
19%12=7=E  
21%12=9=F#  

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
