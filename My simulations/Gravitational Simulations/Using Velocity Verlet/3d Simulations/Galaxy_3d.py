import numpy as np
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation
from Nbody_Verlet_Gravity_3d import animate

#Initial Cnditions
G=1
e=0.1
N_bodies=50     # No. of bodies
N=N_bodies + 1

#Defining the arrays
r=np.zeros((N,3))
v=np.zeros((N,3))
m=np.zeros(N)

## Setting conditions for the centre
m_centre=1000
r_centre=0
v_centre=0

## Set ranges (mass in kg , r in m , v in m/s)
m_min=0.5
m_max=2
r_min=3
r_max=20

##Adding centre point values
m[0]=m_centre
r[0,0] , r[0,1] , r[0,2] = r_centre*np.cos(np.pi/4) ,r_centre*np.sin(np.pi/4) , 0
v[0,0] , v[0,1] , v[0,2] = v_centre*np.cos(np.pi/4) , v_centre*np.sin(np.pi/4) , 0

## Adding the non centre point values through random point generation
for k in range(1,N):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    phi=np.random.uniform(0, 2*np.pi)
    r[k,0] , r[k,1] , r[k,2] = dist*np.cos(phi) , dist*np.sin(phi) , np.random.uniform(-1, 1)*3   # Small z-offset for 3D effect

    #Velocities
    v_o=np.sqrt(G*m_centre/dist)
    v_body=v_o*np.random.uniform(0.6,1)
    v[k,0] , v[k,1] , v[k,2] = v_body*np.cos(phi+np.pi/2) , v_body*np.sin(phi+np.pi/2) , np.random.uniform(-0.1, 0.1)*5  # Small z-velocity for 3D effect``


## Setting x, y, and z limits for the simulation
xlim=[-(r_max + 4), (r_max + 4)]
ylim=[-(r_max + 4), (r_max + 4)]
zlim=[-(r_max + 4), (r_max + 4)]

## Setting marker size and color for each body
c = ["black"] * 1 + ["blue"] * (N - 1)
ms=np.zeros(N)
ms[0] , ms[1:]=8,3

animate(r,v,m,e,N,G,xlim=xlim,ylim=ylim,zlim=zlim,title='Galaxy Simulation',xlabel='X axis',ylabel='Y axis',zlabel='Z axis',grid=True,blit=True,colors=c,ms=ms,frames=10000,dt=0.01,interval=10)
