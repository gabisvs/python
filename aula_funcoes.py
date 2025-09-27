"""27/09"""

"""
Funções: existem aplicações inteiras que utilizam apenas o paradigma funcional, ou seja,
tudo feito com funções.

vantagens:
-modularização de códgio
-reaproveitamento de código
-abstração

analogia:
pensa em um módulo como uma caixa de ferramentas, e dentro desse módulo existem várias
funções que são coomo ferramentas. 

sintaxe:

def nome_da_funcao():
    o que a função faz 
"""

# declaramos a função
def primeira_funcao():
    print("Minha primeira função.")

# chamamos a função
primeira_funcao()
print(primeira_funcao())

def soma():
    a = 10
    b = 20
    print(a + b)

soma()
print()

#escopo global(existe no arquivo inteiro) e escopo local(só existe dentro da função)
g = 10

def muda_valor(): #acontece regra de hierarquia, usa primeiro valores fora da função
    # global g força a usar o valor da função
    g = 5

muda_valor()
print(g)
print()

#parametros da função (nome)
#parametro na criação da função / argumento quando eu ou usar
def apresentar(nome):
    print(f"Olá, eu sou {nome}")

apresentar("Gabrielli")
apresentar("Gabi")
print()

def soma(a, b):
    resultado = a + b
    print(a)
    print(b)
    print(resultado)

soma(10, 10)
soma(100, 10)
soma(29, 10)

#posicional
soma(10, 12)

#por chave
soma(b=1, a=12)
print()

#parametros com valor padrão
#tem hierarquia, caso um for sem valor padrão ele vem primeiro nos parenteses:
#def soma(a, b=0):
def soma(a=0, b=0):
    res = a + b
    print(res)

soma(10)
soma(b=104)
soma()
print()

#caso eu não passe um parametro, ele irá utilizar o padrão
def gera_email(nome, sobrenome, dominio="senai.com"):
    email = f"{nome}.{sobrenome}@{dominio}"
    return email #é tipo um break, para o código/ação final

email_gabrielli = gera_email("gabrielli", "virgilio")
email_leticia = gera_email("leticia", "oliveira", "sesi.com")

#tipo none / return
print(email_gabrielli)
print(email_leticia)
print()

#funções realizam uma ação ou que realizam e retornam alguma coisa
def soma(a=0, b=0):
    resultado = a +b
    return resultado

res_1 = soma(10, 90)
res_2 = soma(10, 34)
res_3 = soma("10", "10")
print(res_1)
print(res_2)
print(res_3)
print()

#tipagem
def soma(a: int = 0, b: int = 0) -> int :
    resultado = a +b
    return resultado

res_1 = soma(10, 90)
res_2 = soma(10, 34)
res_3 = soma("10", "10")
print(res_1)
print(res_2)
print(res_3)
print()


def gera_email(nome: str, sobrenome: str, dominio="senai.com"):
    email = f"{nome}.{sobrenome}@{dominio}"
    return email

# documentação
def soma(a: int, b: int) -> int:
    """
    Recebe dois numeros e retorna a soma dos mesmos
    :param a: valor do tipo int
    :param b: valor do tipo int
    :return: o resultado da soma dos valores
    """
    resultado = a + b
    return resultado

def gera_email(nome: str, sobrenome: str, dominio: str ="senai.com"):
    """
    Função que recebe o nome e o sobrenome e retorna um e-mail
    no formato nome.sobrenome@dominio.com
    :param nome: nome
    :param sobrenome: sobrenome
    :param dominio: dominio (padrão senai.com)
    :return: e-mail no formato: nome.sobrenome@dominio.com
    """

    email = f"{nome}. {sobrenome}@{dominio}"






