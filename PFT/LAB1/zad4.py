# RK4

import numpy as np
import matplotlib.pyplot as plt

## STAŁE ##
R = 1
g = 9.81
m = 1

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

przypadki = 4
Ek = np.zeros((przypadki,N))
U = np.zeros((przypadki,N))
Ec = np.zeros((przypadki,N))
fis = np.zeros((przypadki,N))
omegi = np.zeros((przypadki,N))

stopnie = np.array([45,90,135,175])



## SYMULACJA W CZASIE ##
for k in range(przypadki):
    ## WARUNKI POCZĄTKOWE ##
    s[0,0] =  stopnie[k]*np.pi/180   # s0 = x
    s[1,0] =  0    # s1 = dx/dt ...

    i=0
    for j in range(N-1):
        rk4_vec(t,dt,n,i,s)
        i=i+1
        t=t+dt

    fis[k] = s[0]
    omegi[k] = s[1]

    Ek[k] = abs(m*s[1]*s[1]*R**2/2)
    U[k] = m*g*R*(1-np.cos(s[0]))
    Ec[k] = Ek[k] + U[k]# m*g*R*(np.cos(s[0])) #U[k]

#T = np.zeros(N)
okres = 2*np.pi*np.sqrt(R/g)*(1 + 1/16*fis[3]**2 + 11/3072*fis[3]**4 + 173/737280*fis[3]**6 + 22931/1321205760*fis[3]**8)

## WYKRESY ##

# EK
T = np.arange(0,tmax,dt)
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,Ek[0],label='teta=45')
ax1.plot(T,Ek[1],label='teta=90')
ax1.plot(T,Ek[2],label='teta=135')
ax1.plot(T,Ek[3],label='teta=175')
plt.title('Energia kinetyczna')
ax1.set_xlabel('czas[s]')
ax1.set_ylabel('Ek [J]')
plot_title = 'Energia kinetyczna'
plt.savefig(plot_title)
ax1.legend()

### U ###
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,U[0],label='teta=45')
ax1.plot(T,U[1],label='teta=90')
ax1.plot(T,U[2],label='teta=135')
ax1.plot(T,U[3],label='teta=175')
plt.title('Energia potencjalna')
ax1.set_xlabel('czas[s]')
ax1.set_ylabel('U [J]')
plot_title = 'Energia potencjalna'
plt.savefig(plot_title)
ax1.legend()

### Ec ###
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,Ec[0],label='teta=45')
ax1.plot(T,Ec[1],label='teta=90')
ax1.plot(T,Ec[2],label='teta=135')
ax1.plot(T,Ec[3],label='teta=175')
plt.title('Energia całkowita')
ax1.set_xlabel('czas[s]')
ax1.set_ylabel('E [J]')
plot_title = 'Energia całkowita'
plt.savefig(plot_title)
ax1.legend()


### omega(fi)
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(fis[0],omegi[0],label='teta=45')
ax1.plot(fis[1],omegi[1],label='teta=90')
ax1.plot(fis[2],omegi[2],label='teta=135')
ax1.plot(fis[3],omegi[3],label='teta=175')
plt.title('Trajektoria')
ax1.set_xlabel('kąt [rad]')
ax1.set_ylabel('prętkość kątowa [rad/s]')
plot_title = 'Trajektoria.png'
plt.savefig(plot_title)
ax1.legend()

### okres(fi)
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(fis[3],okres)
plt.title('Wykres okresu wahadła w funkcji maksymalnego wychylenia')
ax1.set_xlabel('kąt [rad]')
ax1.set_ylabel('okres [s]')
plot_title = 'okres.png'
plt.savefig(plot_title)


plt.show()
