'''
Eamon Lee
Classroom Code
This code checks which rooms students can eat in given their
location and circumstance
3/14/18
'''

#starts a while loop for answers that are not yes or no
while True:
    #asks if it is a rainy day
    a=str(raw_input("Is today rainy day schedule?"))
    
    if a=='yes':
        #tells user where they can eat during rainy day
        print "You can only eat in rooms 3 and 4"
        #ends program
        break
    
    elif a=='no':
        
        #asks if the user is in a carpeted room
        b=str(raw_input("Are you in a carpeted room?"))
        
        if b=='yes':
            
            #asks if they are with a teacher
            c=str(raw_input("Are you meeting with a teacher?"))
            
            if c=='yes':
                #tells the user they can eat in a carpeted room
                print "You can eat in any room with permission from a teacher"
                #ends program
                break
            
            elif c=='no':
                #tells the user they cannot eat in a carpeted room
                print "You cant eat in a carpeted room without a teacher"
                #ends program
                break
            
            else:
                #tells the user to answer with a yes or no
                print "Please answer with a yes or no"
                
        elif b=='no':
            #tells the user where they can eat
            print "You can eat in rooms 3 and 4"
            #ends program
            break
        
        else:
            #tells the user to answer with a yes or no
            print "Please answer with a yes or no"
    else:
        #tells the user to answer with a yes or no
        print "Please answer with a yes or no"              
                        
