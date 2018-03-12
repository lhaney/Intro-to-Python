def menu():
    print "___________________________________________________"
    print "|                                                 |"
    print "|     Welcome to the Big Bank                     |"
    print "|                                                 |"
    print "|     To make a transaction try the following     |"     
    print "|                                                 |"
    print "|     1) Deposit                                  |"
    print "|     2) Withdrawl                                |"
    print "|     3) View balance                             |"
    print "|     4) Exit Big Bank program                    |" 
    print "|_________________________________________________|"
    return input ("Choose a transaction option: ")

def deposit(balance):
    deposit = input("Select deposit amount: ")
    deposit = float(deposit)
    balance = deposit + balance
    balance = float(balance)
    print "You have successfully deposited" ,deposit, "dollars into your account"
    print
    bank_balance(balance)
    return balance                

def withdrawl(balance):
    withdrawl = input("Select withdrawl amount: ")
    withdrawl = float(withdrawl)
    if withdrawl <= balance:
        balance = balance - withdrawl
        balance = float(balance)
        print "You have: $" ,balance, "remaining in your acount"
        bank_balance(balance)
        return balance
    else:
        print "you cannot have negative balance"
def bank_balance(balance):
    print "Balance: $" ,balance
    return balance

balance = 0
balance = float(balance)
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        balance = deposit(balance)
    elif choice == 2:
        balance = withdrawl(balance)
    elif choice == 3:
        balance = bank_balance(balance)
    elif choice == 4:
        loop = 0
    else:
        print "That was not an option"

print "Thank you for doing business with us"
