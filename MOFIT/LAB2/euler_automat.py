#euler czas

import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

# stałe
au = 149597870700   #[m]
G = 6.6741*10**(-11)     # [m^3/kg/s^2]
M = 1.989*10**(30)      # [kg]

ig1 = plt.figure()
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

for i in [1000,100,10]:
    tol = i

    x = 0
    x_plot = [x]
    y = 0.586*au
    y_plot = [y]

    vx = 54600
    vy = 0

    dt = 3600
    dtn = [dt]
    okres = 75*365*24*3600
    T = 0
    c=0.9

    while T<=2*okres:
        # u
        xn = x + vx*dt
        yn = y + vy*dt
        r=np.sqrt(x**2+y**2)
        vxn = vx - G*M*xn*(dt/2)/(r**3)
        vyn = vy - G*M*yn*(dt/2)/(r**3)
    #    print('xn=',xn)
    #    print('yn=',yn)
    #    print('vy=',vy)

        # u'
        xp = x + vx*(dt/2)
        yp = y + vy*(dt/2)
        rp = np.sqrt(xp**2+yp**2)
        vxp = vx - G*M*xp*(dt/2)/(rp**3)
        vyp = vy - G*M*yp*(dt/2)/(rp**3)
    #    print(xp)
    #    print(yp)
        xp2 = xp + vxp*dt/2
        yp2 = yp + vyp*dt/2
        rp2 = np.sqrt(xp**2+yp**2)
        vxp2 = vxp - G*M*xp2*dt/2/(rp2**3)
        vyp2 = vyp - G*M*yp2*dt/2/(rp2**3)
    #    print('xp2=',xp2)
    #    print('yp2=',yp2)
        # warunki
        epsx = xn-xp2
        epsy = yn-yp2
    #    print('epsx',epsx)
    #    print('epsy',epsy)

        if abs(epsx) < abs(epsy):
            eps = epsy
        else:
            eps = epsx

        if abs(eps)<=tol:
        #    print("in")
            x = xp2
            y = yp2
            vx = vxp2
            vy = vyp2
            x_plot.append(x)
            y_plot.append(y)
            dtn.append(dt)
            T = T + dt

    #    print('eps',eps)
    #    print('dt',dt)
    #    print('sqrt=',np.sqrt(abs(tol/eps)))
        dt = c*dt*np.sqrt(abs(tol/eps))
        #print('dt_new2',dt)
    #    print(' ')

    # zamiana zmiennych
    x_plot = [a/au for a in x_plot]
    y_plot = [a/au for a in y_plot]
    r = [np.sqrt(a**2+b**2) for a,b in zip(x_plot,y_plot)]

    x_plot.pop(0)
    y_plot.pop(0)
    r.pop(0)
    dtn=np.delete(dtn,0)
    print(dtn[0])
    print(x_plot[1],y_plot[1],r[1])
    print(y_plot[len(y_plot)-1])

    ax1.plot(x_plot,y_plot, label='tol='+str(tol))
    ax2.plot(r,dtn, label='tol='+str(tol))
    plt.title('Euler y(x)')
    ax1.set_xlabel('x [m]')
    ax1.set_ylabel('y [m]')
    ax2.set_xlabel('r [m]')
    ax2.set_ylabel('dt [s]')


ax1.legend()
ax2.legend()
plot_title = 'eulerczas_tol'+str(tol)+'.png'
plt.savefig(plot_title)
plt.show()
