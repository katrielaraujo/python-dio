from textwrap import dedent
from deposito import Deposito
from saque import Saque
from contaCorrente import ContaCorrente
from pessoaFisica import PessoaFisica

def filter_cliente(cpf,clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return
    
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filter_cliente(cpf,clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filter_cliente(cpf,clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filter_cliente(cpf,clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n=================== EXTRATO ===================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("================================================")

def criar_conta(numero_conta,clientes,contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente =  filter_cliente(cpf,clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação do conta encerrado! @@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

def listar_contas(contas):
   for conta in contas:
        print("*" * 100)
        print(dedent(str(conta)))

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filter_cliente(cpf,clientes)

    if cliente:
        print("\n@@@ Já existe cliente @@@")
        return
    
    nome = input("Informe o nome complete: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro,nro - bairros - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome,data_nascimento=data_nascimento,cpf=cpf,endereco=endereco)
    
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def menu():
    menu_str = """
=============== MENU =============== 
[d] Depósito 
[s] Sacar
[e] Extrato 
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair\n=> """
    print(dedent(menu_str))
    opcao = input()
    return opcao
