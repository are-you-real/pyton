import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import animation
import math
#from matplotlib.ticker import LinearLocator, FormatStrFormatter

# STAŁE

# FUNKCJE
def af(a,u,t,N,dx): # ZMIENIA a
    for i in range(N-1):
        #a[i]=( u[i+1,t] + u[i-1,t] - 2*u[i,t] )/dx**2
        a[i+1]=( u[i+2,t] + u[i,t] - 2*u[i+1,t] )/dx**2

        #af(an1,u,t,N-1,dx)
## PARAMETRY ##z
dx = 0.01
xp = 0
xk = 1
X = np.arange(0,xk,dx)
N = np.size(X)   # liczba punktów struny

dt = 0.005
tmax = 5
T = np.arange(0,tmax,dt)
Nt = np.size(T)

# WARUNKI POCZĄTKOWE
u0 = np.zeros(np.size(X))
u0 = [math.exp(-100*(x-0.5)**2) for x in  X]

u = np.zeros((N,Nt))
u[:,0] = u0
v = np.zeros((N,Nt))

# MAIN
an = np.zeros(N)
an1 = np.zeros(N)
af(an,u,0,N-1,dx)

# Make data.
for t in range(Nt-1):
    u[:,t+1] = u[:,t] + dt*v[:,t] + (1/2)*an*dt**2 # dla wszystkich 'x'
    af(an1,u,t,N-1,dx) # dla wszystkich 'x'
    v[:,t+1] = v[:,t] +(dt/2)*(an+an1) #  dla wszystkich 'x'
    an=an1




#fig = plt.figure()

#ax = fig.gca(projection='3d')


#X = np.arange(-5, 5, 0.25)
#Y = np.arange(-5, 5, 0.25)

X,T = np.meshgrid(X,T)

#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)

fig = plt.figure()
ax = plt.subplot(111)
#fig, ax = plt.subplots()
im = ax.imshow(u)
#plt.colorbar()

'''
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, T, u.T, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

# PLOT

ig1 = plt.figure()
ax1 = plt.subplot(111)
time.sleep(0.2)
ax1.plot(X[0],u[:,1500])
plt.title('STRUNA')
ax1.set_xlabel('X')
ax1.set_ylabel('u')
plot_title = 'STRUNA'
'''
#plt.savefig(plot_title)
plt.show()
