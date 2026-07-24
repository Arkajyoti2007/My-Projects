import numpy as np
import matplotlib.pyplot as plt
import rk4_Gravity_numba as rk
from matplotlib.animation import FuncAnimation


def animate(r, v, m, e, N, G, xlim, ylim, zlim, title, xlabel, ylabel, zlabel,grid, blit, colors, ms, frames, dt, interval):
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_zlim(zlim[0], zlim[1])
    ax.view_init(elev=0, azim=0)
    ax.grid(grid)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.set_axis_off()

    colors_arr = np.asarray(colors)
    sizes_arr = np.asarray(ms, dtype=float) ** 2

    scat = ax.scatter(r[:, 0], r[:, 1], r[:, 2], c=colors_arr, s=sizes_arr, depthshade=True)

    a = rk.acceleration(m, 0, r, v, e, N, G)

    def init():
        scat._offsets3d = (r[:, 0], r[:, 1], r[:, 2])
        return (scat,)

    def update_frame(frame):
        nonlocal r, v, a
        r, v, a = rk.rk(r, v, dt, m, a, e, N, G)
        scat._offsets3d = (r[:, 0], r[:, 1], r[:, 2])
        return (scat,)

    ani = FuncAnimation(fig, update_frame, frames=frames, interval=interval, init_func=init, blit=blit)
    plt.tight_layout()
    plt.show()
