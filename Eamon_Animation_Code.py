'''
Eamon Lee
Animation Code
This code runs a animation of randomly generated
circles varying in size and color
4/23/18
'''

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(6,6), facecolor = 'white')
ax = fig.add_axes([0,0,1,1], frameon = False, aspect=1)

n = 50
size_min = 10
size_max = 3000
P = np.random.uniform(0,1,(n,2))

print P

# Colors
C = np.ones((n,4)) * (0,0,0,1)

# Face Colors
F = np.ones((n,4)) * (0,0,0,1)

# Alpha color channel goes from 0 (transparent) to 1 (opaque)
# Takes th selected collumn and changes them to random numbers
C[:,3] = np.linspace(0,1,n)

# Sizes
S = np.linspace(size_min,size_max, n)

print C


# Scatter plot
scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5,
                  edgecolors = C, facecolors=F)

# Ensure limits are [0,1] and remove ticks
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])


def update(frame):
    global P, C, S

    # Everything is made more transparent
    C[:,3] = np.maximum(1, C[:,3] - 1.0/n)

    F[:,0:2] = np.random.uniform(0,1,(n,2))

    # Each thing is made larger
    S += (size_max - size_min)/20

    # Reset specific thing (relative to frame number)
    i = frame % 50
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i,3] = 1
    F[i,0:2] = np.random.uniform(0,1,2)

    # Update scatter object
    scat.set_edgecolors(C)
    scat.set_facecolors(F)
    scat.set_sizes(S)
    scat.set_offsets(P)

    # Return scat
    return scat,


print F

animation = animation.FuncAnimation(fig, update, interval=5)
plt.show()
