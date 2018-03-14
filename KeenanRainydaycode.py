question=raw_input("Are you in room 23?")
if question=="Yes" or question=="yes" or question=="y":
    print "Okay, im sorry but you cannot eat in room 23"
elif question=="No" or question =="no" or question=="n":
    print "Okay, next question."
    question1=raw_input("Is it raint day schedule?")
    if question1=="Yes" or question1=="yes" or question1=="y":
        print "Okay, you are allowed to eat inside the classroom!"
    elif question1=="No" or question1=="no" or question1== "n":
        print "Okay, next question."
        question2=raw_input("Do you have permission from a teacher?")
        if question2=="Yes" or question2=="yes" or question2== "y":
            print "Okay, you are allowed to eat inside the classroom!"
        elif question2== "No" or question2=="no" or question2== "n":
            print "Im sorry but you are not allowed to eat inside the classroom!"
            exit()
        else:
            print "error"
    else:
        print "error"
else:
    print "error"
