'''
this is a CSV data reader coded by Selina Yang with inspirations from Laura Haney's example code
'''
import matplotlib #these  imports the ploting devices 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
matplotlib.rcParams.update({'font.size':8})

filename=open('alltablesGEcrops.csv','r') #this opens up the CSV file
xus=[] #this sets up a space for adding in x  values
yus=[] #this sets up a space for adding in x  values
for line in filename: #this loops the code reading device just enough times to let it read all the data wanted 
    if line[0:5]=='State': #this skips the title line of the CSV so that python would know to skip it
        continue
    else: #this is the actual reading of the code
         a=line.split(',') #this is to tell python to not consider the ',' as part of a value
         if a[0]=='U.S.' and a[1]=='Corn' and a[3]=='All GE varieties': #this is to tell python to look for specific information of interest
             try: 
                 yus.append(float(a[6])) #this adds y values from the colume that contains the information of interest into the blank space set up previously
                 xus.append(float(a[4])) #this adds x values from the colume that contains the information of interest into the blank space set up previously
             except ValueError: #this prevents python from running into infinite loop or stuck
                 continue
filename.close() #this closes the file
#this is the plotting part of the code
years=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017] #these are the years I am specially interested in
fig, ax = plt.subplots()
ax.set_xticks(years) #these sets the the steps for the bar graph
plt.plot(xus,yus,c='b') #this plots the line graph
plt.bar(xus,yus) #this plots the bar graph
plt.ylabel('Percentage of GE corns planted in US',multialignment='center') #this sets the label for y axis
plt.xlabel('Year') #this sets the label for x axis
plt.show() #this displays the data
