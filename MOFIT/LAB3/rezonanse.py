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
tmax = 20
dt = 0.005
T = np.arange(16,tmax,dt)
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
W = np.arange(0,10*np.pi,np.pi/10)
Ex = np.zeros(Nx)
Ew = np.zeros(np.size(W))

j = 0
for w in W:
    aF = np.zeros(Nx)
    aF[round(Nx/2)] = np.cos(w*0) + np.cos(w*(0+dt))

    for x in range(Nx-2):
        a1[x+1] = (u[0,x+2] + u[0,x] - 2*u[0,x+1])/dx**2 + aF[x+1]  #### ??????????????
        ab[x+1] = (u[0,x+2] + u[0,x] - 2*u[0,x+1])/dx**2 - 2*beta*v[x+1] + aF[x+1]

    Ex = (1/2)*(v**2+((ab+a1)/2)**2)
    ## MAIN ##

    for t in range(Nt-1):
        u[t+1,:] = u[t,:] + dt*v + (1/2)*ab*(dt**2)

        aF[round(Nx/2)] = np.cos(w*T[t+1]) + np.cos(w*(T[t+1]+dt))
        for x in range(Nx-2):
            a1[x+1] = (u[t+1,x+2] + u[t+1,x] - 2*u[t+1,x+1])/(dx**2) + aF[x+1]
            ab1[x+1] = (u[t+1,x+2] + u[t+1,x] - 2*u[t+1,x+1])/(dx**2) - 2*beta*v[x+1] + aF[x+1]
        v = (v + (dt/2)*(a1+ab))/(1+beta*dt)
        ab=ab1
        Ex = Ex + (1/2)*(v**2+ab**2)*dx
        Ew[j] = Ew[j] + (1/(T[Nt-1]-T[0]))*np.sum(Ex)*dt
    j = j+1

ig2 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(W,Ew)
ax1.set_xlabel('omega')
ax1.set_ylabel('Energia średnia')
plt.title('Energia średnia')
plot_title = 'ENERGIA.png'
plt.savefig(plot_title)
plt.show()
