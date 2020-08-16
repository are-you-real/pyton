#### ZAD2 ####

from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time


x01 = -0.7155980194664197
x02 = 2.8328820498299936
xs=[x01]
m=1
vs=[0]


def V_prim(x):
     return 2*x*np.exp(-x**2) + 2*(x-2)*1.2*np.exp(-(x-2)**2)
def polozenie(x,dt):
    x = x + vs[len(vs)-1]*dt
    return x
def predkosc(x,v):
    v = v - V_prim(x)*dt/m
    return v
def predkosc_zoporem(x,v,alfa,dt):
    v = v*(1-alfa*dt) - V_prim(x)*dt/m
    return v
def symulacja_zoporem(alfa,T,dt):
    for t in T:
        vs.append(predkosc_zoporem(xs[len(xs)-1],vs[len(vs)-1],alfa,dt))
        xs.append(polozenie(xs[len(xs)-1],dt))
def plot_ruch(T,xs,vs,Tmax,dt,alfa):
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(T, xs, label='polozenie [m]')
    ax.plot(T, vs, label='prednkosc [m/s]')
    plt.title('t=(0,'+str(Tmax)+'), dt='+str(dt)+',alfa='+str(alfa))
    ax.set_xlabel('czas [s]')
    plot_title = 'ruch_t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt)+'s.png'
    plt.savefig(plot_title)
    ax.legend()
def plot_energia(T,Ek,V,Ek_plus_V,Tmax,dt,alfa):
    fig1 = plt.figure()
    ax1 = plt.subplot(111)
    ax1.plot(T, Ek, label='Ek(t) [J]')
    ax1.plot(T, V, label='V(t) [J]')
    ax1.plot(T, Ek_plus_V, label='E_calkowita(t) [J]')
    plt.title('Zestawianie energii: t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__')
    ax1.set_xlabel('czas [s]')
    plot_title = 'energia_t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt)+'s.png'
    plt.savefig(plot_title)
    ax1.legend()

def symulacja_energia(xs,vs,T,Tmax,dt,alfa):
    minus_pow_list = lambda list : [-1*a*b for a,b in zip(list,list)]
    pow_list = lambda list : [a*b for a,b in zip(list,list)]

    xs_=[i-2 for i in xs]
    V = -np.exp(minus_pow_list(xs)) - 1.2*np.exp(minus_pow_list(xs_))
    Ek = [i*m/2 for i in  pow_list(vs)]
    Ek_plus_V = [a+b for a,b in zip(Ek,V)]
    plot_energia(T,Ek,V,Ek_plus_V,Tmax,dt,alfa)


def plot_portret(xs,vs,alfa,Tmax,dt):
    ig1 = plt.figure()
    ax1 = plt.subplot(111)
    ax1.plot(xs, vs)
    plt.title('portret fazowy t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt))
    ax1.set_xlabel('polozenie [m]')
    ax1.set_ylabel('predkosc [m/s]')
    plot_title = 'portret_t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt)+'s.png'
    plt.savefig(plot_title)

def plot_jeden_portret(xs,xs2,xs3,vs,vs2,vs3,alfa,Tmax,dt):
        ig1 = plt.figure()
        ax1 = plt.subplot(111)
        ax1.plot(xs, vs)
        ax1.plot(xs2, vs2)
        ax1.plot(xs3, vs3)
        plt.title('portret fazowy t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt))
        ax1.set_xlabel('polozenie [m]')
        ax1.set_ylabel('predkosc [m/s]')
        plot_title = 'portret_t_0__'+str(Tmax)+'__dt='+str(dt)+'_alfa__'+str(alfa)+'_dt__'+str(dt)+'s.png'
        plt.savefig(plot_title)


### MAIN ###

#>>>>>> x(t) i v(t)
#>>>>>>>> Ek(t),V(t) oraz Ek(t)+V(t) z uwzględnieniem oporu
#>>>>>>>> portret fazowy (x,v) bez oboru
#########################################
# Z OPOREM

#>>>>>1
alfa=0.5
xs=[x01]
vs=[0]

dt = 0.01
Tmax = 100
T = list(np.arange(0,Tmax,dt))
symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)
#>>>2

alfa=5
xs=[x01]
vs=[0]

dt = 0.01
Tmax = 100
T = list(np.arange(0,Tmax,dt))
symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)

#>>>>>3
alfa=201
xs=[x01]
vs=[0]

dt = 0.01
Tmax = 100
T = list(np.arange(0,Tmax,dt))
symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)


"""
# BEZ OPORU

xs=[x01]
vs=[0]

dt = 0.01
Tmax = 100
T = list(np.arange(0,Tmax,dt))
alfa=0
symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)

#>>>>>>>

xs=[x01]
vs=[0]

dt = 0.001
Tmax = 100
T = list(np.arange(0,Tmax,dt))

symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)
#>>>>>>>
xs=[x01]
vs=[0]

dt = 0.01
Tmax = 1000
T = list(np.arange(0,Tmax,dt))

symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)
#>>>>>>>
xs=[x01]
vs=[0]

dt = 0.001
Tmax = 1000
T = list(np.arange(0,Tmax,dt))

symulacja_zoporem(alfa,T,dt)
xs.pop(-1)
vs.pop(-1)
plot_ruch(T,xs,vs,Tmax,dt,alfa)

symulacja_energia(xs,vs,T,Tmax,dt,alfa)

plot_portret(xs,vs,alfa,Tmax,dt)
"""

plt.show()
