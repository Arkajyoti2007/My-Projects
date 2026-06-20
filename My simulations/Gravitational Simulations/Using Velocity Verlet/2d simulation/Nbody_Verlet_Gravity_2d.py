import numpy as np 
import matplotlib.pyplot as plt
import Verlet_Gravity as V
from matplotlib.animation import FuncAnimation


def animate(r,v,m,e,N,G,xlim,ylim,title,xlabel,ylabel,grid,blit,colors , frames , dt,interval ):
    fig,ax=plt.subplots(figsize=(7, 7))
    ax.set_xlim(xlim[0],xlim[1])
    ax.set_ylim(ylim[0],ylim[1])
    ax.grid(grid)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_aspect('equal')

    body=[ax.plot([],[],'o',color=colors[i],ms=5,zorder=3)[0] for i in range(N)]
    trails=[ax.plot([],[],'-',color=colors[i],alpha=0.5,zorder=2)[0] for i in range(N)]



    a=V.acceleration(m,r,e,N,G)

    def init():
        for i in range(N):
            body[i].set_data([r[i, 0]], [r[i, 1]])
            trails[i].set_data([], [])
        return body + trails

    x_history=np.zeros((N,frames))
    y_history=np.zeros((N,frames))
    

    def update_frame(frame):
        nonlocal r,v,a
        r,v,a=V.verlet(r,v,dt,m,a,e,N,G)
        for i in range(N):
            x_history[i,frame]=r[i,0]
            y_history[i,frame]=r[i,1]
            body[i].set_data([x_history[i,frame]],[y_history[i,frame]])
            trails[i].set_data(x_history[i,:frame],y_history[i,:frame])
        return body+trails

    ani=FuncAnimation(fig,update_frame,frames=frames,interval=interval,init_func=init,blit=blit)
    plt.show()




