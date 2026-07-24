import numpy as np
from numba import njit, prange

@njit(parallel=True, fastmath=True, cache=True)
def acceleration(m,t,r,v,e, N, G):
    a = np.zeros((N, 3))
    e2 = e * e
    for i in prange(N):
        xi = r[i, 0]
        yi = r[i, 1]
        zi = r[i, 2]
        ax = 0.0
        ay = 0.0
        az = 0.0
        for j in range(N):
            if j == i:
                continue
            dx = r[j, 0] - xi
            dy = r[j, 1] - yi
            dz = r[j, 2] - zi
            dist_sq = dx * dx + dy * dy + dz * dz + e2
            f = G / dist_sq ** 1.5
            mj = m[j]
            ax += f * mj * dx
            ay += f * mj * dy
            az += f * mj * dz
        a[i, 0] = ax
        a[i, 1] = ay
        a[i, 2] = az
    return a

def energy(m,r,v,e,N,G):
    ke,pe,te=0,0,0
    for i in range(N):
        for j in range(i+1,N):
            pe+=G*m[i]*m[j]/np.sqrt((r[i,0]-r[j,0])**2 + (r[i,1]-r[j,1])**2 + (r[i,2]-r[j,2])**2 + e**2)
        ke+=0.5*m[i]*(v[i,0]**2 + v[i,1]**2 + v[i,2]**2)
    te=ke-pe     
    return ke,pe,te


def rk(r, v, dt, m, a, e, N, G):

    kx1 = v
    kv1 = a

    kx2 = v + 0.5 * dt * kv1
    kv2=acceleration(m, 0, r + 0.5 * dt * kx1, v + 0.5 * dt * kv1, e, N, G)

    kx3 = v + 0.5 * dt * kv2
    kv3=acceleration(m, 0, r + 0.5 * dt * kx2, v + 0.5 * dt * kv2, e, N, G)

    kx4 = v + dt * kv3
    kv4=acceleration(m, 0, r + dt * kx3, v + dt * kv3, e, N, G)

    r_new = r + (dt / 6.0) * (kx1 + 2 * kx2 + 2 * kx3 + kx4)
    v_new = v + (dt / 6.0) * (kv1 + 2 * kv2 + 2 * kv3 + kv4)
    a_new = acceleration(m, 0, r_new, v_new, e, N, G)

    return r_new, v_new, a_new
