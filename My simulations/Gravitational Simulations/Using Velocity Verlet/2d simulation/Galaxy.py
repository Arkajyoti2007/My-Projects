import numpy as np
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation
from Nbody_Verlet_Gravity_2d import animate

#Initial Cnditions
G=1
e=0.5
N_bodies=50      # No. of bodies
N=N_bodies + 1

#Defining the arrays
r=np.zeros((N,2))
v=np.zeros((N,2))
m=np.zeros(N)

## Setting conditions for the centre
m_centre=1e4
r_centre=0
v_centre=0

## Set ranges (mass in kg , r in m , v in m/s)
m_min=0.1
m_max=2
r_min=1
r_max=15

##Adding centre point values
m[0]=m_centre
r[0,0] , r[0,1] = r_centre*np.cos(np.pi/4) ,r_centre*np.sin(np.pi/4)
v[0,0] , v[0,1] = v_centre*np.cos(np.pi/4) , v_centre*np.sin(np.pi/4)

## Adding the non centre point values through random point generation
for k in range(1,N):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    theta=np.random.uniform(0,2*np.pi)
    r[k,0] , r[k,1] = dist*np.cos(theta) , dist*np.sin(theta)
    
    #Velocities
    v_o=np.sqrt(G*m_centre/dist)
    v_body=v_o*np.random.uniform(0.5,1)
    v[k,0] , v[k,1] = v_body*np.cos(theta+np.pi/2) , v_body*np.sin(theta+np.pi/2)
    
## Defining the colour variable
c = np.random.rand(N, 3)
ms=np.zeros(N)
ms[:]=5

## Setting x and y limits for the simulation
xlim=[-(r_max + 4), (r_max + 4)]
ylim=[-(r_max + 4), (r_max + 4)]

animate(r,v,m,e,N,G,xlim=xlim,ylim=ylim,title='Galaxy Simulation',xlabel='X axis',ylabel='Y axis',grid=True,blit=True,colors=c,ms=ms,frames=10000,dt=0.01,interval=10)
