"""
Listas: Uma coleção Python

Características :
[item1, item2, item3...]
-podem ser heterogêneas
-não são arrays
-são iteravéis
-listas também são indexadas em zero (assim como as strings)
-são mutáveis
"""

minha_lista = [1, 2, 3, 4, 5, "oi"]
print(minha_lista)
print(type(minha_lista))

lista_2 = [10, 3.14, "oi", True, [1, 2, 3]] # vários tipos de dados
print(lista_2)

matriz = [[1, 2, 3],
          4, 5, 6]

for i in lista_2:
    print(i)

numeros = list(range(51))
print( numeros)

# indice (posição)
print(numeros[0])
print(numeros[10])
print(numeros[27])

# slicing
print(numeros[0:12])
print(numeros[12:40])
print(numeros[:25])
print(numeros[25:])
print(numeros[::5])
print(numeros[::-5])

# funções
print(len(numeros))

# funções lista numerica
print(sum(numeros))
print(max(numeros))
print(min(numeros))

frutas = ["manga", "mamão", "melancia", "morango"]
print("Nossa lista tem", len(frutas))

frutas.append("banana")# adicionando um item a uma lista
print(frutas)

for i in range(3):
    fruta = input("Fruta: ")
    frutas.append(fruta)

frutas.extend(["melão", "maça"]) #adicionando vários items a uma lista
print(frutas)

frutas.insert(1, "banana")
print(frutas)

# remover item de uma lista
ultima_fruta = frutas.pop()
print(ultima_fruta)
print(frutas)

#outra forma de remover
frutas.remove("banana")
del frutas[5]
print(frutas)

# editar

frutas[0] = "pitaya"
print(frutas)

# encontrar a posição de um elemento
print("Melancia está na posição: ", frutas.index("melancia"))
frutas[frutas.index("melancia")] = "carambola"

# contando quantas vezes um dado elemento aparece na lista
print(f"carambola {frutas.count("carambola")} na nossa lista")

# metodo para ordenar uma lista
frutas.sort()
print(frutas)




