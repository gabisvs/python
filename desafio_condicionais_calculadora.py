operador =  int(input("""
********************
Escolha a Operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão 
5 - Potência 
********************
"""))

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print("")
match operador:
    case 1: print(f"O resultado é: {valor1 + valor2:.2f}")
    case 2: print(f"O resultado é: {valor1 - valor2:.2f}")
    case 3: print(f"O resultado é: {valor1 * valor2:.2f}")
    case 4: print(f"O resultado é: {valor1 / valor2:.2f}")
    case 5: print(f"O resultado é: {valor1 ** valor2:.2f}")
