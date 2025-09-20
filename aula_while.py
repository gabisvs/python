"""
While: usado para criação de estruturas de repetição condicionais, ou seja,
'enquanto' uma condição for True todo o bloco se repetirá

Sintaxe:

while condicção:
    bloco do while

continue: retora até a verificação da condição do while
break: quebra o looping

"""

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("Fim das repetições...")


print("")
n = int(input("N: "))


while n <= 50:

    if n == 50:
        print(f"{n} é igual.")

    else:
        print(f"{n} é menor que 50")

    n = int(input("N: "))

print(f"{n} é maior que 50.")
print("")

# Exemplo Login

user = input("Usuário: ")
if user == "admin":
    password = input("Senha: ")

    while password != "senha123":
        print("Senha incorreta!")
        password = input("Senha: ")

    else:
        print("Bem-vindo!")

else:
    print("Usuário não cadastrado!")


print("")
# tentativas de senha limitada

import time

tentativas = 0

while True:

    if tentativas < 3:
        user = input("Usuário: ")
        if user == "admin":

            password = input("Senha: ")
            if password == "senha123":
                print("Bem-vindo")
                break

            else:
                print("Senha incorreta: ")
                tentativas += 1
                continue

        else:
            print("Tentativas excedidas!")
            for i in range(10, 0, -1):
                print("\r", end=f"Espere: {i} segundos.")
                time.sleep(1)
            print()
            tentativas = 0
            continue
