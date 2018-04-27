import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation

#New figure with white backround
fig = plt.figure(figsize=(6,6), facecolor='white')

#New axis over the whole figure, no frame and a a1:1 aspect ratio
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)

#Number of things
n=50
size_min=10
size_max=3000
P = np.random.uniform(0,1,(n,2))
#Positions
P = np.random.uniform(0,1,(n,2)) #---> List of numbers that are n numbers long and 2 elements wide

print P

#Colors
C = np.ones((n,4)) * (0,0,0,1)

F = np.ones((n,4)) * (0,0,0,1)

#Aplha color channel goes from 0 (transparent) to 1 (opacity)
#Takes the selected collumn and changes them into random numbers.
C[:,3] = np.linspace(0,1,n)


#Sizes
S = np.linspace(size_min, size_max, n)

print C

#Scatter Plot
scat = ax.scatter(P[:,0], P[:,1], marker='_', s=S, lw = 5,
                  edgecolors = C, facecolors=F)

#Ensure limits are [0,1] and remove ticks
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])

def update(frame):
    global P, C, S

    #Every thing is made more transparent    
    C[:,3] = np.maximum(1, C[:,3] - 1.0/n)

    F[:,0:2] = np.random.uniform(0,1,(n,2))

    #Each thing is made larger
    S += (size_max - size_min)/10

    # Reset specific thing (relative to frame number)
    i = frame  % 50
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i, 3] = 1
    F[i,0:2] = np.random.uniform(0,1,2)

#opacity 1 is black
#opacity 0 is transparent

    #Update scatter object
    scat.set_edgecolors(C)
    scat.set_offsets(P)
    

    #Return the modified object
    return scat,

print F

animation = animation.FuncAnimation(fig, update, interval=5)
plt.show()

