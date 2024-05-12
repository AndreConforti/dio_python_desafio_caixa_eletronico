import json
from config import (
    saldo,
    limite,
    extrato,
    numero_saques,
    LIMITE_SAQUES
)

def abrir_arquivo():
    try:
        with open('clientes_contas.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = {
            'clientes': [],
            'contas_correntes': []
        }    
    return dados


def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
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

    return saldo, extrato, numero_saques


def deposito(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        input('Depósito realizado com sucesso!')

    else:
        input("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    input()


def cadastrar_cliente():
    '''Função para cadastrar um novo cliente'''
    nome = input("\nNome: ").strip().upper()
    data_nasc = input("Data de Nascimento: (dd/mm/aaaa) ").strip()
    cpf = input("CPF: ").strip().replace("-", "").replace(".", "")
    logradouro = input("Logradouro: ").strip().lower()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip().lower()
    cidade = input("Cidade: ").strip().lower()
    estado = input("Estado: ").strip().upper()
    
    # primeiro precisamos verificar em nossa lista de clientes se o cpf já está cadastrado
    dados = abrir_arquivo()
        
    for cliente in dados['clientes']:
        if cpf == cliente['cpf']:
            input("\nCPF já cadastrado. Cadastro cancelado")
            return False
    
    cliente = {
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": {
            'logradouro': logradouro,
            'numero': numero,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado
        }
    }
    
    dados['clientes'].append(cliente)
    
    with open('clientes_contas.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    input("\nCliente cadastrado com sucesso!")
    return True


def listar_clientes():
    dados = abrir_arquivo()
        
    if not dados['clientes']:
        print("\nNão há clientes cadastrados")
    
    tamanho_max_nome = max(len(cliente['nome']) for cliente in dados['clientes'])
    tamanho_max_cpf = max(len(cliente['cpf']) for cliente in dados['clientes'])

    print()
    print(f"{'Nome':<{tamanho_max_nome}} | {'CPF':<{tamanho_max_cpf}}")
    print("-" * (tamanho_max_nome + 3 + tamanho_max_cpf))  # linha de separação        
    for cliente in dados['clientes']:     
        print(f"{cliente['nome']:<{tamanho_max_nome}} | {cliente['cpf']:<{tamanho_max_cpf}}") # :< Joga pra esquerda
    print()
    
    input()
    

def excluir_cliente(cpf):
    dados = abrir_arquivo()

    indice_cliente = None
    for i, cliente in enumerate(dados['clientes']):
        if cliente['cpf'] == cpf.strip().replace("-", "").replace(".", ""):
            indice_cliente = i
            break
    
    if  indice_cliente is None:
        input(f"\nCliente com o CPF {cpf} não encontrado. Operação cancelada.")
        return False
    
    while True:
        confirma = input(f"\nOs dados do cliente {dados['clientes'][indice_cliente]['nome']} serão apagados. Deseja prosseguir? (S/N) ").strip().upper()[0]
        if confirma == 'S':
            del dados['clientes'][indice_cliente]
            
            with open('clientes_contas.json', 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
                
            input(f"\nCliente com o CPF {cpf} excluído com sucesso!")
            break
        elif confirma == "N":
            input("\nOperação cancelada.")
            break
        else:
            confirma = input("\nDigite apenas S (para confirmar) ou N (para cancelar)")


def cadastrar_conta_corrente(cpf):
    dados = abrir_arquivo()
    cliente_cadastrado = None

    for cliente in dados['clientes']:
        if cpf == cliente['cpf']:
            cliente_cadastrado = True
    
    ultima_conta = max([conta['conta_corrente'] for conta in dados['contas_correntes']])

    if cliente_cadastrado:   
        nova_conta = {
            'agencia': '0001',
            'conta_corrente': ultima_conta + 1,
            'cliente': cpf
        }   
    else:
        input(f"\nCliente com o CPF {cpf} não encontrado. Operação cancelada.")
        return False
        
    dados['contas_correntes'].append(nova_conta)
    
    with open('clientes_contas.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    input(f"\nConta Corrente nº {nova_conta['conta_corrente']} criada com sucesso!")


def listar_contas_correntes():
    dados = abrir_arquivo()
        
    if not dados['contas_correntes']:
        print("\nNão há Contas Correntes cadastradas.")

    tamanho_max_nome = max(len(cliente['nome']) for cliente in dados['clientes'])

    print(f'\nContas da Agência 0001:\n')
    print(f"Número | {'Conta':<{tamanho_max_nome}}")
    print("-" * (9 + tamanho_max_nome))  
        
    for conta in dados['contas_correntes']:
        for cliente in dados['clientes']: 
            if conta['cliente'] == cliente['cpf']:   
                print(f"{conta['conta_corrente']:<6} | {cliente['nome']:<{tamanho_max_nome}}")
    print()   

    input()


def excluir_conta_corrente(conta):
    dados = abrir_arquivo()

    numero_conta = None
    for i, conta_corrente in enumerate(dados['contas_correntes']):
        if conta_corrente['conta_corrente'] == int(conta):
            numero_conta = i
            break
    
    if  numero_conta is None:
        input(f"\nConta Corrente de nº {conta} não encontrada. Operação cancelada.")
        return False
    
    while True:
        confirma = input(f"\nOs dados da Conta Corrente {dados['contas_correntes'][numero_conta]['conta_corrente']} serão apagados. Deseja prosseguir? (S/N) ").strip().upper()[0]
        if confirma == 'S':
            del dados['contas_correntes'][numero_conta]
            
            with open('clientes_contas.json', 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
                
            input(f"\nConta Corrente de nº {conta} excluída com sucesso!")
            break
        elif confirma == "N":
            input("\nOperação cancelada.")
            break
        else:
            confirma = input("\nDigite apenas S (para confirmar) ou N (para cancelar)")


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3