'''

'''
hangman={6:'''
    +-------+
     |         |
              |
              |
              |
              |
              |
  =======''',5:'''
    +-------+
     |          |
     0         |
                |
                |
                |
                |
  =======''',4:'''
    +-------+
    |          |
    0         |
    |          |
               |
               |
               |
    ======''',3:'''
    +-------+
    |          |
    0         |
   / | \       |
               |
               |
               |
    ======''',2:'''
   +-------+
    |          |
    0         |
   / | \       |
      \        |
               |
               |
    ======''',1:'''
    +-------+
    |          |
    0         |
   / | \       |
   /  \        |
               |
               |
    ======'''}
''' Dylan Cugley
This code is supposed to choose a random word that is chef themed.
Then it creates a variable that is the same length as the word but in
dashes. Then it asks for the user to guess a letter. It then looks through
the word to check if it has that letter until it hasn't found anymore of
that letter. Then it replaces the letter with that dash and the varible
of dashes has the dash replaced with the letter. If it does not find
the letter it removes one from the varible called lives. If lives ends up
equaling zero than it will break the code. When the varible dash equals
the original world, it will end the loop and print 'you win'
This was last edited on 3/13/2018'''
import random
word_list='cubano', 'jon_favreau' , 'beingnets', 'food_truck', 'chef', 'el_jefe','food_blogger'
word= random.choice(word_list)
dash='_'*len(word)
lives=6
findword=word
findlist=list(findword)
print dash
while dash!=word:
    if lives>=1:
        a=raw_input('enter a letter: ')
        a=a.lower()
        ind=findword.find(a)
        newword=word
        if ind==-1:
            lives=lives-1
        while ind!=-1:
            for i in range(0,word.count(a)):
                dash=dash[:ind]+a+dash[ind+1:]
                newword=newword[:ind]+'_'+newword[ind+1:]
                ind=newword.find(a)
                findlist.remove(a)
                print dash
        #elif ind==-1:
        #print 'guess another letter'
        if ind==-1:
            print 'guess another letter'
       # lives=lives-1
        print 'lives= ',lives
        if lives==0:
            print 'game over'
print 'you win'
    #    print dash[:ind]+a+dash[ind+1:]
       # if ind!=-1:
           #     print dash[:ind]+a+dash[ind+1:]
              #  dash=dash[:ind]+a+dash[ind+1:]
                    

                
