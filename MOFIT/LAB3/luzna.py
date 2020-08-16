#Luźne
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
# STAŁE
# FUNKCJE
## PARAMETRY ##
tmax = 5
dt = 0.005
T = np.arange(0,tmax,dt)
Nt = np.size(T)

dx = 0.01
X = np.arange(0,1,dx)
Nx = np.size(X)

u = np.zeros((Nt,Nx))
u[0,:] = [math.exp(-100*(x-0.5)**2) for x in  X]
u[0,0] = u[0,1]
u[0,Nx-1] = u[0,Nx-2]

v = np.zeros(Nx)

a = np.zeros(Nx)
a1 = np.zeros(Nx)
for x in range(Nx-2):
    a[x+1] = (u[0,x+2] + u[0,x] - 2*u[0,x+1])/dx**2


## MAIN ##
for t in range(Nt-1):
    u[t+1,:] = u[t,:] + dt*v + (1/2)*a*(dt**2)
    u[t+1,0] = u[t+1,1]
    u[t+1,Nx-1] = u[t+1,Nx-2]
    for x in range(Nx-2):
        a1[x+1] = (u[t+1,x+2] + u[t+1,x] - 2*u[t+1,x+1])/(dx**2)
    v = v + (dt/2)*(a+a1)
    a=a1



X,T = np.meshgrid(X,T)

fig = plt.figure()
ax = plt.subplot(111)

im = ax.imshow(u.T,extent=[0,np.max(T),1,0])
ax.set_aspect(2)
fig.colorbar(im, ax=ax)
plt.title('Luźne warunki brzegowe')
plot_title = 'Luzne.png'
plt.savefig(plot_title)
plt.show()
