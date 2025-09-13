"""
Input de Dados:

- função input()
    input(argumento do tipo string)

⚠️ - o input sempre retornará valores do tipo string
"""

codigo_produto = input("Informe o código do produto: ")
quantidade_produto = int(input(f"Quantidade de {codigo_produto}: "))
preco_produto = float(input(f"Preço de {codigo_produto}: R$ "))

# print()
# print(codigo_produto)
# print(quantidade_produto, type(quantidade_produto))

print(f"Código: {codigo_produto}, Quantidade: {quantidade_produto}, "
      f"Preço: R$ {preco_produto:,.2f}")