from math import pi

"""
Concatenação de strings:
- Como se fosse uma 'soma' de strings:

    str + str => strstr
"""

nome = "Thiago"
sobrenome = "Lima"

nome_completo = nome + " " +sobrenome
print(nome_completo)

# Exemplo prático:

codigo_produto = "#12"
quantidade_produto = 200
preco_produto = 3.5

print(codigo_produto, quantidade_produto, preco_produto)

# Código: #12, Quantidade: 200, Preço: R$ 3.50

print("Código: " + codigo_produto + ", Quantidade: " + str(quantidade_produto) +
      ", Preço: R$ " + str(preco_produto))


"""
f-string:
- Nos permite compor strings com variáveis sem sair da string
    f"Texto {variavel} final do texto."  
"""
print()
nome = "Thiago"
sobrenome = "Lima"
nome_completo = f"{nome} {sobrenome}"
print(nome_completo)


# Código: #12, Quantidade: 200, Preço: R$ 3.50

codigo_produto = "#12"
quantidade_produto = 200
preco_produto = 3.5

print()
print(f"Código: {codigo_produto}, Quantidade: {quantidade_produto}"
      f", Preço: R$ {preco_produto:.2f}")

# Forma antiga (.format())
# print("Código: {}, Quantidade: {}, Preço: R$ {}".format(codigo_produto,
#                                                         quantidade_produto,
#                                                         preco_produto))

"""
Formatadores: 
- Casas decimais: .nf
- Separador de milhares: ,
- Porcentagem: %
"""

# - Casas decimais: .nf
print()
print(f"{pi:.5f}")

# - Separador de milhares: ,
print()
n_habitantes_sp = 810729
print(f"{n_habitantes_sp:,}")
capital = 1_000_000.50
print(f"{capital:,.2f}")

# - Porcentagem: %
print()
valor_compra = 100
desconto = .3
valor_final = valor_compra * (1 - desconto)
print(f"Valor compra: R$ {valor_compra:,.2f}")
print(f"Desconto: {desconto:.2%}")
print(f"Valor com desconto: R$ {valor_final:,.2f}")
