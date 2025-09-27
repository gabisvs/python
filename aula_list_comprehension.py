"""
List Comprehension

-uma forma elegante de criar uma lista
-podemos criar listas de forma declarativa
-a partir de uma lista existente
-a partir de um range
-a partir de uma string
-a partir de um dicionario

Sintaxe:
[i for i in iterável]
"""

from math import sqrt
from statistics import mean

#modo normal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = []

for n in numeros:
    quadrados.append(n**2)

print(quadrados)
print()

#modo comprehension
quadrados_comprehension = [n ** 2 for n in numeros]
print(quadrados_comprehension)
print()

raizes = [round(sqrt(x),2) for x in range(4, 30)]
print(raizes)
print()

palavra = "paralelepipedo"

conta_letras = set([(l, palavra.count(l)) for l in palavra])
conta_letras = dict(conta_letras)
print(conta_letras)


alunos_notas = {
    "Luis": [5, 6, 7, 8],
    "Gabrelli" : [5, 9, 9 ,8]
}

medias = [mean(notas) for notas in alunos_notas.values()]
print(medias)

# list comprehension condicionais

#modo normal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        pass

    print(pares)

#modo comprehension
pares_comprehension = [n for n in numeros if n % 2 == 0]


numeros_tipo = \
    [(n, "Par") if n % 2 == 0 else (n, "Ímpar") for n in numeros]
print(dict(numeros_tipo))

