"""
Tuplas: Uma coleção Python

Características :
(item1, item2, item3...)
-não precisa colocar paratenses para declarar
-podem ser heterogêneas
-são iteravéis
-são indexadas em zero, assim como strings
-não são mutáveis
"""

minha_tupla = (10, 3.14, "oi", True, [1,2.3], (1,2,3))
print(minha_tupla)
print(type(minha_tupla))

for item in minha_tupla:
    print(item)

#são indexadas em 0
numeros = tuple(range(1,51))

#indice
print(numeros[0])
print(numeros[17])
print(numeros[25])
print(numeros[45])
print(numeros[-1])

#slicing intervalos da lista
print(numeros[0:15])
print(numeros[15:30])
print(numeros[:15])
print(numeros[40:])
print(numeros[::5])
print(numeros[::-5])

#funções
print(len(numeros))
print(sum(numeros))
print(max(numeros))
print(min(numeros))


#tuple unpacking
tupla = 1,2,3
a, b, c = tupla
print(a)
print(b)
print(c)



