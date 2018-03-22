'''
Plotting Code
BY RORY MARTIN
'''
#Imports the necessary mondules
import matplotlib
#makes it easier to refer to numpy
import numpy as np
#makes it easier to refer to pyplot, which is from matplotlib
from matplotlib import pyplot as plt
#Allows you to now edit the file within the code.
filename=open('testingtest.txt','w')
#Adds things to the txt file
filename.write('21,29'+'\n')
filename.write('4,12'+'\n')
filename.write('40,11'+'\n')
filename.write('21,41'+'\n')
filename.write('13,36'+'\n')
filename.write('50,32'+'\n')
filename.write('6,48'+'\n')
filename.write('0,40'+'\n')
filename.write('29,21'+'\n')
filename.write('42,38')
#Tells it to stop updating the file
filename.close()
#Reopens the newly updated file
filename=open('testingtest.txt','r')
#Sets the empty variables x and y
x=[]
y=[]
#Makes sure the code goes over every line in the text file
for line in filename:
    #Splits the numbers on the lines
    a=line.split(',')
    #Turns string to float
    a[0]=float(a[0])
    a[1]=float(a[1])
    #Adds to variable x
    x.append(a[0])
    #Adds to variable y
    y.append(a[1])
#Labels the y axis of the Plot
plt.ylabel('y')
#Labels the x axis of the Plot
plt.xlabel('x')
#Creates red dotted lines placed according to x and y variables
plt.plot(x,y,'r--')
#Creates blue dots placed according to x and y variables
plt.plot(x,y,'bo')
#Opens the plot
plt.show()
    
#Closes the text file again
filename.close()

