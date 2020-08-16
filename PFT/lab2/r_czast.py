# RK4

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
## STAŁE ##
alfa = 0.5
g = 9.81

## FUNKCJE ##
def pochodne(s,k):
        k[0] = s[2]
        k[1] = s[3]
        k[2] = -g*np.cos(alfa)**2*np.sin(s[0])/(np.sin(alfa)*s[1]) - 2*s[2]*s[3]/s[1]
        k[3] = np.sin(alfa)**2*s[1]*s[2]**2 - g*np.sin(alfa)*np.cos(alfa)**2*(1-np.cos(s[0]))

def rk4_vec(t,dt,n,iter,s):
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)

    pochodne(s[:,iter],k1)
    pochodne(s[:,iter]+dt/2*k1,k2)
    pochodne(s[:,iter]+dt/2*k2,k3)
    pochodne(s[:,iter]+dt*k3,k4)

    s[:,iter+1]=s[:,iter]+dt/6*(k1+2*k2+2*k3+k4)
    #print(s)

## PARAMETRY ##z
n = 4    #ilość zmiennych w RRZ1
dt = 0.1
t = 0
N = 500    #liczba kroków czasowych
tmax = dt*N


s = np.zeros((n,N))

## WARUNKI POCZĄTKOWE ##
stopnie = 4
s[0,0] =  1.1   # s0 = fi
s[1,0] =  1    # = z
s[2,0] =  0  # predkaosc d fi/dt
s[3,0] =  0  # = dz/dt ...

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

### ENERGIA
E = np.zeros(N)
E = (1/2)*(np.tan(alfa)**2*s[1]**2*s[2]**2 + \
    s[3]**2/np.cos(alfa)**2) +  \
    g*s[1]*np.sin(alfa)*[1-np.cos(s[0])]

X = np.zeros(N)
X = s[1]*np.tan(alfa)*np.cos(s[0])
Y = np.zeros(N)
Y = s[1]*np.tan(alfa)*np.sin(s[0])

teta = np.pi/2 - alfa

Xnew = np.cos(teta)*X + np.sin(teta)*s[1]
Ynew = Y
Znew = -np.sin(teta)*X + np.cos(teta)*s[1]


print(X.size())

## WYKRES ##
T = np.arange(0,tmax,dt)

ig1 = plt.figure()
ax1 = plt.subplot(321)
ax2 = plt.subplot(322)
ax3 = plt.subplot(325)
ax4 = plt.subplot(326)
ax1.plot(T,s[0])
ax2.plot(T,s[1])
ax3.plot(T,s[2])
ax4.plot(T,s[3])

ax1.set_xlabel('czas')
ax1.set_ylabel('kont')
ax2.set_xlabel('czas')
ax2.set_ylabel('z')

ax3.set_xlabel('czas')
ax3.set_ylabel('d_phi/dt')
ax4.set_xlabel('czas')
ax4.set_ylabel('dx/dt')
plt.title('phi='+str(s[0,0])+' z='+str(s[1,0])+' omeg_phi='+str(s[2,0])+' v_z='+str(s[3,0]))
plot_title = 'piz'+str(s[0,0])+'.png'
plt.savefig(plot_title)

ig2 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,E[0])
ax1.set_xlabel('czas')
ax1.set_ylabel('Energia całkowita')
plt.title('phi='+str(s[0,0])+' z='+str(s[1,0])+' omeg_phi='+str(s[2,0])+' v_z='+str(s[3,0]))
plot_title = 'ENERGIA'+str(s[0,0])+'.png'
plt.savefig(plot_title)

#zline = np.linspace(0, 15, 1000)
#print(np.linspace(0, 15, 1000)[2])
ig3 = plt.figure()
ax =plt.axes(projection = '3d')
ax.plot3D(Xnew,Ynew,Znew)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('phi='+str(s[0,0])+' z='+str(s[1,0])+' omeg_phi='+str(s[2,0])+' v_z='+str(s[3,0]))
plot_title = '3d'+str(s[0,0])+'.png'
plt.savefig(plot_title)
plt.show()
