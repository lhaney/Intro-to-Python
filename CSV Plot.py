'''
Sample Data Plotting Code
BY RORY MARTIN
'''
#Imports the necessary mondules
import matplotlib
#makes it easier to refer to numpy
import numpy as np
#makes it easier to refer to pyplot, which is from matplotlib
from matplotlib import pyplot as plt
#Allows you to now edit the file within the code.
filename=open('sample_data.csv','r')
#Creates the variables x,y,and z
x=[]
y=[]
z=[]
#Makes sure the code goes over every line in the excel file
for line in filename:
    #Skips the first line
    if line[0]=='d':
        continue
    else:
        a=line.split(',')
        #Turns string to float
        a[1]=float(a[1])
        a[2]=float(a[2])
        #Adds to variable x
        x.append(a[0])
        #Adds to variable y
        y.append(a[1])
        #Adds to variable z, but also makes it a reasonable amount
        z.append(a[2]/1000)
#Allows labels variable to be different from data variable
fig, ax = plt.subplots()
ax.set_xticklabels(x)
#Labels the y axis of the Plot
plt.ylabel('Energy (In Thousands)')
#Labels the x axis of the Plot
plt.xlabel('Dates')
#Title
plt.title('Use the magnifying glass to zoom in on the points')
#Creates red dotted lines placed according to y and z variables
plt.plot(y,z,'r--')
#Creates blue dots placed according to y and z variables
plt.plot(y,z,'bo')
#Opens the plot
plt.show()
            
#Closes the excel file again
filename.close()

