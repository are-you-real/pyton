# rk4

import numpy as np
import matplotlib.pyplot as plt
import pylab

def ax(x,y):
    return -G*M*x/np.sqrt(x**2+y**2)
def ay(x,y):
    return -G*M*y/np.sqrt(x**2+y**2)

# stałe
au = 149597870700   #[m]
G = 6.6741*10**(-11)     # [m^3/kg/s^2]
M = 1.989*10**(30)      # [kg]

x = 0
x_plot = [x]
y = 0.586 *au
y_plot = [y]

vx = 54600
vy = 0

okres = 75*365*24*3600
dt = 3600
T = np.arange(0,okres,dt)

l =0
for i in T:
#for i in range(200):
    #print(l)
    l=l+1
    k11 = vx
    k12 = vy
    k13 = ax(x,y)
    k14 = ay(x,y)

    k21 = vx+dt*k13/2
    k22 = vy+dt*k14/2
    k23 = ax(x+dt*k11/2,y+dt*k12/2)
    k24 = ay(x+dt*k11/2,y+dt*k12/2)

    k31 = vx+dt*k23/2
    k32 = vy+dt*k24/2
    k33 = ax(x+dt*k21/2,y+dt*k22/2)
    k34 = ay(x+dt*k21/2,y+dt*k22/2)

    k41 = vx+dt*k33/2
    k42 = vy+dt*k34/2 # , ax(x+dt*k3[0]/2,y+dt*k3[1]/2), ay(x+dt*k3[0]/2,y+dt*k3[1]/2)]
    k43 = ax(x+(dt/2)*k31,y+(dt/2)*k32)
    k44 = ay(x+(dt/2)*k31,y+(dt/2)*k32)

    x = x +   (dt/6)*(k11 + 2*k21 + 2*k31 + k41)
    y = y +   (dt/6)*(k12 + 2*k22 + 2*k32 + k42)
    vx = vx + (dt/6)*(k13 + 2*k23 + 2*k33 + k43) # k4[2])
    vy = vy + (dt/6)*(k14 + 2*k24 + 2*k34 + k44) #k4[3])

    x_plot.append(x)
    y_plot.append(y)

x_plot = [a/au for a in x_plot]
y_plot = [a/au for a in y_plot]
T = [a/3600/24 for a in T]

x_plot.pop(len(x_plot)-1)
y_plot.pop(len(y_plot)-1)

ig1 = plt.figure()
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
ax1.plot(x_plot,y_plot) #, label='tol='+str(tol))
ax2.plot(T,y_plot) #, label='tol='+str(tol))
plt.title('RK4')
ax1.set_xlabel('x [au]')
ax1.set_ylabel('y [au]')
ax2.set_ylabel('y [au]')
ax2.set_xlabel('T [dni]')
plot_title = 'RK4.png'
plt.savefig(plot_title)
plt.show()
