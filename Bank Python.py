balance = 1000

while True:
    print "----------------------------------"
    print "Hello, welcome to QuickBanker ATM."

    print "Press (W) to Withdrawal"

    print "Press (D) to Deposit"
        
    print "Press ($) to See balance"
    print "----------------------------------"
    
    selection=raw_input('Please select - Withdrawal / Deposit / Balance?')
    if selection=='W'or selection=='Withdrawal':
        withdrawal = int(raw_input("How much would you like to Withdrawal? $10 / $20 / $50 / $100"))
        if withdrawal==10:
            if withdrawal>balance:
                print 'Sorry, you are poor lol'
            else:
                print '$10 successfully withdrawaled from account'
                balance = balance - 10
            elif withdrawal==20:
                if withdrawal>balance:
                    print 'Sorry, you are poor lol'
                else:
                    print '$20 successfully withdrawaled from account'
                    balance = balance - 20
            elif withdrawal==50:
                if withdrawal>balance:
                    print 'Sorry, you are poor lol'
                else:
                    print '$50 successfully withdrawaled from account'
                balance = balance - 50
            elif withdrawal==100:
                if withdrawal>balance:
                    print 'Sorry, you are poor lol'
                else:
                    print '$100  successfully withdrawaled from account'
                balance = balance - 100
                else:
                    print 'Err0r'
    elif selection=='D'or selection=='Deposit' or selection=='d':
        deposit = int(raw_input("How much would you like to Deposit? $10 / $20 / $50 / $100"))
        if deposit==10:
            print '$10 successfully deposited to account'
            balance = balance + 10
        elif deposit==20:
            print '$20 successfully deposited to account'
            balance = balance + 20
        elif deposit==50:
            print '$50 successfully deposited to account'
            balance = balance + 50
        elif deposit==100:                  
            print '$100  successfully deposited to account'
            balance = balance + 100
        else:
            print 'Err0r'
    elif selection=='$' or selection=='Balance':
        print 'Your current balance is:',balance,'dollars.'
  


    

    
        
