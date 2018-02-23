for i in range(0,3): #do this 3 times
    name= raw_input('Name of Student?') #name
    score1= float(raw_input('Test Score 1?')) #score 1
    score2= float(raw_input('Test Score 2?')) #score 2
    score3= float(raw_input('Test Score 3?')) #score 3
    average = (score1+score2+score3)/3 #take an average
    print 'Student Name:' ,name #print their name
    print 'Average Score:',average #and average
    if average <= 2: #if the average is less then 2
            if score1 <= 2: #if score 1 is below 2, be ready to print 1
                v1 = "1 "
            else:
                del v1
            if score2 <= 2: #if score 2 is below 2, be ready to print 2
                v2 = "2 "
            else:
                del v2            
            if score3 <= 2: #if score 3 is below 2, be ready to print 3
                v3 = "3 "
            else:
                del v3
            print "Tell this dumb guy to redo his tests! He needs to redo test(s) "+v1+''+v2+''+v3 #print the ones to replace
        
    else:
        continue
