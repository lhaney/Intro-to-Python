#import modules nessary to plot
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation

#creating a blank canvas and setting up the canvas to the favored position and size
fig=plt.figure(figsize=(6,6),facecolor='#080888')#face color is the screen color. some names work, but html color codes always work
ax=fig.add_axes([0,0,1,1],frameon = False, aspect=1) #[latitude, longtitude,side length, side length](<--out of 1)

#setting up variables
n=50 #50 things
size_min=10 #the minimum size of the things
size_max=4000 #the maximum size of the things
p = np.random.uniform(0,1,(n,2)) #this is the position of the 50 things (pick randomly according to the normal distibution distribution)

#creating the bases of animation

#sets up the edge color of the things
c=np.ones((n,4))*(0,0,0,1) #this is the border colors of the 50 things (Red(R), Blue(B),Green(G), opacity(Alpha))
c[:,0]=np.linspace(0,1,n)#v
c[:,1]=np.linspace(0,1,n)#v
c[:,2]=np.linspace(0,1,n)#make the border line color is random
c[:,3]=np.linspace(0,1,n)#make sure the opacity is random for each thing but all visible on computer screens
s=np.linspace(size_min,size_max,n)#this is the sizes of the 50 things (randomized)


#sets up the body color of the things
bc= np.ones((n,4))*(0,0,0,1)#this is the body colors of the 50 things (Red(R), Blue(B),Green(G), opacity(Alpha))
bc[:,0]=np.linspace(0,1,n)#v
bc[:,1]=np.linspace(0,1,n)#v
bc[:,2]=np.linspace(0,1,n)#make sure the body color is random
bc[:,3]=np.linspace(0,1,n)#make sure the opacity is random for each thing but all visible on the computer screen

#sum up all above settings
scat=ax.scatter(p[:,0],p[:,1],s=s,lw=1, #this creates a scatterplot to mark the position of the figures
                edgecolors=c,facecolors=bc)

#ensure limts are within 0 and 1 and get rid of the borders of the plot
ax.set_xlim(0,1),ax.set_xticks([])
ax.set_ylim(0,1),ax.set_yticks([])

#animating the changes
def update(frame):
      global p,c,s
      c[:,3]=np.maximum(1,c[:,3]-1.0/n) #makes everything more transparent each time
      s+=(size_max-size_min)/20 #makes everything bigger each time

      #Reset specific things relative to frame numer
      i=frame%50
      p[i]=np.random.uniform(0,1,2) #replacing position of one item and repositioning it
      s[i]=size_min #replacing size of one item to the smallest size
      c[i,3]=1 #makes the one item to maximum opacity


      #updates the scattering object and return the modifies object
      scat.set_edgecolors(c)
      scat.set_sizes(s)
      scat.set_offsets(p)
      return scat,

animation=animation.FuncAnimation(fig,update,interval=20) #put together the animation

plt.show() #show the animation
