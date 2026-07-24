import numpy as np
import matplotlib.pyplot as plt
import rk4_Gravity_numba as rk
from matplotlib.animation import FuncAnimation
from Nbody_rk4_Gravity_2d import animate

m=np.array([1.0,1.0,1.0],float)
r=np.array([[0.0,0.0],[0.5,0.87],[-0.5,0.87]],float)
v=np.array([[1.0,0.0],[-1.0,1.0],[-1.0,-1.0]],float)
N=3
G=1
e=0.1

## Setting marker size and color for each body
c = ['Red','Green','Blue']
ms=np.array([5,5,5],float)

animate(r,v,m,e,N,G,xlim=[-10,10],ylim=[-10,10],title='Nbody simulation',xlabel='X axis',ylabel='Y axis',grid=True,blit=True,colors=c,ms=ms,frames=1000,dt=0.1,interval=1)
