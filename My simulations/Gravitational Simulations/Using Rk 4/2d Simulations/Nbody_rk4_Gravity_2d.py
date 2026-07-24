import numpy as np 
import matplotlib.pyplot as plt
import rk4_Gravity_numba as rk
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

    body=[ax.plot([],[],marker='o',color=colors[i],markersize=ms[i],zorder=3)[0] for i in range(N)]
    trails=[ax.plot([],[],color=colors[i],alpha=0.5,zorder=2)[0] for i in range(N)]



    a=rk.acceleration(m, 0, r, v, e, N, G)

    def init():
        for i in range(N):
            body[i].set_data([r[i, 0]], [r[i, 1]])
            trails[i].set_data([], [])
        return body + trails

    x_history=np.zeros((N,frames))
    y_history=np.zeros((N,frames))
    KE=np.zeros(frames)
    PE=np.zeros(frames)
    TE=np.zeros(frames)

    def update_frame(frame):
        nonlocal r,v,a
        r,v,a=rk.rk(r,v,dt,m,a,e,N,G)
        for i in range(N):
            x_history[i,frame]=r[i,0]
            y_history[i,frame]=r[i,1]
            body[i].set_data([x_history[i,frame]],[y_history[i,frame]])
            trails[i].set_data(x_history[i,:frame],y_history[i,:frame])
        KE[frame],PE[frame],TE[frame]=rk.energy(m,r,v,e,N,G)

        return body+trails

    ani=FuncAnimation(fig,update_frame,frames=frames,interval=interval,init_func=init,blit=blit)
    frame_array=np.arange(frames)
    plt.show()
    plt.plot(frame_array,KE,label='Kinetic Energy')
    plt.plot(frame_array,PE,label='Potential Energy')
    plt.plot(frame_array,TE,label='Total Energy')
    plt.legend()
    plt.xlabel('Frame')
    plt.ylabel('Energy')
    plt.title('Energy vs Frame')
    plt.show()




