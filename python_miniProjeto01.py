import datetime
import textwrap

def create_user():
    name = input("Nome: ")
    birthday_str = input("Data de Nascimento (dd/mm/ano): ")
    birthday = datetime.datetime.strptime(birthday_str, '%d/%m/%Y').date()
    cpf = input("CPF: ")
    address = input("Endereço: ")
    
    user = {
        "name": name,
        "birthday": birthday,
        "CPF": cpf,
        "address": address
    }
    return user

def create_account(user, accounts):
    account = {
        "owner": user,
        "agency": "0001",
        "number_account": len(accounts) + 1,
        "balance": 0.0,
    }
    accounts.append(account)

def print_statement(statement,/,*,account):
    print(f"EXTRATO BANCARIO: AGENCIA:{account['agency']} CONTA:{account['number_account']}")
    print("RESPONSAVEL DA CONTA: "+account['owner']['name'])
    for state in statement:
        print(state.replace('.', ','))
    print(f"SALDO ATUAL: R$ {account['balance']}".replace('.', ','))

def deposit(value, statement, account,/):
    if value > 0:
        statement.append(f"Depósito: R$ {value:.2f}")
        account["balance"] += value
    else:
        print("Valor inválido")

def validate_withdrawal(value, number_drawal, account):
    LIMIT = 500.0
    DRAWAL_LIMIT = 3
    BASE_LIMIT = 0

    insufficient = value <= account["balance"]
    valid = value > BASE_LIMIT
    withdrawal_limit = value <= LIMIT
    limit_drawal = number_drawal <= DRAWAL_LIMIT

    if not insufficient:
        print("Saldo insuficiente")
    if not valid:
        print("Valor inválido")
    if not withdrawal_limit:
        print("Valor limite de saque")
    if not limit_drawal:
        print("Superou o limite de saques diários")

    return insufficient and valid and withdrawal_limit and limit_drawal

def withdrawal(*,value, statement, number_drawal, account):
    if validate_withdrawal(value, number_drawal, account):
        account["balance"] -= value
        number_drawal += 1
        statement.append(f"Saque: R$ {value:.2f}")

def print_menu():
    menu_str = """
[a] Entrar
[d] Depósito 
[s] Saque 
[e] Extrato 
[q] Sair\n=> """
    print(textwrap.dedent(menu_str))

def find_account(user, accounts):
    for acc in accounts:
        if user == acc["owner"]:
            return acc

def main():
    users = []
    accounts = []
    number_drawal = 0
    statement = []
    account = None

    while True:
        print_menu()
        opcao = input()
        if opcao == "a":
            user = create_user()
            if user not in users:
                users.append(user)
                create_account(user, accounts)
            account = find_account(user, accounts)
        elif opcao == "d" and account is not None:
            value = float(input("Valor do depósito: "))
            deposit(value, statement, account)
        elif opcao == "s" and account is not None:
            value = float(input("Valor do saque: "))
            withdrawal(value=value, statement=statement, number_drawal=number_drawal, account=account)
        elif opcao == "e" and account is not None:
            print_statement(statement,account=account)
        elif opcao == "q":
            break
        else:
            print("Opção inválida")

main()
