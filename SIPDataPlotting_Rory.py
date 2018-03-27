'''
SIP Data Plotting Code
BY RORY MARTIN
**GIVE CREDIT IF YOU USE A PORTION OF THE CODE**
'''
#Imports the necessary mondules
import matplotlib
#makes it easier to refer to numpy
import numpy as np
#makes it easier to refer to pyplot, which is from matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
#Allows you to now edit the file within the code.
filename=open('share-with-mental-health-or-development-disorder.csv','r')
#Creates the variables x,y,and z
x=[]
y=[]
z=[]
w=[]
#Makes sure the code goes over every line in the excel file
for line in filename:
    #Skips the first line
    if line[0:6]=='Entity':
        print 'Creating Plot[1/2]...'
        continue
    else:
        a=line.split(',')
        #Turns string to float
        a2=float(a[2])
        a3=float(a[3])
        #Adds to variable x
        if a2<2011:
            continue
        else:
            if a[1]=='USA':
                x.append(a[0])
        #Adds to variable y
                y.append(a3)
                w.append(round(a3,3))
        #Adds to variable z, but also makes it a reasonable amount
                z.append(a2)
#Allows labels variable to be different from data variable
#Labels the y axis of the Plot
filename.close()
filename1=open('share-with-depression.csv','r')
k=[]
l=[]
o=[]
p=[]
m=[]
for line in filename1:
    #Skips the first line
    if line[0:6]=='Entity':
        print 'Creating Plot[2/2]...'
        continue
    else:
        b=line.split(',')
        #Turns string to float
        b2=float(b[2])
        b3=float(b[3])
        #Adds to variable x
        if b2<2011:
            continue
        else:
            if b[1]=='USA':
                k.append(b[0])
        #Adds to variable y
                l.append(b3)
                o.append(round(b3,2))
                p.append(round(b3,3))
        #Adds to variable z, but also makes it a reasonable amount
                m.append(b2)
filename1.close()
filename=open('share-with-mental-health-or-development-disorder.csv','r')
filename1=open('share-with-mental-health-or-development-disorder.csv','r')

fig,ax=plt.subplots()

ax=plt.subplot(2,1,1)
fmt = '%.2f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(yticks)
for i, txt in enumerate(w):
    ax.annotate(txt, (z[i],y[i]))
plt.ylabel('Percentage')
#Labels the x axis of the Plot
plt.xlabel('Year')
#Title
plt.title('People with Mental Disorders vs. People with Depression in the USA(2012-2016)')
#Creates red dotted lines placed according to y and z variables
plt.plot(z,y,c='g')
#Creates blue dots placed according to y and z variables
plt.scatter(z,y,c='g')
#plt.subplot(2,1,2)
ax1=plt.subplot(2,1,2)
fmt = '%.2f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax1.yaxis.set_major_formatter(yticks)
for i, txt in enumerate(p):
    ax1.annotate(txt, (m[i],l[i]))
plt.ylabel('Percentage')
plt.xlabel('Year')
plt.plot(m,l,c='r')
plt.scatter(m,l,c='r')
#Opens the plot
plt.show()
            
#Closes the excel file again


