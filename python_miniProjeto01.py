BASE_VALUE = 0.0
LIMIT_VALUE = 500.0

user = "Gui"
balance = 1000.0
number_drawals = 0
withdrawal_amount = 0.0
DAILY_LIMIT = 3
statement_string = "Bank statement: "

def statement():
    print(f"{statement_string} \nBALANCE: R$ {balance}".replace(".",","))

def deposit(value):
    global statement_string,balance

    if value > BASE_VALUE:
        statement_string += f"\ndeposit: R$ {value}"
        balance += value
    else:
        print("Invalid amount")

def withdrawal(value):
    global statement_string, balance, number_drawals,withdrawal_amount

    if value > BASE_VALUE and number_drawals < DAILY_LIMIT:

        if (withdrawal_amount+value) < LIMIT_VALUE and value <= balance :
            withdrawal_amount+=value
            balance -= value
            number_drawals += 1
            statement_string += f"\nwithdrawal: R$ {value}"
        else:
            print("AMOUNT OF LIMIT")

    else:
        print("LIMIT OF DRAWALS DAILY")



menu = """

[d] Deposito
[s] sacar
[e] extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        value = float(input("Valor deposito: "))
        deposit(value)
    elif opcao == "s":
        value = float(input("Valor Saque: "))
        withdrawal(value)
    elif opcao == "e":
        statement()
    elif opcao == "q":
        break
    else:
        print("Invalid opcao")