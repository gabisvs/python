print("*********Somador de Despesas********")
despesas = int(input("Digite a quantidade de despesas: "))
total = 0

for i in range(1, despesas + 1):
    valor_compra = float(input(f"Valor da {i} despesa R$ "))
    total = total + valor_compra

print("")
print(f"Você gastou um total de R$ {total} ")
print("************************************")




