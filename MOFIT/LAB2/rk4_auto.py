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

dt = [360]
i = 0

tol=100
c=0.9

for i in [1000,100,10]:
    x_plot = []
    y_plot = []
    dt_plot = []
    tol = i
    T=0
    while T<=h_okres:
    #for i in T:
        x1 = pos(x,vx,dt[len(dt)-1])
        y1 = pos(y,vy,dt[len(dt)-1])
        #print(x1,y1)
        r = np.sqrt(x1**2 + y1**2)
        #vx1 = vel(vx,x1,r,dt[len(dt)-1])
        #vy1 = vel(vy,y1,r,dt[len(dt)-1])

        ## dt/2
        xa = pos(x,vx,dt[len(dt)-1]/2)
        ya = pos(y,vy,dt[len(dt)-1]/2)
        r = np.sqrt(xa**2 + ya**2)
        vxa = vel(vx,xa,r,dt[len(dt)-1]/2)
        vya = vel(vy,ya,r,dt[len(dt)-1]/2)
    #    print(xa,ya)

        xa = pos(xa,vxa,dt[len(dt)-1]/2)
        ya = pos(ya,vya,dt[len(dt)-1]/2)
        r = np.sqrt(xa**2 + ya**2)
        vxa = vel(vxa,xa,r,dt[len(dt)-1]/2)
        vya = vel(vya,ya,r,dt[len(dt)-1]/2)
    #    print('xa2',xa)

        ### spr
        eps = xa-x1
        epsy = ya-y1
        if abs(eps) < abs(epsy):
            eps = epsy
        if abs(eps)<=tol:
            x=xa
            y=ya
            vx=vxa
            vy=vya
            xend.append(x)
            yend.append(y)
            dt.append(c*dt[len(dt)-1]*abs(tol/eps)**(1/2))
        else:
            if eps != 0:
                dt[len(dt)-1]= c*dt[len(dt)-1]*abs(tol/eps)**(1/2)
            else:
                print('eps=0 dla i=',i)
            #dt.append(dt[len(dt)-1])
        T=T+i
        i = i+dt[len(dt)-1]

    #zamiana zmiennych
    r = [np.sqrt(a**2 + b**2) for a,b in zip(xend,yend)]
    xend = [a/au for a in xend]
    yend = [a/au for a in yend]
    dt = [a/60 for a in dt]
    x_plot.append(xend)
    y_plot.append(yend)
    dt_plot.append(dt)

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
ax1.plot(dt_plot[0],r)#,'r.')
ax2.plot(x_plot,y_plot)
plt.title('RK4')#'Euler y(x)')
ax1.set_xlabel(labelx)#'x [m]')
ax1.set_ylabel(labely)#'y [m]')
ax2.set_xlabel('x [m]')
ax2.set_ylabel('y [m]')
plot_title = title+'.png'
plt.savefig(plot_title)

plt.show()
