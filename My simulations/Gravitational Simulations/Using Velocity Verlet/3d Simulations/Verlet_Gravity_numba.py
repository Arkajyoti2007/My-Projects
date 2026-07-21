import numpy as np
from numba import njit, prange

@njit(parallel=True, fastmath=True, cache=True)
def acceleration(m, r, e, N, G):
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


def verlet(r, v, dt, m, a, e, N, G):
    r_new = r + v * dt + 0.5 * a * dt ** 2
    a_new = acceleration(m, r_new, e, N, G)
    v_new = v + 0.5 * (a + a_new) * dt
    return r_new, v_new, a_new
