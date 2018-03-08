'''
Eamon Lee
Hangman code
Runs a game of hangman using a random word from the list below
3/1/18
'''

#this imports the module for random chance
import random

#this is the word list that can be changed at anytime these are the words used for the game
my_dict={'chunky':'------', 'disobey':'-------', 'grand':'-----',
         'diplomacy':'---------', 'hostage':'-------', 'filter':'------',
         'morsel':'------', 'below':'-----', 'block':'-----', 'guard':'-----', 
         'melt':'----', 'danger':'------', 'more':'----', 'red':'---',
         'joy':'---', 'stick':'-----', 'focus':'-----', 'blunder':'-------',
         'jade':'----', 'fairy':'-----', 'tale':'----'}

#selects a random key from the list
rand_word=random.choice(my_dict.keys())

#establishes the amount of lives the player has this can aslo change at anytime
lives=6

#this dictionary asigns a number to a ascii picture
ascii_lives={
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

#intro prints the hidden version of the random word
print "Welcome to the hangman videogame"
print "Your word is",my_dict[rand_word]

#this creates an empty list for each guessed letter
guesses=[]

#main while loop most of the program exists in here
#this loop is the code for each round
#as long as this loop is true the game will continue
while True:

    #this asks the user for a guess
    guess=raw_input("Guess a letter")

    #if the guess is upper case this will turn it lower case so it can be checked against the key
    if guess==guess.upper():
        guess=guess.lower()
    else:
        print ' '

    #Finds the index of the guess in the key
    ind=rand_word.find(guess)

    #if the find command does not find the guess in the key it will return a -1
    #if this happens it will subtract 1 from lives
    if ind==-1:
        lives=lives-1
        print "Sorry wrong letter"

    #if the guess is found in guesses you will also lose a live
    elif guess in guesses:
        lives=lives-1
        print "Sorry you have already used this letter"

    #if the loop reaches this point the guess is inside the key and is correct
    #this prints the guess and dashes before the guess and after the guess
    #this the redefines the hidden word as the hidden word + the guess
    else:
        guesses.append(guess)
        my_dict[rand_word]=(my_dict[rand_word][:ind]+guess+my_dict[rand_word][ind+1:])

    #this will terminate the code when the player has no more lives
    if lives==0:
        print "Out of lives so you lose"
        break

    #this terminates the code when the hidden word = the key
    if rand_word==my_dict[rand_word]:
        print "Great job you win!"
        break

    #this prints the amount of lives, the hidden word and the guesses
    print my_dict[rand_word]
    print ascii_lives[lives]
    print ' '.join(guesses)
