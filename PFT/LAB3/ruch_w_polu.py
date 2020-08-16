# RK4

import numpy as np
import matplotlib.pyplot as plt

## STAŁE ##
q = 1
B = 1
m = 1
wc = q*B/m
T = 2*np.pi/wc

## FUNKCJE ##
def pochodne(s,k):
        k[0] = s[3]/m
        k[1] = s[4]/(m*s[0]**2) - q*B/(2*m)
        k[2] = s[5]/m
        k[3] = s[4]**2/(m*s[0]**3) - q**2*B**2*s[0]/(4*m)
        k[4] = 0
        k[5] = 0
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
n = 6    #ilość zmiennych w RRZ1
t = 0
N = 5000    #liczba kroków czasowych
dt = 5*T/N
tmax = dt*N

s = np.zeros((n,N))
x = np.zeros((4,N))
y = np.zeros((4,N))
r = np.zeros((4,N))
phi = np.zeros((4,N))
p_r = np.zeros((4,N))
p_phi = np.zeros((4,N))
E = np.zeros((4,N))

## WARUNKI POCZĄTKOWE ##
# (0)   ------------------------------
s[0,0] = 1.5        # r
s[1,0] = 1.25*np.pi # phi
s[2,0] = 0          # z
s[3,0] = 0          # p_r
s[4,0] = q*B*s[0,0]**2/2   # p_phi
s[5,0] = 0          # p_z

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

# Przejśćie do układu kartezjańskiego
x[0] = s[0,:]*np.cos(s[1,:])
y[0] = s[0,:]*np.sin(s[1,:])
r[0] = s[0,:]
phi[0] = s[1,:]
p_r[0] = s[3,:]
p_phi[0] = s[4,:]
E[0] = (1/(2*m))*(s[3]**2 + s[4]**2/s[0]**2 + s[5]) -\
    q*B*s[4]/(2*m) + q**2*B**2*s[0]**2/(8*m)


# (1)   ------------------------------
s[0,0] = 1        # r
s[1,0] = 1.25*np.pi # phi
s[2,0] = 0          # z
s[3,0] = 0          # p_r
s[4,0] = -q*B*s[0,0]**2/2   # p_phi
s[5,0] = 0          # p_z

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

# Przejśćie do układu kartezjańskiego
x[1] = s[0,:]*np.cos(s[1,:])
y[1] = s[0,:]*np.sin(s[1,:])
r[1] = s[0,:]
phi[1] = s[1,:]
p_r[1] = s[3,:]
p_phi[1] = s[4,:]
E[1] = (1/(2*m))*(s[3]**2 + s[4]**2/s[0]**2 + s[5]) -\
    q*B*s[4]/(2*m) + q**2*B**2*s[0]**2/(8*m)

# (2)   ------------------------------
s[0,0] = 2       # r
s[1,0] = 0       # phi
s[2,0] = 0       # z
s[3,0] = 0       # p_r
s[4,0] = -q*B*s[0,0]**2/2   # p_phi
s[5,0] = 0       # p_z

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

# Przejśćie do układu kartezjańskiego
x[2] = s[0,:]*np.cos(s[1,:])
y[2] = s[0,:]*np.sin(s[1,:])
r[2] = s[0,:]
phi[2] = s[1,:]
p_r[2] = s[3,:]
p_phi[2] = s[4,:]
E[2] = (1/(2*m))*(s[3]**2 + s[4]**2/s[0]**2 + s[5]) -\
    q*B*s[4]/(2*m) + q**2*B**2*s[0]**2/(8*m)

# (3)   ------------------------------
s[0,0] = 2        # r
s[1,0] = 0        # phi
s[2,0] = 0        # z
s[3,0] = 2        # p_r
s[4,0] = -q*B*s[0,0]**2/2   # p_phi
s[5,0] = 0        # p_z

## SYMULACJA W CZASIE ##
i=0
for j in range(N-1):
    rk4_vec(t,dt,n,i,s)
    i=i+1
    t=t+dt

# Przejśćie do układu kartezjańskiego
x[3] = s[0,:]*np.cos(s[1,:])
y[3] = s[0,:]*np.sin(s[1,:])
r[3] = s[0,:]
phi[3] = s[1,:]
p_r[3] = s[3,:]
p_phi[3] = s[4,:]
E[3] = (1/(2*m))*(s[3]**2 + s[4]**2/s[0]**2 + s[5]) -\
    q*B*s[4]/(2*m) + q**2*B**2*s[0]**2/(8*m)

## WYKRES ##
T = np.arange(0,tmax,dt)
# x,y
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(x[0],y[0],'o',label='WP 0')
ax1.plot(x[1],y[1],label='WP 1')
ax1.plot(x[2],y[2],label='WP 2')
ax1.plot(x[3],y[3],label='WP 3')
#ax1.plot(T,fi,label='obliczenia analityczne')
#plt.title('tor')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
plot_title = 'tor.png'
plt.savefig(plot_title)
ax1.legend()

# r,t
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,r[0],'o',label='WP 0')
ax1.plot(T,r[1],label='WP 1')
ax1.plot(T,r[2],label='WP 2')
ax1.plot(T,r[3],label='WP 3')
#ax1.plot(T,fi,label='obliczenia analityczne')
#plt.title('Wahadło,teta0='+str(stopnie)+'stopnie')
ax1.set_xlabel('t')
ax1.set_ylabel('r')
plot_title = 'rt.png'
plt.savefig(plot_title)
ax1.legend()

# phi,t
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,phi[0],'o',label='WP 0')
ax1.plot(T,phi[1],label='WP 1')
ax1.plot(T,phi[2],label='WP 2')
ax1.plot(T,phi[3],label='WP 3')
#ax1.plot(T,fi,label='obliczenia analityczne')
#plt.title('Wahadło,teta0='+str(stopnie)+'stopnie')
ax1.set_xlabel('t')
ax1.set_ylabel('phi')
plot_title = 'phiT.png'
plt.savefig(plot_title)
ax1.legend()

# p_r,t
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,p_r[0],'o',label='WP 0')
ax1.plot(T,p_r[1],label='WP 1')
ax1.plot(T,p_r[2],label='WP 2')
ax1.plot(T,p_r[3],label='WP 3')
#ax1.plot(T,fi,label='obliczenia analityczne')
#plt.title('Wahadło,teta0='+str(stopnie)+'stopnie')
ax1.set_xlabel('t')
ax1.set_ylabel('p_r')
plot_title = 'prT.png'
plt.savefig(plot_title)
ax1.legend()

# p_phi,t
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,p_phi[0],'o',label='WP 0')
ax1.plot(T,p_phi[1],label='WP 1')
ax1.plot(T,p_phi[2],label='WP 2')
ax1.plot(T,p_phi[3],label='WP 3')
#ax1.plot(T,fi,label='obliczenia analityczne')
#plt.title('Wahadło,teta0='+str(stopnie)+'stopnie')
ax1.set_xlabel('t')
ax1.set_ylabel('p_phi')
plot_title = 'pphiT.png'
plt.savefig(plot_title)
ax1.legend()

# E,t
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T,E[0],'o',label='WP 0')
ax1.plot(T,E[1],label='WP 1')
ax1.plot(T,E[2],label='WP 2')
ax1.plot(T,E[3],label='WP 3')
#ax1.plot(T,fi,label='obliczenia analityczne')
#plt.title('Wahadło,teta0='+str(stopnie)+'stopnie')
ax1.set_xlabel('t')
ax1.set_ylabel('E')
plot_title = 'Et.png'
plt.savefig(plot_title)
ax1.legend()
plt.show()
