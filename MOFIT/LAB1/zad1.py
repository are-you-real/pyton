# Lab1 Zad1

from numba import jit
import numpy as np
import time

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
b = -0
c = 10
# pierwiastek w (a,b) $$$$$$$$$$$$$$$$$$$$$$$$$$
x0 = (a+b)/2
f0 = f(x0)
# f0 musi przyjmować wartość nie dodatnią aby V(x)<=E
while f0 != 0:
    if f(a)*f0 < 0:
        b = x0
    elif f0*f(b) < 0:
        a = x0
    else:
        print("ERROR: f(a),f(x0) oraz f(b) mają ten sam znak")
    x0 = (a+b)/2
    f0=f(x0)
print(f0,"--",x0)
#--- pierwszy pkt zero x01 przyjmuje wartosc f01
f01 = f0
x01 = x0

# pierwiastek w (b,c) $$$$$$$$$$$$$$$$$$$$$$$$$$
x0 = (b+c)/2
f0 = f(x0)
# f0 musi przyjmować wartość nie dodatnią aby V(x)<=E
while f0 != 0:
    if f(b)*f0 < 0:
        c = x0
    elif f0*f(c) < 0:
        b = x0
    else:
        print("ERROR: f(a),f(x0) oraz f(b) mają ten sam znak")
    x0 = (b+c)/2
    f0=f(x0)
print(f0,"--",x0)

f02 = f0 #--- drugi pkt zero x02 przyjmuje wartosc f02
x02 = x0 #*

timeZ1AEnd = time.time()
print("czas działania Zad1 a=",timeZ1AEnd - timeZ1AStart,"sekunt")

# 1.1 b %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
timeZ1BStart = time.time()
a = -10
b = 0
c = 10
# pierwiastek w (a,b) $$$$$$$$$$$$$$$$$$$$$$$$$$
x0 = -1
f0 = f(x0)
f_prim = lambda x : 2*x*np.exp(-x**2) + 2*(x-2)*1.2*np.exp(-(x-2)**2)
print("fp0=",f_prim(x0))
fp0 = f_prim(x0)

#while f0 != 0 or fp0 != 0:
for i in range(30):
    fp0 = f_prim(x0)
    print("fp0=",fp0)
    print("x0=",x0)
    print(f(x0)/f_prim(x0))
    x0 = x0 - f(x0)/f_prim(x0)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  SPR czemu wywala 1.1b ???!!!!!
print("1.1b->",f0,"--",x0)

timeZ1BEnd = time.time()
print("czas działania Zad1 b=",timeZ1BEnd - timeZ1BStart,"sekunt")
