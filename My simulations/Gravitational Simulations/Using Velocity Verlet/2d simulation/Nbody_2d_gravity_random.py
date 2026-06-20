import numpy as np
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation
from Nbody_Verlet_Gravity_2d import animate


G=1
e=0.1
N=20      # No. of bodies

r=np.zeros((N,2))
v=np.zeros((N,2))
m=np.zeros(N)

## Set ranges (mass in kg , r in m , v in m/s)
m_min=10
m_max=15
r_min=0
r_max=10*np.sqrt(2)
v_min=2
v_max=4

c = np.random.rand(N, 3)

for k in range(N):
    mbody=np.random.uniform(m_min,m_max)
    m[k]=mbody
    dist=np.random.uniform(r_min,r_max)
    theta=np.random.uniform(0,2*np.pi)
    r[k,0]=dist*np.cos(theta)
    r[k,1]=dist*np.sin(theta)
    v[k,0]=np.random.uniform(v_min,v_max)
    v[k,1]=np.random.uniform(v_min,v_max)



animate(r,v,m,e,N,G,xlim=[-11,11],ylim=[-11,11],title='Nbody random simulation',xlabel='X axis',ylabel='Y axis',grid=True,blit=True,colors=c,frames=10000,dt=0.1,interval=10)
