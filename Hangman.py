'''
Hangman Code
'''
import random
word_list=['one','two','three','four','five']
my_word=random.choice(word_list)
that_word=my_word
my_list=list(my_word)
hidden=('_'*len(my_word))
hiddenls=list(hidden)
Lives=5

print 'Welcome to Hangman!'
print 'Your word is '+hidden
while True:
    letter=raw_input('Enter a letter: ')
    if letter==letter.upper():
        letter=letter.lower()
    if letter in my_list:
        for t in range(0,my_word.count(letter)):
            ind=that_word.find(letter)
            if ind==-1:
                Lives=Lives-1
                print 'LETTER ALREADY USED'
                print 'You have ',Lives,'lives left.'
            else:
                hiddenls[ind]=letter
                hidden=''.join(hiddenls)
                that_word=(that_word[:ind]+'_'+that_word[ind+1:])
        print hidden
    else:
        Lives=Lives-1
        print 'LETTER NOT FOUND'
        print 'You have ',Lives,'lives left.'
        print hidden
    if Lives==0:
        print 'You Lose...'
        break
    if hidden==my_word:
        print 'You Win!'
        break
       
