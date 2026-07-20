import numpy as np
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation
from Nbody_Verlet_Gravity_3d import animate

#Initial Cnditions
G=1
e=0.5
N_bodies1=100
N_bodies2=100
N=N_bodies1 + N_bodies2 + 2

#Defining the arrays
r=np.zeros((N,3))
v=np.zeros((N,3))
m=np.zeros(N)

## Setting conditions for the centre
m_centre1=1000
m_centre2=1000


## Set ranges (mass in kg , r in m , v in m/s)
m_min=0.5
m_max=2
r_min=5
r_max=20

##Adding centre point values
m[0]=m_centre1
m[1]=m_centre2
r[0,0] , r[0,1] , r[0,2] = 25 , 0 , 0
v[0,0] , v[0,1] , v[0,2] = 0 , 0 , 0
r[1,0] , r[1,1] , r[1,2] = -25 , 0 , 0
v[1,0] , v[1,1] , v[1,2] = 0 , 0 , 0

## Adding the non centre point values through random point generation
for k in range(2,N_bodies1+2):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    phi=np.random.uniform(0, 2*np.pi)
    r[k,0] , r[k,1] , r[k,2] = dist*np.cos(phi)-30 , dist*np.sin(phi) , np.random.uniform(-1, 1)*1   # Small z-offset for 3D effect

    #Velocities
    v_o=np.sqrt(G*m_centre1/dist)
    v_body=v_o*np.random.uniform(0.8,1)
    v[k,0] , v[k,1] , v[k,2] = v_body*np.cos(phi+np.pi/2) , v_body*np.sin(phi+np.pi/2) , np.random.uniform(-0.1, 0.1)*3  # Small z-velocity for 3D effect``

for k in range(N_bodies1+2,N_bodies1+N_bodies2+2):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    phi=np.random.uniform(0, 2*np.pi)
    r[k,0] , r[k,1] , r[k,2] = dist*np.cos(phi)+30 , dist*np.sin(phi) , np.random.uniform(-1, 1)*3   # Small z-offset for 3D effect

    #Velocities
    v_o=np.sqrt(G*m_centre2/dist)
    v_body=v_o*np.random.uniform(0.6,1)
    v[k,0] , v[k,1] , v[k,2] = v_body*np.cos(phi+np.pi/2) , v_body*np.sin(phi+np.pi/2) , np.random.uniform(-0.1, 0.1)*5  # Small z-velocity for 3D effect``



## Setting x, y, and z limits for the simulation
xlim=[-50, 40]
ylim=[-35, 50]
zlim=[-20, 20]

## Setting marker size and color for each body
c = ["black"] * 2 + ["blue"] * (N-2)
ms=np.zeros(N)
ms[0:2] , ms[2:]=8,2

animate(r,v,m,e,N,G,xlim=xlim,ylim=ylim,zlim=zlim,title='Nbody Galaxy Collision Simulation',xlabel='X axis',ylabel='Y axis',zlabel='Z axis',grid=True,blit=True,colors=c,ms=ms,frames=10000,dt=0.01,interval=10)
