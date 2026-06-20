import numpy as np 
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation
from Nbody_Verlet_Gravity_2d import animate

m=np.array([10.0,10.0],float)
r=np.array([[4.0,96.0],[4.0,100.0]],float)
v=np.array([[-1.054,-0.556],[1.054,-0.556]],float)
N=2
G=1
e=0.1
animate(r,v,m,e,N,G,xlim=[-100,100],ylim=[-100,100],title='Binart star 2d simulation',xlabel='X axis',ylabel='Y axis',grid=True,blit=False,colors=['Red','Green'],frames=10000,dt=0.1,interval=1)