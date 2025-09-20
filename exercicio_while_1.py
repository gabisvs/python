saldo = 0

while True:

    print("************************")
    print("Bem-vindo ao Banco!")
    print("")
    print("Para continuar digite uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Sair")
    print("")
    operacao = int(input("Número: "))

    if operacao == 1:
        print("*************************")
        print("Seção Depósito")
        deposito = float(input("Digite o valor que deseja depósitar R$ "))
        saldo += deposito
        print("")
        print("Transação bem sucedida!")
        print("*************************")
        print("")

    elif operacao == 2:
        if saldo <= 0:
            print("Sem saldo para fazer Saque.")
            print("")

        if saldo >= 1:
            print("*************************")
            print("Seção Saque")
            saque = float(input("Digite o valor que deseja sacar R$ "))
            saldo -= saque
            print("")
            print("Transação bem sucedida!")
            print("")
            print("*************************")


    elif operacao == 3:
        print("")
        print(f"Seu saldo é R$ {saldo} ")
        print("Obrigada por utilizar nosso banco!")
        print("**********************************")
        break

    else:
        print("Operação inválida!")
