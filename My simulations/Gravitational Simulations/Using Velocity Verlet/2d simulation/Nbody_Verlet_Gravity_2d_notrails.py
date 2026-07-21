import numpy as np 
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation


def animate(r,v,m,e,N,G,xlim,ylim,title,xlabel,ylabel,grid,blit,colors,ms , frames , dt,interval ):
    fig,ax=plt.subplots(figsize=(7, 7))
    ax.set_xlim(xlim[0],xlim[1])
    ax.set_ylim(ylim[0],ylim[1])
    ax.grid(grid)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_aspect('equal')

    colors_arr = np.asarray(colors)
    sizes_arr = np.asarray(ms, dtype=float) ** 2

    scat = ax.scatter(r[:, 0], r[:, 1], c=colors_arr, s=sizes_arr, depthshade=True)
    a=V.acceleration(m,r,e,N,G)

    def init():
        for i in range(N):
            scat._setdata = (r[:, 0], r[:, 1])
        return (scat,)



    def update_frame(frame):
        nonlocal r,v,a
        r,v,a=V.verlet(r,v,dt,m,a,e,N,G)
        scat._setdata = (r[:, 0], r[:, 1])
        return (scat,)

    ani=FuncAnimation(fig,update_frame,frames=frames,interval=interval,init_func=init,blit=blit)
    
    plt.show()



