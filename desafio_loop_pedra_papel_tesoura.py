import random

while True:
    print("********************")
    print("Bem-vindo ao jogo!")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("Para sair, digite 4")
    opcao = int(input("Selecione uma opção: "))
    opcao_bot = random.choice (["Pedra",  "Papel", "Tesoura"])

    if opcao == 1 and opcao_bot == "Pedra":
        print(f"O bot escolheu: {opcao_bot}")
        print("Empatou! jogue novamente.")
        print("")

    elif opcao == 1 and opcao_bot == "Papel":
        print(f"O bot escolheu: {opcao_bot}")
        print("Você perdeu essa rodada!")
        print("")

    elif opcao == 1 and opcao_bot == "Tesoura":
        print(f"O bot escolheu: {opcao_bot}")
        print("Você perdeu essa rodada!")
        print("")

    if opcao == 2 and opcao_bot == "Pedra":
        print(f"O bot escolheu: {opcao_bot}")
        print("Você ganhou essa rodada!")
        print("")

    elif opcao == 2 and opcao_bot == "Papel":
        print(f"O bot escolheu: {opcao_bot}")
        print("Empatou! jogue novamente.")
        print("")

    elif opcao == 2 and opcao_bot == "Tesoura":
        print(f"O bot escolheu: {opcao_bot}")
        print("Você perdeu essa rodada!")
        print("")

    if opcao == 3 and opcao_bot == "Pedra":
        print(f"O bot escolheu: {opcao_bot}")
        print("Você perdeu essa rodada!")
        print("")

    elif opcao == 3 and opcao_bot == "Papel":
        print(f"O bot escolheu: {opcao_bot}")
        print("Você ganhou essa rodada!")
        print("")

    elif opcao == 3 and opcao_bot == "Tesoura":
        print(f"O bot escolheu: {opcao_bot}")
        print("Empatou! jogue novamente.")
        print("")

    elif opcao == 4:
        break

    else :
        print("Opção inválida. Escolha novamente!")