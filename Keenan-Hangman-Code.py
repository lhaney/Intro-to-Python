'''
Hangman Code
This code was finalized on March 13, 2018
Created and annotated by Keenan Cole
'''
import random
picture={
0:'''
    -+--+
     |  |
    \o/ |
     |  |
    / \ |
   -----+----
''',
1:'''
    -+--+
     |  |
    \o/ |
     |  |
      \ |
   -----+----
''',
2:'''
    -+--+
     |  |
    \o/ |
     |  |
        |
   -----+----
''',
3:'''
    -+--+
     |  |
    \o/ |
        |
        |
   -----+----
''',
4:'''
    -+--+
     |  |
    \o  |
        |
        |
   -----+----
''',
5:'''
    -+--+
     |  |
     o  |
        |
        |
   -----+----
''',
6:'''
    -+--+
     |  |
        |
        |
        |
   -----+----
'''}
w_list=['monkey','gorilla','giraffe','panther','hippo','zebra','elephant','gazelle','cheetah']
my_word=random.choice(w_list)
my_list=list(my_word)
invis=('-'*len(my_word))
invis_lists=list(invis)
lives=6
guesses=[]
#This part of the code here sets up the amount of lives the player has and the sets the word + its dashes (this is the dash '-') 
#This part also sets up the guesses so that players cannot repeat a guess or letter

print 'Welcome to Python Hangman!'
print 'Your Animal is '+invis
#This is the starting message for the game
while True:
    #This while true makes it so that anything inside it repeats until the code breaks/game ends
    guess=', '.join(guesses)
    #This is a string or text form for the guesses
    letter=str(raw_input('Guess a letter: '))
    #This allows the user to input a letter
    ind=my_word.find(letter)
    #This part checks to see if the letter is in the word and translates it into an index
    indx=guess.find(letter)
    #This bit checks to see if the letter has been used multiple times
    if letter==letter.upper():
    #This part of the code makes it so that the letters are always lowercase
        letter=letter.lower()
    elif letter in my_list:
    #This part of the code sees if the letter is in the word
        for t in range(0,my_word.count(letter)):
            if ind==-1:
            #This part of the code is if the letter has already been used
                lives=lives-1
                print 'This letter has been used already!'
                print 'You have ',lives,'lives left.'
                print picture[lives]
                print invis
                print 'Letters Used: '+', '.join(used_list)
            else:
            #This part of the code shows what happens when an unused correct letter is picken
                invis_list[ind]=letter
                invis=''.join(hiddenls)
                my_word=(my_word[:ind]+'_'+my_word[ind+1:])
                print 'You have ',lives,'lives left.'
                print picture[lives]
                print invis
                guesses.append(letter)
                print 'Letters used: '+', '.join(guesses)                                     
    else:
    #This part of the code prevents wrong letters from being repeated
        if indx!=-1:
            lives=lives-1
            print 'This letter has been used already!'
            print 'You have ',lives,'lives left.'
            print picture[lives]
            print invis
            print 'Letters used: '+', '.join(guesses)
        else:
        #This part of the code prevents
            lives=lives-1
            print 'Invalid letter!'
            print 'You have ',lives,'lives left.'
            print picture[lives]
            print invis
            guesses.append(letter)
            print 'Letters used: '+', '.join(guesses)
    if lives==0 or lives<0:
    #This part of the code analyzes the word to see if the player has lost and then ends the loop
        print picture[lives]
        print 'Sorry, You lose!'
        break
    if invis==my_word:
    #This part of the code analyzes the word to see if the player has won and then ends the loop
        print picture[lives]
        print 'Congrats, You win!'
        print 'Lives left:',lives,
        break
