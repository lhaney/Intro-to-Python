'''
File plot Code
This code was written and finalized by Keenan Cole and Dylan Cugley
3/22/18
'''
import matplotlib
from matplotlib import pyplot as plt
#These commands import all the things we will need to plot
keen=open('Keen.txt', 'w')
#This part of the code creates/opens the file in the 'write' mode
keen.write('1,1' + '\n')
keen.write('2,2' + '\n')
keen.write('4,4')
keen.close()
#This part of the code writes the numbers inside the file and then closes the file
keen=open('Keen.txt', 'r')
#This opens the file in 'read' mode
x=[]
y=[]
#This sets up the variables for the plot so we can categorize the numbers to plot them
for line in keen:
    x.append(float(line.split(',')[0]))
#This appends the left number of the line to 'X'
    y.append(float(line.split(',')[1]))
#This appends the right number of the line to 'Y'
print x
print y
plt.plot(x,y, 'r1')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
#Finally, this prints the numbers for each list and then plots it on the pyplot
