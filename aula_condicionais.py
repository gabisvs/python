"""
Condicionais em Python:

if - se (executa um bloco de código se uma condição for verdadeira.)
elif - senão se (permite testar múltiplas condições em sequência.)
else - senão (executa um bloco de código se a condição do if for falsa.)

Utilização: Usaremos condicionais sempre que nosso código tiver um comportamento
para cada situação

Exemplo:
Se o farol estiver verde:
    avance!
senão se estiver amarelo:
    reduza!
senão se estiver vermelhor:
    pare!
senão: observe o guarda de trânsito

"""

# IF

# Exemplo Estoque

codigo_produto = "#123"
quantidade_produto = 500
preco_produto = 4.5

if quantidade_produto < 1000:
    print("Quantidade abaixo do mínimo!")
    print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}")


# Exemplo Farol

farol = "verde"

if farol == "verde":
    print("siga!")


# ELSE ********************************************************************

# Exemplo Estoque

codigo_produto = "#123"
quantidade_produto = 5000
preco_produto = 4.5

if quantidade_produto < 1000:
    print("Quantidade abaixo do mínimo!")
    print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}")

else:
    print("Quantidade está ok!")

# Exemplo Farol

farol = "verde"

if farol == "verde":
    print("siga!")

else:
    print("Observe o guarda de trânsito.")


# ELIF ********************************************************************

# Exemplo Estoque

codigo_produto = "#123"
quantidade_produto = 500
preco_produto = 4.5

if 1000 > quantidade_produto >= 0:
    print("Quantidade abaixo do mínimo!")
    print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}")

elif 1000 <= quantidade_produto <= 2500:
    print("Quantidade ok!")

elif 2500 < quantidade_produto < 5000:
    print("Quantidade acima do máximo!")
    print(f"Vender {quantidade_produto - 2500} unidades de {codigo_produto}")

else:
    print("Quantidade está inválida!")

# Exemplo Farol

farol = "verde"

if farol == "verde":
    print("siga!")

elif farol == "amarelo":
    print("Reduza!")

elif farol == "vermelho":
    print("Pare!")

else:
    print("Observe o guarda de trânsito.")


# NESTED IF ********************************************************************

# Exemplo Estoque

codigo_produto = input("Código do produto: ")
quantidade_produto = input("Quantidade do produto: ")
preco_produto = 4.5

if codigo_produto == "#123":

    if 1000 > quantidade_produto >= 0:
        print("Quantidade abaixo do mínimo!")
        print(f"Comprar {1000 - quantidade_produto} unidades de {codigo_produto}")

    elif 1000 <= quantidade_produto <= 2500:
        print("Quantidade ok!")

    elif 2500 < quantidade_produto < 5000:
        print("Quantidade acima do máximo!")
        print(f"Vender {quantidade_produto - 2500} unidades de {codigo_produto}")

    else:
        print("Quantidade está inválida!")


elif codigo_produto == "#344":

    if 700 > quantidade_produto >= 0:
        print("Quantidade abaixo do mínimo!")
        print(f"Comprar {700 - quantidade_produto} unidades de {codigo_produto}")

    elif 700 <= quantidade_produto <= 1500:
        print("Quantidade ok!")

    elif 1500 < quantidade_produto < 3500:
        print("Quantidade acima do máximo!")
        print(f"Vender {quantidade_produto - 1500} unidades de {codigo_produto}")

    else:
        print("Quantidade está inválida!")



# Operações ternárias

media = 3

status = "Aprovado" if media >= 5 else "Reprovado"
print(f"Média: {media}")
print(f"Status: {status}")

# Match Case

dia_semana = int(input("Digite o número do dia da semana (Ex: 1 - Domingo)"))

match dia_semana:

    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sábado")
    case _: print("Dia Inválido")














