print("*********************************************************")
lado1 = int(input("Digite o valor do primeiro lado:"))
lado2 = int(input("Digite o valor do segundo lado:"))
lado3 = int(input("Digite o valor do terceiro lado:"))

print("")

if  lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:

    if lado1 == lado2 == lado3:
        print("Os valores informados representam um triângulo Equilátero!")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores informados representam um triângulo Isósceles!")

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Os valores informados representam um triângulo Escaleno")

else:
     print("Os valores informados não representam um triângulo. Tente novamente!")

print("*********************************************************")