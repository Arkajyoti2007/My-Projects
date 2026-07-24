import numpy as np
import matplotlib.pyplot as plt
import rk4_Gravity_numba as rk
from matplotlib.animation import FuncAnimation
from Nbody_rk4_Gravity_2d import animate

#Initial Cnditions
G=1
e=5
N_bodies1=100
N_bodies2=100
N_bodies3=100
N=N_bodies1 + N_bodies2 + N_bodies3 + 3

#Defining the arrays
r=np.zeros((N,2))
v=np.zeros((N,2))
m=np.zeros(N)

## Setting conditions for the centre
m_centre1=1e3
m_centre2=1e3
m_centre3=1e3


## Set ranges (mass in kg , r in m , v in m/s)
m_min=0.1
m_max=2
r_min=1
r_max=25

##Adding centre point values
m[0]=m_centre1
r[0,0] , r[0,1] = -40,0
v[0,0] , v[0,1] = 0,0
m[1]=m_centre2
r[1,0] , r[1,1] = 40,0
v[1,0] , v[1,1] = 0,0
m[2]=m_centre3
r[2,0] , r[2,1] = 0,40
v[2,0] , v[2,1] = 0,0
## Adding the non centre point values through random point generation for the first galaxy
for k in range(3,N_bodies1+3):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    theta=np.random.uniform(0,2*np.pi)
    r[k,0] , r[k,1] = dist*np.cos(theta)-40 , dist*np.sin(theta)
    
    #Velocities
    v_o=np.sqrt(G*m_centre1/dist)
    v_body=v_o*np.random.uniform(0.5,1)
    v[k,0] , v[k,1] = v_body*np.cos(theta+np.pi/2) , v_body*np.sin(theta+np.pi/2)
    
for k in range(N_bodies1+3,N_bodies1+N_bodies2+3):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    theta=np.random.uniform(0,2*np.pi)
    r[k,0] , r[k,1] = dist*np.cos(theta)+40 , dist*np.sin(theta)
    
    #Velocities
    v_o=np.sqrt(G*m_centre2/dist)
    v_body=v_o*np.random.uniform(0.5,1)
    v[k,0] , v[k,1] = v_body*np.cos(theta+np.pi/2) , v_body*np.sin(theta+np.pi/2)

for k in range(N_bodies1+N_bodies2+3,N):
    
    # Mass
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody

    #Position
    dist=np.random.uniform(r_min,r_max)
    theta=np.random.uniform(0,2*np.pi)
    r[k,0] , r[k,1] = dist*np.cos(theta) , dist*np.sin(theta)+40
    
    #Velocities
    v_o=np.sqrt(G*m_centre3/dist)
    v_body=v_o*np.random.uniform(0.5,1)
    v[k,0] , v[k,1] = v_body*np.cos(theta+np.pi/2) , v_body*np.sin(theta+np.pi/2)

## Defining the colour and size variable
c = ["black"] * 3 + ["blue"] * (N - 3)
ms = np.zeros(N, dtype=float)
ms[:3] = 8
ms[3:] = 3

## Setting x and y limits for the simulation
xlim=[-60, 60]
ylim=[-60, 60]

animate(r,v,m,e,N,G,xlim=xlim,ylim=ylim,title='Galaxy Simulation',xlabel='X axis',ylabel='Y axis',grid=True,blit=True,colors=c,ms=ms,frames=100000,dt=0.1,interval=0.1)
