"""
Operadores de Comparação:

== Igual a
!= Diferente de
> Maior que
< Menor que
>= Maior ou igual
<= Menor ou igual

Usaremos esses operadores sempre que precisarmos fazer comprações emtre valores,
sejam eles int, float ou string

Esses comparadores nos ajudarão a controlar o fluxo do nosso programa

"""
# Igual a ==

print(10 == 10)
print(10 == 10.0)
print(10 == "10")
print(10 == 250 / 50 * 2)
print("senha123" == "Senha123")
print("senha123" == "senha123")
print()

# Diferente !=

print(10 != 10)
print(10 != 10.0)
print(10 != "10")
print(10 != 250 / 50 * 2)
print("senha123" != "Senha123")
print()

# Maior que >

print(10 > 2)
print(10 > 50)
print(10 > 1000 / 9)
print(len("senha123") > 8)
print()

# Maior que <

print(10 < 2)
print(10 < 50)
print(10 < 1000 / 9)
print(len("senha123") < 8)
print()

# Maior ou igual a

print(10 >= 2)
print(10 >= 10)
print(10 >= 50)
print(len("senha123") >= 8)
print()

# Menor ou igual a

print(10 <= 2)
print(10 <= 10)
print(10 <= 50)
print(len("senha123") <= 8)
print()
