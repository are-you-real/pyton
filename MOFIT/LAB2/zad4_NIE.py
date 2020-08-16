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
y0 = [0.0586*au] #[m]
vx0 = [54600]
vy0 = [0]   #[m/s]
# funkcje
def last(x):
    return x[len(x)-1]

def pos_n1(x,y,vx,vy,dt):
    x.append(x[len(x)-1]+vx[len(vx)-1]*dt)
    y.append(y[len(y)-1]+vy[len(vy)-1]*dt)


def predkosc(x,y,vx,vy,r,dt):
    vx.append(vx[len(vx)-1]-G*M*x[len(x)-1]*dt/r**3)
    vy.append(vy[len(vy)-1]-G*M*y[len(y)-1]*dt/r**3)

def mag(x,y):
    return np.sqrt(x[len(x)-1]**2+y[len(y)-1]**2)

def symulacja(T,x,y,xa,ya,vx,vy,dt,r,tol):
    c=0.9
    vxbuf=vx
    vybuf=vy
    for i in T:
        pos_n1(x,y,vx,vy,last(dt))
        pos_n1(xa,ya,vx,vy,last(dt)/2)
        #print(last(r))
        #print(last(dt))
        rbuf=mag(xa,ya)
        predkosc(xa,ya,vxbuf,vybuf,rbuf,last(dt)/2)
        pos_n1(xa,ya,vxbuf,vybuf,last(dt)/2)
        # spr
        eps = last(xa)-last(x)
        epsy = last(ya)-last(y)
    #    print(last(x),last(xa))
    #    print(eps,epsy)
        if abs(eps) < abs(epsy):
            eps = epsy
        if abs(eps)<=tol:
            x[len(x)-1]=last(xa)
        r.append(mag(x,y))
        predkosc(x,y,vx,vy,last(r),last(dt))
        if eps != 0:
            dt.append(c*last(dt)*(tol/eps))
        else:
            print('eps=0 dla i=',i)
            dt.append(c*last(dt)*(tol/0.0001))

def plot_euler(x,y,labelx,labely,title):
    ig1 = plt.figure()
    ax1 = plt.subplot(111)
    ax1.plot(x,y,'r.')
    plt.title(title)#'Euler y(x)')
    ax1.set_xlabel(labelx)#'x [m]')
    ax1.set_ylabel(labely)#'y [m]')
    #plot_title = 'portret_t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt)+'s.png'
    #plt.savefig(plot_title)
#MAIN
x = x0
y = y0
xa = x
ya = y

vx = vx0
vy = vy0
dt = [36000]
T = np.arange(0,h_okres*3,last(dt))
r=[mag(x,y)]
tol=1000
symulacja(T,x,y,xa,ya,vx,vy,dt,r,tol)
#print(np.delete(T,1))
xau=[x/au for x in x]
yau=[y/au for y in y]
xau = np.delete(xau,len(xau)-1)
yau = np.delete(yau,len(yau)-1)
plot_euler(dt,r,'dt [s]','r [m]','Euler y(x)')
plot_euler(xau,yau,'x [m]','y [m]','Euler y(x)')

plt.show()
print(len(x))
