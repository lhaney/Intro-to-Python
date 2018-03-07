#This code was designed by Rory and Jaegar 
'''
Hangman Code
'''
#These are the templates for the different stages of the hanging
hangman={6:'''
   +---+
   |   |
       |
       |
       |
       |
 =========''',5:'''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''',4:'''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''',3:'''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''',2:'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''',1:'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''',0:'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========='''}
#Makes the chosen word random
import random
#The Word List
word_list=['expansion','firecracker','divine','federal','center','haunt','crisis','star','portrait','grieving','gargoyle','holding','focus','disease','minimal','horseradish','amongst','nitro','feast','church','heroic','condemned','cow','chaos','Dylan','bliss','bet','hangman','melt','lizard','abyssal','hamster','Sequoyah','robbery','fierce','sad','hidden','governor','bananas','damage','average','flap','firm','insurance','dancer','airtight','wilderness','believable','disfigurement','gripping','Minecraft','conquest','blunt','pierce','purple','piece','sonic','mystery','random','delight','bring','igunana','proposal','pound','gripping','hogwash','beeswax','horrific','fracture','company','coal','corrosive','grand','plantation','fictional','bachelor','content','ladybug','amuse','lavender','blindly','fossil','assassin','sink','gurgle','data','possess','elaborate','evectional','four','depression','ninja','bittersweet','perfume','book','iPhone','creative','Roblox','eerie','ferment','degeneration','discipline','contest','gravitational','computation','analyst','bit','sparrow','sewage','Exorcist','believer','carnivore','audacity','yeti','Fafnir','Diablo','Ronnie','Reaper','Ditto','Bootleg','Ireland','Mirage']
#Sets the word you guess to a random word from the above list
my_word=random.choice(word_list)
#Here to provide a stand-in for the original word, which we do not want to change. This makes a changeable variable
that_word=my_word
#Turns word into list
my_list=list(my_word)
#Provides the dashes
hidden=('_'*len(my_word))
hiddenls=list(hidden)
#You are not a cat, who has nine lives. In hangman you have only six.
Lives=6
#Prepares a list of letters used
used_list=[]

print 'Welcome to Hangman!'
print 'Your word is '+hidden
#Keeps the game going until conditions are met.
while True:
    #Provides a string form for used_list
    used_string=', '.join(used_list)
    #How you enter a letter
    letter=raw_input('Enter a letter: ')
    #Checks for if a letter is in the word
    ind=that_word.find(letter)
    #Checks for multiple uses
    inx=used_string.find(letter)
    try:
        #Prevents numbers
        val = int(letter)
        print "Numbers are not in hangman. Lose two lives"
        Lives=Lives-2
        #Prevents Negative lives
        if Lives<0:
            Lives=0
        else:
            print 'You have ',Lives,'lives left.'
            #Updates you on progress
            print hangman[Lives]
            print hidden
            print 'Here are the letters you have used: '+', '.join(used_list)
            #returns you to the While True
            continue
    except ValueError:
        #Prevents inputs with more than one letter
        if len(letter)>1:
            print 'Only Enter One Letter Please'
            continue
        else:
            #Prevents errors due to variations in case
            if letter==letter.upper():
                letter=letter.lower()
            elif letter in my_list:
                #For if letter is there
                for t in range(0,my_word.count(letter)):
                    #If letter was used
                    if ind==-1:
                        Lives=Lives-1
                        if Lives<0:
                            Lives=0
                        print 'LETTER ALREADY USED'
                        print 'You have ',Lives,'lives left.'
                        print hangman[Lives]
                        print hidden
                        print 'Here are the letters you have used: '+', '.join(used_list)
                    else:
                        #If letter is correct, but not yet used
                        hiddenls[ind]=letter
                        hidden=''.join(hiddenls)
                        that_word=(that_word[:ind]+'_'+that_word[ind+1:])
                        print 'You have ',Lives,'lives left.'
                        print hangman[Lives]
                        print hidden
                        used_list.append(letter)
                        print 'Here are the letters you have used: '+', '.join(used_list)

                                        
            else:
                #If the letter is wrong, but already used
                if inx!=-1:
                    Lives=Lives-1
                    if Lives<0:
                        Lives=0
                    print 'LETTER ALREADY USED'
                    print 'You have ',Lives,'lives left.'
                    print hangman[Lives]
                    print hidden
                    print 'Here are the letters you have used: '+', '.join(used_list)
                else:
                    #If the letter is wrong, but not yet used
                    Lives=Lives-1
                    if Lives<0:
                        Lives=0
                    print 'LETTER NOT FOUND'
                    print 'You have ',Lives,'lives left.'
                    print hangman[Lives]
                    print hidden
                    used_list.append(letter)
                    print 'Here are the letters you have used: '+', '.join(used_list)
#Checks if lives run out, and ends the While True
    if Lives==0:
        print hangman[Lives]
        print 'YOU LOSE...'
        break
#Checks if word is complete, and also ends the while True
    if hidden==my_word:
        print hangman[Lives]
        print 'YOU WIN!'
        print 'You had ',Lives,'lives left.'
        break
