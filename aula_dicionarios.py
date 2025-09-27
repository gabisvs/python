"""
Dicionários: Uma coleção Python

Características :
{chave1: valor1, chave2: valor2, chave3, valor3}
-podem ser heterogêneas
-são iteravéis
-não são indexados
-são mutáveis
"""

usuario = {
    "nome": "Gabrielli",
    "idade": "21",
    "e-mail": "gabivirgilio@outlook.com",
    "irmaos": ["Ana", "Daniel", "Maria"]
}

print(usuario)
print(type(usuario))

for item in usuario:
    print(item)
print()

#nao indexadas, tudo pela chaves
print("Nome", usuario["nome"])
print()

# formas de "pegarmos" valores de um dicionario
print("Nome", usuario["nome"])
print(usuario.get("nome"))
print()

#formas de criar novos valores em dicionario
usuario["altura"] = 1.8
print(usuario)
print()

usuario.update({"altura": 1.8})
print(usuario)
print()

#formas de remover valores de um dicionario
del usuario["altura"]
print(usuario)
print()

valor = usuario.pop("altura")
print(usuario)
print(valor)
print()

#metodos legais

#só quero as chaves
print(list(usuario.keys()))
for chave in usuario.keys():
    print(valor)

#só quero as chaves
print(list(usuario.values()))
for chave in usuario.values():
    print(valor)

#chaves e valores
print(list(usuario.items()))
for chave, valor in usuario.items():
    print(chave, " -> ", valor)

#criando dicionarios a partir de listas
alunos = ["Gabrielli", "Luis", "Leticia"]
notas = [5, 8, 9]

alunos_notas = dict(list(zip(alunos,notas)))
print(alunos_notas)

#aplicações
