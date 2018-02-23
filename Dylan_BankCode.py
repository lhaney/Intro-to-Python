init_balance = 1000
def deposit(balance,c):
   init_balance=balance+c
   return balance
a=raw_input('would you like to make a deposit or withdraw money?')
if a=='withdraw':
    b=int(raw_input( 'how much would you like to withdraw?') )
    if b>1000:
        print 'error you can not have a negative balance'
    else:
        print 'your balance is ', balance-b 
elif a=='deposit':
  c=int(raw_input('how much would you like to deposit?') )
  print 'your balance is ', deposit(balance,c)
else:
    print 'error'
print balance
