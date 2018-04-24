'''
Eamon Lee
Sip Graphing Code
This code reads a csv file and writes the data to lists
then graphs the data in a plot
4/24/18
'''

#imports matplotlib for ploting
import matplotlib
from matplotlib import pyplot as plt

#opens the csv file
filename=open('DPSCS.csv', 'r')

#creates multiple lists that the data can be appended to another one for the dates
b=['99','00','01','02','03','04','05',
   '06','07','08','09','10','11','12']
x=[]
y=[]
z=[]

#this reads each line the appends the data to the lists
for line in filename:

    #this is here to skip the title
    if line[0]=='F':
        continue
    else:
        x.append(line.split(',')[0])
        y.append(line.split(',')[1])

#prints each list
print x
print y

#allows the x and y axis to be different than the data
fig,ax=plt.subplots()

#sets the x axis as b
ax.set_xticklabels(b)

#plots the data as blue dashes
plt.plot(x,y,'b--')

#adds a y label
plt.ylabel('Recitivism Rates Among Prisoners')

#adds a x label
plt.xlabel('Year')

#adds a title
plt.title('Recitivism Rates Over the Years')

#shows the graph
plt.show()
