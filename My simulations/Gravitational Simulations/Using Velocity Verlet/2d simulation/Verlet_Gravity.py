import numpy as np

def acceleration(m,r,e,N,G):
    i,j = np.triu_indices(N,k=1)
    a_x = np.zeros(N)
    a_y = np.zeros(N)
    dx = r[j,0] - r[i,0]
    dy = r[j,1] - r[i,1]
    dist_sq = dx**2 + dy**2 + e**2
    f = (G) / (dist_sq**1.5)
    a_x = np.bincount(i,weights=f*m[j]*dx,minlength=N) - np.bincount(j,weights=f*m[i]*dx,minlength=N)
    a_y = np.bincount(i,weights=f*m[j]*dy,minlength=N) - np.bincount(j,weights=f*m[i]*dy,minlength=N)
    return np.column_stack((a_x, a_y))


def energy(m,r,v,e,N,G):
    ke,pe,te=0,0,0
    for i in range(N):
        for j in range(i+1,N):
            pe+=G*m[i]*m[j]/np.sqrt((r[i,0]-r[j,0])**2 + (r[i,1]-r[j,1])**2 + e**2)
        ke+=0.5*m[i]*(v[i,0]**2 + v[i,1]**2)
    te=ke-pe     
    return ke,pe,te



def verlet(r,v,dt,m,a,e,N,G):
    r_new=r.copy()
    r_new=r + v*dt + 0.5*a*dt**2
    a_new=acceleration(m,r_new,e,N,G)
    v_new=v+0.5*(a+a_new)*dt
    return r_new,v_new,a_new
