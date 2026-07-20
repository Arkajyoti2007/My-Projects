import numpy as np 
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation


def animate(r,v,m,e,N,G,xlim,ylim,zlim,title,xlabel,ylabel,zlabel,grid,blit,colors ,ms, frames , dt,interval ):
    fig=plt.figure(figsize=(7, 7))
    ax=fig.add_subplot(111,projection='3d')
    ax.set_xlim(xlim[0],xlim[1])
    ax.set_ylim(ylim[0],ylim[1])
    ax.set_zlim(zlim[0],zlim[1])
    ax.grid(grid)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.set_axis_off()

    body=[ax.plot3D([],[],[],marker='o',color=colors[i],markersize=ms[i],zorder=3)[0] for i in range(N)]
    a=V.acceleration(m,r,e,N,G)

    def init():
        for i in range(N):
            body[i].set_data([r[i, 0]], [r[i, 1]])
            body[i].set_3d_properties([r[i, 2]])
        return body


    def update_frame(frame):
        nonlocal r,v,a
        r,v,a=V.verlet(r,v,dt,m,a,e,N,G)
        for i in range(N):

            body[i].set_data([r[i, 0]],[r[i, 1]])
            body[i].set_3d_properties([r[i, 2]])
        return body

    ani=FuncAnimation(fig,update_frame,frames=frames,interval=interval,init_func=init,blit=blit)
    plt.show()
  
 



