'''
Eamon Lee
Scoring code
This is code for a program that calculates the averages of the class
3/9/18
'''

#defines a variable to store the averages
average=0.0

#runs the amount of trials defined by num_students
for j in range (0,3):
    
    #asks user for name of a student
    name=str(raw_input("What is your name?"))
    
    #asks student for 1st 2nd and 3rd score
    s1=int(raw_input("What is your first score?"))
    s2=int(raw_input("What is your second score?"))
    s3=int(raw_input("What is your third score?"))
    
    #finds the average for the student's score
    average=((s1+s2+s3)/3)+average
    
    #prints the average score for the student
    print name,"Your average score is:", (s1+s2+s3)/3
    
    #checks student average
    if s1+s2+s3/3 > 70:
        print "Nice work!"
    elif (s1+s2+s3)/3 < 70:
        print "Study harder to increase your average"
        
    #checks the 1st score
    if s1 < 70:
        print "Redo test one"
    else:
        print "Nice work on test one"
        
    #checks the 2nd score
    if s2 < 70:
        print "Redo test two"
    else:
        print "Nice work on test two"
        
    #checks the 3rd score 
    if s3 < 70:
        print "Redo test three"
    else:
        print "Nice work on test three"
        
#prints the class average once the for loop is done
print "The class average is",average/3

