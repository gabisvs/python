# Strings

# Métodos úteis

# Formatação

texto = "pRoGrAmAçÃo Em PyThOn"

print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
print(texto.replace("Em", "Com").title())
print(" John Doe ".strip())

# Exemplo 1
# nome = input("Nome: ")
# ultimo_nome = input("Último nome: ")
# email = nome.lower() + "." + ultimo_nome.lower() + "@senai.com"
# print(email)

# Exemplo 2
# nome = input("Nome e último nome: ")
# email = nome.lower().replace(" ", ".") + "@senai.com"
# print(email)

# Validação
import string

print("Todas as letras", string.ascii_letters)
print("Todos os digitos", string.digits)
print("Todas as pontuações", string.punctuation)

print()
print("João".isalpha())
print("11999999999".isdigit())
print("LED200".isalnum())

# Separando strings
nome_completo = "Thiago Lima"
print(nome_completo.split())

# funções
print("Quantos char tem a palavra paralelepipedo?", len("paralelepipedo"))

print()
print()
print()
print()
print()
print()
print()




"""
Strings como iteráveis:

- O que é um iterável:  é tudo valor o qual eu posso 'percorrer'
"""

# Indexadas em 0

texto = "Programação em Python"
print("o que está na posição zero da variável texto:", texto[0])

# Índice
print(texto[0])
print(texto[2])
print(texto[5])
print(texto[10])
print(texto[20])
print(texto[-1])

# Slicing
print(texto[0:6])
print(texto[5:17])
print(texto[3:8])
print(texto[:10])
print(texto[6:])
print(texto[:15:2])
print(texto[::5])
print(texto[::2])
print(texto[::-1])