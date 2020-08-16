import numpy as np
import matplotlib.pyplot as plt
import math
from numba import jit
@jit(nopython=True)

def q(x):
     return np.pi**(-1/2)*math.exp(-x**2)

def ba():
     #Schemat Metropolisa
     In1 = np.array([])
     In2 = np.array([])
     In3 = np.array([])
     In4 = np.array([])
     xw = np.array([0])

     l = range(10**5)

     for i in l:
         if i==10**5-2 or i == 10**4 or i == 5*10**4:
             print(i)

         dx = np.random.uniform(-1/4,1/4)
         xwp = xw[len(xw)-1] + dx
         y = np.random.uniform(0,1)
         qw = q(xw[len(xw)-1])
         qwp = q(xwp)
         if y < qwp/qw:
             xw = np.append(xw,xwp)
         else:
             xw = np.append(xw,xw[len(xw)-1])
         In1 = np.append(In1,sum(xw)/(i+1))
         In2 = np.append(In2,sum(xw**2)/(i+1))
         In3 = np.append(In3,sum(xw**3)/(i+1))
         In4 = np.append(In4,sum(xw**4)/(i+1))


     # x,y
     ig1 = plt.figure()
     ax1 = plt.subplot(111)
     ax1.plot(l,In1,label='In1')
     ax1.plot(l,In2,label='In2')
     ax1.plot(l,In3,label='In3')
     ax1.plot(l,In4,label='In4')
     #ax1.plot(T,fi,label='obliczenia analityczne')
     #plt.title('tor')
     ax1.set_xlabel('l')
     ax1.set_xscale("log")
     ax1.set_ylabel('In')
     #plot_title = 'In.png'
     #plt.savefig(plot_title)
     ax1.legend()
     plt.show()
ba()
