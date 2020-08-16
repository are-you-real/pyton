import numpy as np
import matplotlib.pyplot as plt
import math

siz=10**5
def q(x,y):
    return np.pi**(-1)*math.exp(-(x**2+y**2))

#Schemat Metropolisa
xw = np.zeros(siz+1)
yw = np.zeros(siz+1)
E = np.zeros(siz)

sum = 0

l = range(siz)

for i in l:
    dx = np.random.uniform(-1/4,1/4)
    dy = np.random.uniform(-1/4,1/4)
    xwp = xw[i] + dx
    ywp = yw[i] + dy
    los = np.random.uniform(0,1)
    qw = q(xw[i],yw[i])
    qwp = q(xwp,ywp)

    if los < qwp/qw:
        xw[i+1] = xwp
        yw[i+1] = ywp
    else:
        xw[i+1] = xw[i]
        yw[i+1] = yw[i]

#    sum = sum + (xw[i+1]**2+xw[i+1]**2)/2
#    E[i] = sum/(i+1)

#lim = np.zeros(siz) + E[len(E)-1]

# x,y
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(xw,yw)

plt.title('xy_dla_'+str(siz)+'_kroków')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
plot_title = 'hamilton_'+str(siz)+'.png'
plt.savefig(plot_title)

'''
########################### E
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(l,E,label='In1')
ax1.plot(l,lim,'--')

#plt.title('tor')
ax1.set_xlabel('krok')
ax1.set_xscale("log")
ax1.set_ylabel('E')
plot_title = 'E_hamilton.png'
plt.savefig(plot_title)
'''
plt.show()
