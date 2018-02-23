b = 0.0 #initial balance is 0
yes = ["y", "Y", "yes", "Yes"] #things accepted as a yes in the code
no = ["n", 'N', 'no', "No"] #things accepted as a no in the code
d = ["deposit", "Deposit", "d", "D"] #things accepted as a deposit in the code
w = ["Withdraw", "withdraw", "Withdrawl", "withdrawl", "w", "W"] #things accepted as a withdrawl in the code
h = ["Help", "help", "h", "H"] #things accepted as help in the code 

def hel(): #The help menu code 
    print ""
    print "Welcome to this work of art! If you are confused, here is the syntax for the code!"
    print ""
    print "If you want to make a transaction, please type yes, Yes, y, or Y."
    print ""
    print "If you want to make a deposit, please type deposit, Deposit, d, or D."
    print ""
    print "If you want to make a withdrawl, please type withdraw, Withdraw, withdrawl, Withdrawl, w, or W."
    print ""

def deposit(b): #The code will deposit an amount from your account
    try: #try to do this code
        d = float(raw_input("How much would you like to deposit?"))
        b = b + (d * 0.98) #Add the deposit
        print "Your balance is ",b #Print the balance
        return b #Set b to the value in the code
    except ValueError: #otherwise tell them to put in a number!
            print "Please put in a number! If you are confused, please type help, Help, h, or H in the transaction menu"

def withdraw(b): #The code that will withdraw an amount from your account
    try: #try to do this code
        w = float(raw_input("How much would you like to withdraw?")) #Make the amount you withdraw into a float
        if (b - w < 0): #If this would bring your account below 0 it will say you're broke
            print "We're sorry, but you're broke!"
        else: #otherwise subtract the amount from your account
            b = b - (1.02 * w)
            print "Your balance is ",b #Print the new balance
            return b #Set b to the value in the code
    except ValueError: #otherwise do this
            print "Please put in a number! If you are confused, please type help, Help, h, or H in the transaction menu"

        
while True:
    t = raw_input("Would you like to make a transaction?") 
    if t in yes: #If yes then ask if withdraw or deposit
        wd = raw_input("Would you like to make a deposit or a withdrawl?")
        if wd in w: #if deposit go to withdrawl code
            b=withdraw(b) #set b equal to the b from the withdraw code above
        elif wd in d: #if withdraw go to deposit code
            b=deposit(b) #set b equal to the b from the deposit code above
        else: #otherwise say you don't recognize
            print "We're sorry, we didn't recognize what you wrote! If you are confused, please type help, Help, h, or H in the transaction menu"
    elif t in h: #go to help menu
        hel()
    elif t in no: #if they say no end the code
        print "Have a great day!"
        break #end the loop
    else:
        print "We're sorry, we didn't recognize what you wrote! If you are confused, please type help, Help, h, or H"
