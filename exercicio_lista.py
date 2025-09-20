while True:

    print("-----------------------------------")
    nome = input("Digite o nome do atleta: ")
    if len(nome) == 0: break

    salto1 = float(input("Digite a distância do primeiro salto: "))
    salto2 = float(input("Digite a distância do segundo salto: "))
    salto3 = float(input("Digite a distância do terceiro salto: "))
    salto4 = float(input("Digite a distância do quarto salto: "))
    salto5 = float(input("Digite a distância do quinto salto: "))
    print("")


    saltos = [salto1, salto2, salto3, salto4, salto5]
    media = sum(saltos) / 5

    print(f"Primeiro Salto: {salto1} \nSegundo Salto: {salto2} \nTerceiro Salto: {salto3} \nQuarto Salto: {salto4} \nQuinto Salto: {salto5}")
    print("")

    print(f"O Resultado final é:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos}")
    print(f"A média dos saltos é: {media} ")
    print("-----------------------------------")
    print("")






