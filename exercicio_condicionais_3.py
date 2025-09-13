print("***************************************")
salario = float(input("Digite o seu salário: "))

print("")

ali10 = (salario * 10) / 100
ali15 = (salario * 15) / 100
ali20 = (salario * 20) / 100

if salario <= 2000:
    print("Você está isento")

elif 2000 < salario <= 3500:
    print(f"O seu salário líquido será: {salario - ali10:.2f}")

elif 3500 <= salario <= 5000:
    print(f"O seu salário líquido será: {salario - ali15:.2f}")

elif salario > 5000:
    print(f"O seu salário líquido será: {salario - ali20:.2f} ")

print("**************************************")

