'''
Eamon lee and Ben GB
Ploting program
Writes a set of points onto a text file then reads in and plots it
3/22/18
'''

import matplotlib
from matplotlib import pyplot as plt

#creates a file called swamp.txt and opens it to write
filename=open('swamp.txt','w')

#writes a txt file with the following data points
filename.write('5,10'+'\n')
filename.write('15,20'+'\n')
filename.write('3,6'+'\n')
filename.write('9,16'+'\n')
filename.write('40,50'+'\n')

#this closes the txt file
filename.close()

#reopens the txt file to read
filename=open('swamp.txt','r')

#creates a list called x
x=[]

#creates a list called y
y=[]

#this for loop appends the values in the txt file to the x and y array
for line in filename:
    
    #appends the numbers in the 0 index to x
    x.append(float(line.split(',')[0]))

    #appends the numbers in the 1 index to y
    y.append(float(line.split(',')[1]))

#this prints the x and y array
print x
print y

#plots the x and y array with the style within the string
plt.plot(x,y, 'r1')

#labels the x axis with "numbers"
plt.xlabel('numbers')

#labels the y axis with "more numbers"
plt.ylabel('more numbers')

#shows the user the plot
plt.show()
