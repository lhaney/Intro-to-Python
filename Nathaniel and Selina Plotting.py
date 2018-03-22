'''
Made by Nathaniel and Selina
Writes points in a text file and plots them on a graph
3/22/18
'''


import matplotlib
from matplotlib import pyplot as plt
import numpy as np
#creates a file
filename=open('array.txt','w')
#writes a series of numbers into it
filename.write('3,9'+'\n')
filename.write('12,56'+'\n')
filename.write('47,74'+'\n')
filename.write('91,29'+'\n')
#closes the file
filename.close()
#reopens the file to read
filename=open('array.txt','r')
#defines lists
xlist=[]
ylist=[]
for line in filename:
#adds numbers to a list
    xlist.append(float(line.split(',')[0]))
    ylist.append(float(line.split(',')[1]))
#prints lists
print xlist
print ylist
#plots list
line=plt.plot(ylist,xlist)
#changes color to yellow)
plt.setp(line, 'color', 'y',)
#opens the plot
plt.show()
