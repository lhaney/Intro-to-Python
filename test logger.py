'''
Jaegar and Selina programed this code to help teachers log their students'
score as well as calculate the average score of individuals and for the whole class.
It could also be used by students to figure out what their average
score is and which test they would want to wotk on if they want to improve their score.
'''
j=0 
for i in range (0,3): #3 is the number of students you would like to log in this log.
    name=str(raw_input("enter name"))
    a= int(raw_input("what's your first score?"))
    b= int(raw_input("what's your second score?"))
    c= int(raw_input("what's your third score?"))
    j=(( a+b+c)/3)+j #3 is the number of students you would like to log in this log.
    print name, ",your average score is", (a+b+c)/3 #3 is the number of tests you would like to log in this log.
    if (a+b+c)/3 > 70: #80 is the average score you expect students to have in order to pass the course. #3 is the number of tests you would like to log in this log.
            print "nice job"
    elif (a+b+c)/3 < 70: #80 is the average score you expect students to have in order to pass the course. #3 is the number of tests you would like to log in this log.
            print "work harder!"
    if a<70: #70 is the score you expect students to have in order to pass the certain test. 
        print "you should redo test 1"
    else:
            print 'great job on test 1!'
    if b<70:#70 is the score you expect students to have in order to pass the certain test. 
            print "you should redo test 2"
    else:
            print 'great job on test 2!'
    if c<70:#70 is the score you expect students to have in order to pass the certain test. 
            print "you should redo test 3"
    else:
            print 'great job on test 3!'
print "the average score of the class is", j/3#3 is the number of students you would like to log in this log.
