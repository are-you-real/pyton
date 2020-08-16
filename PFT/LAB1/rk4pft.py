# RK4

import numpy as np
import matplotlib.pyplot as plt

## STAŁE ##
R = 1
g = 9.81

## FUNKCJE ##
def pochodne(s,k):
        k[0] = s[1]
        k[1] = -g/R*np.sin(s[0])

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
n = 2    #ilość zmiennych w RRZ1
dt = 0.01
t = 0
N = 1000    #liczba kroków czasowych
tmax = dt*N

s = np.zeros((n,N))

## WARUNKI POCZĄTKOWE ##
stopnie = 4
s[0,0] =  stopnie*np.pi/180   # s0 = x
s[1,0] =  0    # s1 = dx/dt ...
#s[2] =      # s2 = d^2x/dt^2
#s[4] =

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

################### ROZW ANALITYCZNE #############
fi0 = stopnie*np.pi/180
t = 0
fi = np.zeros(N)
i=0
for i in range(N):
    fi[i] = fi0*np.sin(np.sqrt(g/R)*t + np.pi/2)
    t = t + dt
    i=i+1



## WYKRES ##
T = np.arange(0,tmax,dt)

ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,s[0],label='metoda RK4')
ax1.plot(T,fi,label='obliczenia analityczne')
plt.title('Wahadło,teta0='+str(stopnie)+'stopnie')
ax1.set_xlabel('czas[s]')
ax1.set_ylabel('kąt [rad]')
plot_title = 'wahadlo_t4.png'
plt.savefig(plot_title)
ax1.legend()
plt.show()
