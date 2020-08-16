#### ZAD2 ####

from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

class Z2:
    x01 = -0.7155980194664197
    x02 = 2.8328820498299936
    T = list(range(0,31))
    xs=[x01]
    m=1
    vs=[0]
    dt = 0.1
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
    def symulacja():
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
S=Z2()
Z2.symulacja()

Z2.xs.pop(-1)
Z2.vs.pop(-1)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(Z2.T, Z2.xs, label='polozenie [m]')
ax.plot(Z2.T, Z2.vs, label='prednkosc [m/s]')
plt.title('zleznosc polozenia oraz pradkosci od czasu (bez oporu)')
ax.set_xlabel('czas [s]')
ax.legend()


"""
>>>>>>>> Ek(t),V(t) oraz Ek(t)+V(t) bez oboru
"""
minus_pow_list = lambda list : [-1*a*b for a,b in zip(list,list)]
pow_list = lambda list : [a*b for a,b in zip(list,list)]
Z2.xs_=[i-2 for i in Z2.xs]
Z2.V = -np.exp(minus_pow_list(Z2.xs)) - 1.2*np.exp(minus_pow_list(Z2.xs_))
Ek = [i*m/2 for i in  pow_list(Z2.vs)]
Ek_plus_V = [a*b for a,b in zip(Ek,V)]

fig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(T, Ek, label='Ek(t) [J]')
ax1.plot(T, V, label='V(t) [J]')
ax1.plot(T, Ek_plus_V, label='Ek+V(t) [J]')
plt.title('Zestawianie energii potencjalnej i kinetycznej (bez oporu)')
ax1.set_xlabel('czas [s]')
ax1.legend()

##############################################################################
"""
>>>>>>>> x(t) i v(t) z uwzględnieniem oporu
"""
symulacja_zoporem()

xs.pop(-1)
vs.pop(-1)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(T, xs, label='polozenie [m]')
ax.plot(T, vs, label='prednkosc [m/s]')
plt.title('zleznosc polozenia oraz pradkosci od czasu (z uwzględnieniem oporu )')
ax.set_xlabel('czas [s]')
ax.legend()

"""
>>>>>>>> Ek(t),V(t) oraz Ek(t)+V(t) z uwzględnieniem oporu
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
plt.title('Zestawianie energii potencjalnej i kinetycznej (z uwzględnieniem oporu)' )
ax1.set_xlabel('czas [s]')
ax1.legend()



plt.show()
