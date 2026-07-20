import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Verlet_Gravity_numba as V
from Nbody_Verlet_Gravity_3d_notrails import animate


##--------------------------Defining the parameters for the simulation-------------------------------------##
## For the central black hole
M_bh= 1.0e4
r_bh= np.array([0.0, 0.0, 0.0])
v_bh= np.array([0.0, 0.0, 0.0])

# Setting the no. of and masses bodies
N_bodies= 50000
N_disk= int(N_bodies*9/10)
N_jets= int(N_bodies*1/10)
N_jet_north= int(N_jets//2)
N_jet_south= int(N_jets - N_jet_north)
M_bodies= np.random.uniform(0.001*(M_bh/N_bodies),0.1*(M_bh/N_bodies), N_bodies)
N= N_bodies + 1

#Setting acretion disk parameters
R_in= 50
R_out= 200
H_disk=0.05
theta_min , theta_max= (np.pi/2) - H_disk , (np.pi/2) + H_disk
phi_min , phi_max= 0 , 2*np.pi

#Setting jet parameters
R_jet= R_in
theta_min_jet_north , theta_max_jet_north= 0 , 0.1
theta_min_jet_south , theta_max_jet_south= np.pi - 0.1 , np.pi
phi_min_jet , phi_max_jet= 0 , 2*np.pi

#Setting the gravitational constant and vectors
G=1
m= np.zeros(N)
r=np.zeros((N,3))
v=np.zeros((N,3))
a=np.zeros((N,3))

##------------------------Initializing the position and velocity of the central black hole---------------------------##
r[0]= r_bh
v[0]= v_bh
m[0]= M_bh

##------------------------Generating random  points for bodies in the accretion disk--------------------------##

## Generating random masses 
m[1:N_disk+1]= np.random.uniform(0.001*(M_bh/N_bodies),0.1*(M_bh/N_bodies), N_disk)

## Generating random positions in spherical coordinates for the accretion disk
theta_disk= np.random.uniform(theta_min, theta_max, N_disk)
phi_disk= np.random.uniform(phi_min, phi_max, N_disk)
r_disk= np.random.uniform(R_in, R_out, N_disk)
r[1:N_disk+1,0]= r_disk * np.sin(theta_disk) * np.cos(phi_disk)
r[1:N_disk+1,1]= r_disk * np.sin(theta_disk) * np.sin(phi_disk)
r[1:N_disk+1,2]= r_disk * np.cos(theta_disk)

## Generating velocities
v_k= np.sqrt(G*M_bh/r_disk)
vin=-0.05*v_k
v[1:N_disk+1,0]= (-1)*v_k*np.sin(phi_disk) + vin * np.cos(phi_disk)
v[1:N_disk+1,1]= v_k*np.cos(phi_disk) + vin * np.sin(phi_disk)
v[1:N_disk+1,2]= 0.05*v_k


##------------------------Generating random points for the north polar jets--------------------------##

## Generating masses
m[N_disk+1:N_disk+N_jet_north+1]= np.random.uniform(0.001*(M_bh/N_bodies),0.1*(M_bh/N_bodies), N_jet_north)

## Generating random positions in spherical coordinates for the north polar jets
theta_jet_north= np.random.uniform(theta_min_jet_north, theta_max_jet_north, N_jet_north)
phi_jet_north= np.random.uniform(phi_min_jet, phi_max_jet, N_jet_north)
r_jet_north= np.random.uniform(R_jet-10, R_jet+50, N_jet_north)
r[N_disk+1:N_disk+N_jet_north+1,0]= r_jet_north * np.sin(theta_jet_north) * np.cos(phi_jet_north)
r[N_disk+1:N_disk+N_jet_north+1,1]= r_jet_north * np.sin(theta_jet_north) * np.sin(phi_jet_north)
r[N_disk+1:N_disk+N_jet_north+1,2]= r_jet_north * np.cos(theta_jet_north)

### Generating velocities
v_k_jet_north= np.sqrt(2*G*M_bh/r_jet_north)
v[N_disk+1:N_disk+N_jet_north+1,0]= v_k_jet_north*np.random.uniform(-0.1,0.1, N_jet_north)
v[N_disk+1:N_disk+N_jet_north+1,1]= v_k_jet_north*np.random.uniform(-0.1,0.1, N_jet_north)
v[N_disk+1:N_disk+N_jet_north+1,2]= v_k_jet_north*np.random.uniform(1.1,2.0, N_jet_north)

##------------------------Generating random points for the south polar jets--------------------------##

## Generating masses
m[N_disk+N_jet_north+1:N]= np.random.uniform(0.001*(M_bh/N_bodies),0.1*(M_bh/N_bodies), N_jet_south)

## Generating random positions in spherical coordinates for the south polar jets
theta_jet_south= np.random.uniform(theta_min_jet_south, theta_max_jet_south, N_jet_south)
phi_jet_south= np.random.uniform(phi_min_jet, phi_max_jet, N_jet_south)
r_jet_south= np.random.uniform(R_jet-10, R_jet+50, N_jet_south)
r[N_disk+N_jet_north+1:N,0]= r_jet_south * np.sin(theta_jet_south) * np.cos(phi_jet_south)
r[N_disk+N_jet_north+1:N,1]= r_jet_south * np.sin(theta_jet_south) * np.sin(phi_jet_south)
r[N_disk+N_jet_north+1:N,2]= r_jet_south * np.cos(theta_jet_south)

### Generating velocities
v_k_jet_south= np.sqrt(2*G*M_bh/r_jet_south)
v[N_disk+N_jet_north+1:N,0]= v_k_jet_south*np.random.uniform(-0.1,0.1, N_jet_south)
v[N_disk+N_jet_north+1:N,1]= v_k_jet_south*np.random.uniform(-0.1,0.1, N_jet_south)
v[N_disk+N_jet_north+1:N,2]= v_k_jet_south*np.random.uniform(-1.1,-2.0, N_jet_south)

#------------------------Calling the animate function to visualize the simulation--------------------------##

##Setting the parameters for the animation
xlim=[-R_out - 10, R_out + 10]
ylim=[-R_out - 10, R_out + 10]
zlim=[-R_jet -30, R_jet + 30]

c=['black'] + ['red']*int(N_bodies) 
ms=[60] + [0.7]*int(N_bodies)

animate(r,v,m,e=1,N=N,G=G,xlim=xlim,ylim=ylim,zlim=zlim,title='Black Hole Accretion Disk Simulation',xlabel='X axis',ylabel='Y axis',zlabel='Z axis',grid=False,blit=False,colors=c,ms=ms,frames=10000,dt=0.1,interval=1)
