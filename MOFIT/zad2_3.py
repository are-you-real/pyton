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
dt = 0.001


#T = list(range(0,30,dt2))
#T = list(range(0,30,dt3))
alfa=0.3
def V_prim(x):
     return 2*x*np.exp(-x**2) + 2*(x-2)*1.2*np.exp(-(x-2)**2)
def polozenie(x):
    x = x + vs[len(vs)-1]*dt
    return x
def predkosc(x,v):
    v = v - V_prim(x)*dt/m
    return v
def predkosc_zoporem(x,v):
    v = v*(1-alfa*dt) - V_prim(x)*dt/m
    return v
def symulacja(T):
    for t in T:
        vs.append(predkosc(xs[len(xs)-1],vs[len(vs)-1]))
        xs.append(polozenie(xs[len(xs)-1]))
def symulacja_zoporem():
    for t in T:
        vs.append(predkosc_zoporem(xs[len(xs)-1],vs[len(vs)-1]))
        xs.append(polozenie(xs[len(xs)-1]))
### MAIN ###
"""
>>>>>>>> x(t) i v(t) bez oboru
"""

T = list(np.arange(0,100,dt))
symulacja()

xs.pop(-1)
vs.pop(-1)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(T, xs, label='polozenie [m]')
ax.plot(T, vs, label='prednkosc [m/s]')
plt.title('zleznosc polozenia oraz pradkosci od czasu (bez oporu)')
ax.set_xlabel('czas [s]')
plot_title = "czas_i_polozenie_bez_oporu_" +  str(dt) + "s.png"
plt.savefig(plot_title)
ax.legend()

"""
>>>>>>>> Ek(t),V(t) oraz Ek(t)+V(t) bez oboru
"""
minus_pow_list = lambda list : [-1*a*b for a,b in zip(list,list)]
pow_list = lambda list : [a*b for a,b in zip(list,list)]
xs_=[i-2 for i in xs]
V = -np.exp(minus_pow_list(xs)) - 1.2*np.exp(minus_pow_list(xs_))
Ek = [i*m/2 for i in  pow_list(vs)]
Ek_plus_V = [a*b for a,b in zip(Ek,V)]

fig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T, Ek, label='Ek(t) [J]')
ax1.plot(T, V, label='V(t) [J]')
ax1.plot(T, Ek_plus_V, label='Ek+V(t) [J]')
plt.title('Zestawianie energii potencjalnej i kinetycznej (bez oporu)')
ax1.set_xlabel('czas [s]')
plot_title = "Zestawianie_energii_potencjalnej_i_kinetycznej_bezoporu_" +  str(dt) + "_s.png"
plt.savefig(plot_title)
ax1.legend()

"""
>>>>>>>> portret fazowy (x,v) bez oboru
"""
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(xs, vs)
plt.title('portret fazowy (bez oporu)')
ax1.set_xlabel('polozenie [m]')
ax1.set_ylabel('predkosc [m/s]')
plot_title = "portret_fazowy_bez_oboru_z_krokiem_" +  str(dt) + "_s.png"
plt.savefig(plot_title)

ax1.legend()


plt.show()
