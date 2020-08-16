#### Euler ####

#from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

au = 149597870700   #[m]
G = 6.6741*10**(-11)     # [m^3/kg/s^2]
M = 1.989*10**(30)      # [kg]
h_okres = 75*365*24*3600 #2375162222    # [s]

x0 = [0]
y0 = [8.766435223*10**(10)] #[m]
vx0 = [54600]
vy0 = [0]   #[m/s]
# funkcje

def pos_n1(x,y,vx,vy,dt):
    x.append(x[len(x)-1]+vx[len(vx)-1]*dt)
    y.append(y[len(y)-1]+vy[len(vy)-1]*dt)

def predkosc(x,y,vx,vy,r,dt):
    vx.append(vx[len(vx)-1]-G*M*x[len(x)-1]*dt/r**3)
    vy.append(vy[len(vy)-1]-G*M*y[len(y)-1]*dt/r**3)

def mag(x,y):
    return np.sqrt(x[len(x)-1]**2+y[len(y)-1]**2)

def symulacja(T,x,y,vx,vy,dt):
    for i in T:
        pos_n1(x,y,vx,vy,dt)
        r = mag(x,y)
        predkosc(x,y,vx,vy,r,dt)


def plot_euler(x,y,labelx,labely,title):
    ig1 = plt.figure()
    ax1 = plt.subplot(111)
    #(ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x,y)

    #ax2.plot(y,T)
    plt.title(title)#'Euler y(x)')
    ax1.set_xlabel(labelx)#'x [m]')
    ax1.set_ylabel(labely)#'y [m]')
    plot_title = title+'.png'
    plt.savefig(plot_title)
#MAIN
x = x0
y = y0
vx = vx0
vy = vy0
dt = 3600
T = np.arange(0,h_okres*3,dt)
symulacja(T,x,y,vx,vy,dt)
#print(np.delete(T,1))
xau=[x/au for x in x]
yau=[y/au for y in y]
T = [T/3600/24/365 for T in T]
xau = np.delete(xau,len(xau)-1)
yau = np.delete(yau,len(yau)-1)
plot_euler(T,yau,'t [lata]','y [m]','Euler y(t)')
plot_euler(xau,yau,'x [m]','y [m]','Euler y(x)')

plt.show()
print(len(x))
