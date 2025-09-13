"""
Operadores Lógicos:
and  E
or OU
not Negativo

Prioridade:
1° ()
2° not
3° and
4° or

Utilização: Usaremos esses operadores sempre que precisarmos unir duas ou
mais comparações lógicas ou criar expressões lógicas mais completas
"""

# AND (para quando todas as condições tem que ser atendidas)

print(False and False )
print(False and True )
print(True and False )
print(True and True )
print(True and True and True and True and True and False) # 1 x 1 x 1 x 1 x 1 x 1 x 1 x 1 x 0 = 0

# Exemplo login

user = input("Usúario: ")
password = input("Senha: ")

acesso = user == "admin" and password == "senha123"

print()
print(f"Usuário reconhecido: {user == "admin}"}")
print(f"Senha reconhecida: {password == "senha123"}")
print(f"Acesso liberado: {acesso}")
print()


# OR (basta que uma entrada seja verdadeira para que o restante seja verdadeiro)

print(False or False )
print(False or True )
print(True or False )
print(True or True )
print(False or False or False or False or False or True) # 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 1

# Exemplo critérios para reprovar um aluno

media_final = 50
frequencia = .5

reprova_aluno = media_final < 5 or frequencia < .75

print()
print(f"Média final: {media_final:.2f}")
print(f"Frequência: {frequencia:.2%}")
print(f"Aluno reprovado: {reprova_aluno}")

# NOT (usado para inverter o valor-verdade)

print(not False)
print(not True)

print(not 10 > 2 and 10 % 5 == 0)
print(10 > 2 and 10 % 5 == 0)

# Exemplo Bomba D'Água

C = False
B = True
A = True

situacao_1 = not A and not B and not C # quando n tiver água em A, n tiver em B, n tiver em C
situacao_2 = A and not B and not C # se tiver água em A, n tiver em B, n tiver em C
situacao_3 = A and B and not C #se tiver água em A, em B, e não tiver em C

bomba = situacao_1 or situacao_2 or situacao_3
print(f"Bomba Ligada: {bomba}")








