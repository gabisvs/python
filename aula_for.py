"""
Em python temos dois tipos de loopings:

-for: criar estrutura de repetição contada;

Utilização: Sempre que eu precisar repetir uma estrutura de código N vezes,
a quantidade de loops pode ser baseada em: ranges, strings, listas, etc

"""

#Sintaxe:
# for i in iterável:
#    bloco do for

numeros = [1, 2, 3, 4, 5]

for i in numeros:
    print("oi")

for i in numeros:
    print(i)

for _ in numeros:
    nome = input("Nome: ")
    print(f"Bem vindo {nome}!")

for letra in "Olá Mundo!":
    print(letra.upper())


# range()

# 1° forma: range(stop)
sequencia = range(2)
print(sequencia)
print(*sequencia)

for i in range(10):
    print(i)

for n in range(5):
    nome = input("Nome: ")
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    media = (n1 + n2) / 2
    print(f"{nome}, sua média é de {media}")

    if media == 10:
        print("A+")

    elif media < 10 and media >=7:
        print("B")

    elif media >=0 and media < 7:
        print("C")

# 2° forma: range(start, stop)

for i in range(1, 11):
    print(f"O quadrado de {i} é {i**2} ")

idade = int(input(14, 25))

if idade in range(14, 25):
    print("Pode fazer o CAI")
else:
    print("Faça um técnico")

# 3° forma: range(star, stop, step)

for n in range(1, 110, 10):
    print(n)

#Exemplo: Cálculo de Comissão para um vendedor de carros
print()
n_carros = int(input("Quantos carros você vendeu em Agosto? "))
total = 0

for venda in range(1, n_carros + 1):
    valor_venda = float(input(f"Valor da {venda} venda: R$"))
    total = total + valor_venda

comissao = total * .07

print()
print(f"Você vendeu um total de: R$ {total: ,.2f}")
print(f"A comissao foi de: R$ {comissao: ,.2f}")
