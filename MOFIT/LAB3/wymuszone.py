#WYMUSZONE
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import animation
import math
#from matplotlib.ticker import LinearLocator, FormatStrFormatter

# STAŁE
# FUNKCJE
## PARAMETRY ##
tmax = 10
dt = 0.005
T = np.arange(0,tmax,dt)
Nt = np.size(T)

dx = 0.01
X = np.arange(0,1,dx)
Nx = np.size(X)

u = np.zeros((Nt,Nx))
#u[0,:] = [math.exp(-100*(x-0.5)**2) for x in  X]

u[0,0] = 0
u[0,Nx-1] = 0

beta = 1

v = np.zeros(Nx)

a1 = np.zeros(Nx)
ab = np.zeros(Nx)
ab1 = np.zeros(Nx)

### WYMUSZENIA ###
w = np.pi/2
aF = np.zeros(Nx)
aF[round(Nx/2)] = np.cos(w*0)



for x in range(Nx-2):
    a1[x+1] = (u[0,x+2] + u[0,x] - 2*u[0,x+1])/dx**2 + aF[x+1]  #### ??????????????
    ab[x+1] = (u[0,x+2] + u[0,x] - 2*u[0,x+1])/dx**2 - 2*beta*v[x+1] + aF[x+1]

## MAIN ##
j = 0

for t in range(Nt-1):
    u[t+1,:] = u[t,:] + dt*v + (1/2)*ab*(dt**2)

    aF[round(Nx/2)] = np.cos(w*T[t+1])
    for x in range(Nx-2):
        a1[x+1] = (u[t+1,x+2] + u[t+1,x] - 2*u[t+1,x+1])/(dx**2) + aF[x+1]
        ab1[x+1] = (u[t+1,x+2] + u[t+1,x] - 2*u[t+1,x+1])/(dx**2) - 2*beta*v[x+1] + aF[x+1]
    v = (v + (dt/2)*(a1+ab))/(1+beta*dt)
    ab=ab1



X,T = np.meshgrid(X,T)

fig = plt.figure()
ax = plt.subplot(111)

im = ax.imshow(u.T,extent=[0,np.max(T),1,0])
ax.set_aspect(2)
fig.colorbar(im, ax=ax)
plt.title('wymuszenie')
plot_title = 'wymuszenie.png'
plt.savefig(plot_title)
plt.show()
