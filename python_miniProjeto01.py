import datetime

def create_user():
    user = {
        "name": input("Nome: "),
        "birthday": datetime.datetime.strptime(input("Data de Nascimento (dd-mm-yyyy): "), '%d-%m-%Y').date(),
        "CPF": input("CPF: "),
        "address": input("Endereco: ")
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

def add_user(user, users):
    users.append(user)

def print_statement(statement):
    for state in statement:
        print(state.replace('.',','))

def deposit(value, statement, account):
    if value > 0:
        statement.append(f"Deposito: R$ {value:.2f}")
        account["balance"] += value
    else:
        print("Valor inválido")

def validate_withdrawal(value, number_drawal, account):
    LIMIT = 500.0
    DRAWAL_LIMIT = 3

    insufficient = value < account["balance"]
    valid = value > 0
    withdrawal_limit = value <= LIMIT
    limit_drawal = number_drawal <= DRAWAL_LIMIT

    if insufficient:
        print("Saldo insuficiente")
    if valid:
        print("Valor inválido")
    if withdrawal_limit:
        print("Valor limite de saque")
    if limit_drawal:
        print("Superou o limite de saques diários")

    return not (insufficient or valid or withdrawal_limit or limit_drawal)

def withdrawal(value, statement, number_drawal, account):
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
    print(menu_str)

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
            deposit(value,statement, account)
        elif opcao == "s" and account is not None:
            value = float(input("Valor do saque: "))
            withdrawal(value,statement, number_drawal, account)
        elif opcao == "e" and account is not None:
            print_statement(statement)
        elif opcao == "q":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
