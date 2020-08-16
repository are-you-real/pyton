import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

au = 149597870700   #[m]
G = 6.6741*10**(-11)     # [m^3/kg/s^2]
#G = G * 3600 / au**3           # [au^3/kg/min]
M = 1.989*10**(30)      # [kg]

# funkcje
def pos(x,vx,dt):
    return x + vx*dt

def vel(v,x,r,dt):
    return v-G*M*x*dt/r**3

##########################



h_okres = 75*365*24*3600 #2375162222    # [s]
#h_okres = h_okres/60 #[min]

xend = [0]
yend = [0.056*au] #[m]
#yend[0] = yend[0] / au
vx = 54600 #* 60 / au
vy = 0                     #[au/s]

x = 0
y = yend[len(xend)-1]
xa = x
ya = y
vxa = vx
vya = vy

dt = 3600
i = 0

tol=100
c=0.9

print(x,y)
T=0
while T<=h_okres:
#for i in T:
    x = pos(x,vx,dt)
    y = pos(y,vy,dt)
    #print(x1,y1)
    r = np.sqrt(x**2 + y**2)
    vx = vel(vx,x,r,dt)
    vy = vel(vy,y,r,dt)

    xend.append(x)
    yend.append(y)

#zamiana zmiennych
r = [np.sqrt(a**2 + b**2) for a,b in zip(xend,yend)]
xend = [a/au for a in xend]
yend = [a/au for a in yend]
dt = [a/60 for a in dt]

print(T)
title='dfs'
labelx='r'
labely='dt[min]'
#print(r)
#print(dt)
#print(xend)
ig1 = plt.figure()
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
ax1.plot(dt,r)#,'r.')
ax2.plot(x,y)
plt.title(title)#'Euler y(x)')
ax1.set_xlabel(labelx)#'x [m]')
ax1.set_ylabel(labely)#'y [m]')
ax2.set_xlabel('x [m]')
ax2.set_ylabel('y [m]')

plt.show()
