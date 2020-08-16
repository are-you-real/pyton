#R4
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

au = 149597870700   #[m]
G = 6.6741*10**(-11)     # [m^3/kg/s^2]
G = G * 3600 / au**3           # [au^3/kg/min]
M = 1.989*10**(30)      # [kg]
h_okres = 2375162222    # [s]
h_okres = h_okres/60/60 #[h]

x0 = [0]
y0 = [8.766435223*10**(10)] #[m]
y0[0] = y0[0] / au
vx0 = [54600 * 60 * 60/ au ]
vy0 = [0]      #[au/h]                 #[m/s]
# funkcje
def last(x):
    return x[len(x)-1]
def at(x_war,r):            #bierze zmienną float
    return -G*M*x_war/(r**2)    #-G*M*last(x)/r**2

def k1_f(x,y,vx,vy,k1,r,dt):
    k1[0].append(last(vx))
    k1[1].append(last(vy))
    k1[2].append(at(last(x),r))
    k1[3].append(at(last(y),r))
#k2
def k2_f(x,y,k1,k2,r,dt):
    k2[0].append(k1[0][len(k1[0])-1] + dt*k1[2][len(k1[2])-1]/2)
    k2[1].append(k1[1][len(k1[1])-1] + dt*k1[3][len(k1[3])-1]/2)
    k2[2].append(at(dt*last(k1[0])/2,r)) #last(x)+
    k2[3].append(at(last(y)+dt*last(k1[1])/2,r))

#k3
def k3_f(x,y,k1,k2,k3,r,dt):
    k3[0].append(last(k1[0])+dt*last(k2[2])/2)
    k3[1].append(last(k1[1])+dt*last(k2[3])/2)
    k3[2].append(at(last(x)+dt*last(k2[0])/2,r))
    k3[3].append(at(last(y)+dt*last(k2[1])/2,r))

#k4
def k4_f(x,y,k1,k2,k3,r,dt):
    k4[0].append(last(k1[0])+dt*last(k3[2])/2)
    k4[1].append(last(k1[1])+dt*last(k3[3])/2)
    k4[2].append(at(last(x)+dt*last(k3[0])/2,r))
    k4[3].append(at(last(y)+dt*last(k3[1])/2,r))

def mag(x,y):
    return np.sqrt(x[len(x)-1]**2+y[len(y)-1]**2)

def symulacja(x,y,vx,vy,k1,k2,k3,dt,T):
    for i in T:
        r = mag(x,y)

        k2_f(x,y,k1,k2,r,dt)
        k3_f(x,y,k1,k2,k3,r,dt)
        k4_f(x,y,k1,k2,k3,r,dt)

        x.append(last(x) + (dt/6)*(last(k1[0])+2*last(k2[0])+2*last(k3[0])+last(k4[0])))
        y.append(last(y) + (dt/6)*(last(k1[1])+2*last(k2[1])+2*last(k3[1])+last(k4[1])))
        vx.append(last(vx) + (dt/6)*(last(k1[0])+2*last(k2[0])+2*last(k3[0])+last(k4[0])))
        vy.append(last(vy) + (dt/6)*(last(k1[1])+2*last(k2[1])+2*last(k3[1])+last(k4[1])))

        k1_f(x,y,vx,vy,k1,r,dt)

#MAIN
x = x0
y = y0
vx = vx0
vy = vy0

k1 = [vx0, vy0, [at(last(x0),mag(x0,y0))], [at(last(y0),mag(x0,y0))] ]
k2 = [[],[],[],[]]
k3 = [[],[],[],[]]
k4 = [[],[],[],[]]

dt = 3600
T = np.arange(0,h_okres,dt)


symulacja(x,y,vx,vy,k1,k2,k3,dt,T)
print(x)
print(y)


ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(x,y,'r.')
#ax1.plot(y,T)
plt.title('RK4 y(x)')
ax1.set_xlabel('x [m]')
ax1.set_ylabel('y [m]')
plt.show()
