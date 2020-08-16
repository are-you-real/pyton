# Lab1 Zad1

from numba import jit
import numpy as np
import time

import matplotlib.pyplot as plt
import pylab


timeZ1AStart = time.time()

### Constants ###
E = -0.6 # [J]
m = 1 #[kg]
v0 = 0
#################
# equation #
# V(x) = −exp(−x^2)−1.2 exp(−(x−2)^2)
# f = −exp(−x^2)−1.2 exp(−(x−2)^2) - E

# 1.1 a %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## szukamy pkt 0 dla funkcji 'f'
### szukamy 3 punkty dające nam 2 przedziały w których są punkty zerowe
f = lambda x : -np.exp(-x**2) - 1.2*np.exp(-(x-2)**2) - E
print(f(-20))
print(f(-10))
print(f(0))
print(f(10))
print(f(20))

### szukamy pkt 0 w przedziałach (a,b) oraz (b,c)
a = -10
b = 0
c = 10
# pierwiastek w (a,b) $$$$$$$$$$$$$$$$$$$$$$$$$$
x0 = [(a+b)/2]
f0 = f(x0[len(x0)-1])
T=1
# f0 musi przyjmować wartość nie dodatnią aby V(x)<=E
while f0 != 0:
    T=T+1
    if f(a)*f0 < 0:
        b = x0[len(x0)-1]
    elif f0*f(b) < 0:
        a = x0[len(x0)-1]
    else:
        print("ERROR: f(a),f(x0) oraz f(b) mają ten sam znak")
    x0.append((a+b)/2)
    f0=f(x0[len(x0)-1])

#--- pierwszy pkt zero x01 przyjmuje wartosc f01
f01 = f0
x01 = x0
print("x01=",x01[len(x0)-1])
print("liczba kroków=",T)

T = list(np.arange(T))


fig = plt.figure()
ax = plt.subplot(311)
ax.plot(T, x0, label='punkt zerowy', marker='o')
plt.title('tempo zbieżności rozwiązania w przedziale (a,b)')
ax.set_xlabel('krok')
ax.set_ylabel('wartość x0')
#ax.legend()



# pierwiastek w (b,c) $$$$$$$$$$$$$$$$$$$$$$$$$$
b = 0
x0 = [(b+c)/2]
f0 = f(x0[len(x0)-1])
# f0 musi przyjmować wartość nie dodatnią aby V(x)<=E
T=1
while f0 != 0:
    T = T + 1
    if f(b)*f0 < 0:
        c = x0[len(x0)-1]
    elif f0*f(c) < 0:
        b = x0[len(x0)-1]
    else:
        print("ERROR: f(a),f(x0) oraz f(b) mają ten sam znak")
    x0.append((b+c)/2)
    f0=f(x0[len(x0)-1])

f02 = f0 #--- drugi pkt zero x02 przyjmuje wartosc f02
x02 = x0 #*
print("x02=",x02[len(x0)-1])
print("liczba kroków=",T)

T = list(np.arange(T))
#fig = plt.figure()
ax = plt.subplot(313)
ax.plot(T, x0, label='punkt zerowy', marker='o')
plt.title('tempo zbieżności rozwiązania w przedziale (b,c)')
ax.set_xlabel('krok')
ax.set_ylabel('wartość x0')
plot_title = "tempo_zbieżności_rozwiązan" + ".png"
plt.savefig(plot_title)

plt.show()

timeZ1AEnd = time.time()
print("czas działania Zad1 a=",timeZ1AEnd - timeZ1AStart,"sekunt")
"""
# 1.1 b %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
timeZ1BStart = time.time()
a = -10
b = 0
c = 10
# pierwiastek w (a,b) $$$$$$$$$$$$$$$$$$$$$$$$$$
x0 = [-1]
f0 = f(x0)
f_prim = lambda x : 2*x*np.exp(-x**2) + 2*(x-2)*1.2*np.exp(-(x-2)**2)
print("fp0=",f_prim(x0))
fp0 = f_prim(x0)

#while f0 != 0 or fp0 != 0:
for i in range(30):
    fp0 = f_prim(x0[len(x0)-1])
    #print("fp0=",fp0)
    #print("x0=",x0)
    print(f(x0)/f_prim(x0))
    x0.append(x0 - f(x0[len(x0)-1])/f_prim(x0[len(x0)-1]))

print("x0=",x0)
#print("1.1b->",f0,"--",x0)

timeZ1BEnd = time.time()
#print("czas działania Zad1 b=",timeZ1BEnd - timeZ1BStart,"sekunt")

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
