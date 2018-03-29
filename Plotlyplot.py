#Milo's code

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

filename=open('schoolscsv.csv','r') #open the file to read
x=[] 
y=[]
s=[]
for i,line in enumerate(filename): #for loop with line equal to the things in each line
        row=line.split(',') #create a list strings, with no commas
        x.append(row[0]) #everything in the first row 
        y.append(row[1]) #everything in the second row
        s.append(row[2]) #everything in the third row
s=map(lambda t: int(t.strip("\n")),s) #remove the line breaks and turn into an int
c=['blue'] #first item is blue
for i in range(1,len(x)): #rest are green
        c.append('green')
plt.scatter(x,y,s=s,c=c) #make a plot with the size of each dot equal to the list s
plt.xlabel('Proficiency') #label the x axis
plt.ylabel('Percent chronically absent') #label the y axis
plt.title('Size of dot correlates with percentage low income students, blue is state avg') #subtitle
plt.suptitle('Do schools with bad attendence perform worse?', fontsize=18) #title
plt.show() #show the plot
filename.close() #close the file
