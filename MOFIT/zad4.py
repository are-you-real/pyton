#### ZAD4 ####

from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

xn = -0.7155980194664197
xn1 = xn
xs = [xn]
vn = 0
vn1 = 0
vs = [vn]
m=1
dt = 0.001
alfa=0
T = list(np.arange(0,30,dt))

def V_prim(x):
     return 2*x*np.exp(-x**2) + 2*(x-2)*1.2*np.exp(-(x-2)**2)

F1 = xn1-xn-dt*(vn-vn1)/2
xn = xn1
xn1 = xn-F1
xs.append(xn1)
F2 = vn1-vn-dt*(-V_prim(xn1)/m-alfa*vn1-V_prim(xn)-alfa*vn)/2
vn1 = vn -F2
vn = vn1
vs.append(vn1)

for i in T:
    F1 = xn1-xn-dt*(vn-vn1)/2
    xn = xn1
    xn1 = xn-F1
    xs.append(xn1)
    F2 = vn1-vn-dt*(-V_prim(xn1)/m-alfa*vn1-V_prim(xn)-alfa*vn)/2
    vn1 = vn -F2
    vn = vn1
    vs.append(vn1)


xs.pop(-1)
vs.pop(-1)

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
