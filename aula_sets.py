""""""
"""
Sets: Uma coleção Python

Características :
{item1, item2, ..., itemN};
-podem ser heterogêneas
-são iteravéis
-não são indexados
-são mutáveis
-funciona como conjunto matemático;
"""

meu_set = {10, 3.14, "oi", True}
print(meu_set)

for item in meu_set:
    print(item)

numeros = set(range(1, 21))
print(numeros)

# funções
print(len(numeros))
print(sum(numeros))
print(max(numeros))
print(min(numeros))

# metodos de conjunto
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

#adicionar itens a um set
s2.add(9)
print(s2)

#união
s_uniao = s1.union(s2)
print(s_uniao)

#intersecção
s_intersecção = s1.intersection(s2)
print(s_intersecção)

#diferença
s_diferenca = s1.difference(s2)
print(s_diferenca)

#exemplo

votos_a = [
'Maria', 'Ana', 'Davi', 'Miguel', 'Sophia', 'Gustavo', 'Matheus',
'Guilherme', 'Luiz', 'Isabella', 'Beatriz', 'Yasmin', 'Laura',
'Maria Alice', 'Heloísa', 'Maria Cecília', 'Elisa', 'Maria Helena',
'Lívia', 'Maria Júlia', 'Isadora', 'Maria Luiza', 'Rebeca', 'Isis',
'Esther', 'Manuella', 'Ísis', 'Maria Liz', 'Lavínia', 'Ana Laura',
'Ana Clara', 'Maria Luísa', 'Ana Júlia', 'Anna Liz', 'Maria Laura',
'Maria Flor', 'Hellena', 'Maria Isis', 'Maria Julia', 'Cecilia',
'Ana Luiza', 'Lunna', 'Maria Vitória', 'Maria Fernanda', 'Luara',
'Ágatha', 'Ana Cecília', 'Ana Beatriz', 'Luiza', 'Yasmin'
]

votos_b = [
'Maria', 'Maria', 'Ana', 'Davi', 'Miguel', 'Miguel', 'Sophia',
'Gustavo', 'Matheus', 'Guilherme', 'Guilherme', 'Luiz', 'Isabella',
'Isabella', 'Beatriz', 'Yasmin', 'Laura', 'Laura', 'Maria Alice',
'Heloísa', 'Maria Cecília', 'Elisa', 'Elisa', 'Maria Helena',
'Lívia', 'Maria Júlia', 'Isadora', 'Maria Luiza', 'Rebeca',
'Rebeca', 'Isis', 'Esther', 'Manuella', 'Manuella', 'Ísis',
'Maria Liz', 'Lavínia', 'Ana Laura', 'Ana Laura', 'Ana Clara',
'Maria Luísa', 'Ana Júlia', 'Anna Liz', 'Maria Laura', 'Maria Flor',
'Hellena', 'Maria Isis', 'Maria Julia', 'Cecilia', 'Ana Luiza'
]

print("Quantidade de votos candidato A: ", len(votos_a))
print("Quantidade de votos candidato B: ", len(votos_b))

votos_a = set(votos_a)
votos_b = set(votos_b)

print("Quantidade de votos candidato A: ", len(votos_a))
print("Quantidade de votos candidato B: ", len(votos_b))
print("Votou em ambos: ", votos_a.intersection(votos_b))