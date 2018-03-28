import random

print '''
Welcome to Hangman version 1.1.
In this version, you will only find words special to the Harry Potter series.
Here are the things you might want to keep in mind:
1) This game is not case sensitive (accepts both caps and lower case letters)
2) Any type of numbers should not be correct and will be considered wrong.
3) This version can currently render 1 letter at a time (do not try to enter a word even if it might be correct.)
4) Your objective is to guess the word before your lose all your chances to guess. (# of chances depended on the word length)
Have fun and be excited about the new update.
'''
a=["lumos", "ronald","acidpops","alchemy","Aconite","Doxy","Dragon","Newt","Ghoul","Giant","Gnomes","Grim","Gurg","Patronus","Phoenix","Portkey","Relashio",]
a=random.choice(a)
a=a.lower()
b=len(a)
n='-'*b 
print n
while b>0:
        if n==a:
            print "You Win!","the word is:",a
            break
        else:
            m=str(raw_input('guess a letter'))
            print "your left guess # is", b-1
            m=m.lower()
            ind=a.find(m)
            if ind== -1:
                print "try again"
                b=b-1
                continue
            else:
                a=a
                print n[:ind]+m+n[ind+1:]
                n=n[:ind]+m+n[ind+1:]
if b==0:
    print "the word is", a
    print "----------- GOOD LUCK NEXT TIME------------"
