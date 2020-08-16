# RK4

import numpy as np
import matplotlib.pyplot as plt
import math as m

## STAŁE ##
au = 149597870700       #[m]
G = 6.6741*10**(-11)    # [m^3/kg/s^2]
M = 1.989*10**(30)      # [kg]

## FUNKCJE ##
def pochodne(s,k):
        k[0] = s[2]
        k[1] = s[3]
        k[2] = -G*M*s[0]/np.sqrt(s[0]**2+s[1]**2)
        k[3] = -G*M*s[1]/np.sqrt(s[0]**2+s[1]**2)

def rk4_vec(t,dt,n,iter,s):
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)

    pochodne(s[:,iter],k1)
    pochodne(s[:,iter]+dt/2*k1,k2)
    pochodne(s[:,iter]+dt/2*k2,k3)
    pochodne(s[:,iter]+dt*k1,k4)

    s[:,iter+1]=s[:,iter]+dt/6*(k1+2*k2+2*k3+k4)
    #print(s)

## PARAMETRY ##z
n = 4    #ilość zmiennych w RRZ1
dt = 3600
t = 0
tmax = 24*3600
N = m.floor(tmax/dt)    #liczba kroków czasowych

s = np.zeros((n,N))

## WARUNKI POCZĄTKOWE ##
s[0,0] =  0         #x0
s[1,0] =  0.586*au  #y0
s[2,0] =  54600     #vx0 [m/s]
s[3,0] =  0         #vy0 [m/s]

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

## WYKRES ##
T = np.arange(0,tmax,dt)

ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(s[1],s[0],label='metoda RK$')
#ax1.plot(T,fi,label='obliczenia analityczne')
plt.title('RK4')
ax1.set_xlabel('czas[s]')
ax1.set_ylabel('kąt [rad]')
plot_title = 'wahadlo_t4.png'
plt.savefig(plot_title)
ax1.legend()
plt.show()
