import os
from operacoes import(
    saque,
    deposito,
    exibir_extrato,
    cadastrar_cliente,
    listar_clientes,
    excluir_cliente,
    cadastrar_conta_corrente,
    listar_contas_correntes,
    excluir_conta_corrente
)

from config import (
    saldo,
    limite,
    extrato,
    numero_saques,
    LIMITE_SAQUES
)

menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Cliente
    [5] Listar Clientes
    [6] Excluir Cliente (CPF cliente)
    [7] Cadastrar Conta Corrente (CPF cliente)
    [8] Listar Contas Correntes
    [9] Excluir Conta Correte (Nº Conta)
    [0] Sair

=> """

while True:

    os.system('clear')
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, extrato, valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(
                                            saldo=saldo, 
                                            valor=valor, 
                                            extrato=extrato, 
                                            limite=limite, 
                                            numero_saques=numero_saques, 
                                            limite_saques=LIMITE_SAQUES
                                        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        cadastrar_cliente()
        
    elif opcao == "5":
        listar_clientes()
        
    elif opcao == "6":
        cpf = input("Digite o CPF do cliente a ser excluído: ")
        excluir_cliente(cpf)
        
    elif opcao == "7":
        cpf = input("Digite o CPF do cliente: ")
        cadastrar_conta_corrente(cpf)

    elif opcao == "8":
        listar_contas_correntes()

    elif opcao == "9":
        conta = input("Digite o nº da conta a ser excluída: ")
        excluir_conta_corrente(conta)

    elif opcao == "0":
        break

    else:
        input("\nOperação inválida, por favor selecione novamente a operação desejada.")

print('\nSaindo do sistema. Tenha um ótimo dia!\n')