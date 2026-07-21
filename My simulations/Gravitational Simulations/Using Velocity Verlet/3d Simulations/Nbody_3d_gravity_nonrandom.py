import numpy as np
import matplotlib.pyplot as plt
import Verlet_Gravity_numba as V
from matplotlib.animation import FuncAnimation
from Nbody_Verlet_Gravity_3d import animate

m=np.array([1.0,1.0],float)
r=np.array([[2.0,6.0,0.0],[4.0,5.0,0.0]],float)
v=np.array([[1.0,0.0,0.0],[0.0,0.0,0.0]],float)
N=2
G=1
e=0.1

animate(r,v,m,e,N,G,xlim=[-11,11],ylim=[-11,11],zlim=[-11,11],title='Nbody simulation',xlabel='X axis',ylabel='Y axis',zlabel='Z axis',grid=True,blit=False,colors=['Red','Green'],ms=[10,10],frames=100,dt=0.1,interval=1)
