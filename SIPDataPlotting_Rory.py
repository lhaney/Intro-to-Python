'''
SIP Data Plotting Code
BY RORY MARTIN
**Give Credit if you use my Code**
'''
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
filename=open('share-with-mental-health-or-development-disorder.csv','r')
x=[]
y=[]
z=[]
w=[]
for line in filename:
    if line[0:6]=='Entity':
        print 'Creating Plot[1/2]...'
        continue
    else:
        a=line.split(',')
        a2=float(a[2])
        a3=float(a[3])
        if a2<2011:
            continue
        else:
            if a[1]=='USA':
                x.append(a[0])
                y.append(a3)
                w.append(round(a3,3))
                z.append(a2)
filename.close()
filename1=open('share-with-depression.csv','r')
k=[]
l=[]
o=[]
p=[]
m=[]
for line in filename1:
    if line[0:6]=='Entity':
        print 'Creating Plot[2/2]...'
        continue
    else:
        b=line.split(',')
        b2=float(b[2])
        b3=float(b[3])
        if b2<2011:
            continue
        else:
            if b[1]=='USA':
                k.append(b[0])
                l.append(b3)
                o.append(round(b3,2))
                p.append(round(b3,3))
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
plt.xlabel('Year')
plt.title('People with Mental Disorders vs. People with Depression in the USA(2012-2016)')
plt.plot(z,y,c='g')
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
plt.show()


