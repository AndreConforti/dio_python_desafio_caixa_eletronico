import os

menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    os.system('clear')
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            input('Depósito realizado com sucesso!')

        else:
            input("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            input("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            input("Operação falhou! O valor do saque excede o limite.")
          
        elif excedeu_saques:
            input("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            input('Saque efetuado com sucesso!')

        else:
            input("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        input()

    elif opcao == "0":
        break

    else:
        input("Operação inválida, por favor selecione novamente a operação desejada.")

print('\nSaindo do sistema. Tenha um ótimo dia!\n')