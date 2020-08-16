
import numpy as np
import matplotlib.pyplot as plt
import math
siz=10**7
def q(x):
    return np.pi**(-1/2)*math.exp(-x**2)

#Schemat Metropolisa
#In1 = np.array([])
In1 = np.zeros(siz)
In2 = np.zeros(siz)
In3 = np.zeros(siz)
In4 = np.zeros(siz)
xw = np.zeros(siz+1)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0


l = range(siz)

for i in l:
    if i==10**5-2 or i == 10**4 or i == 5*10**4:
        print(i)
    dx = np.random.uniform(-1/4,1/4)
    xwp = xw[i] + dx
    y = np.random.uniform(0,1)
    qw = q(xw[i])
    qwp = q(xwp)
    if y < qwp/qw:
        #xw = np.append(xw,xwp)
        xw[i+1] = xwp
    else:
        xw[i+1] = xw[i]
    sum1 = sum1+xw[i+1]
    sum2 = sum2+xw[i+1]**2
    sum3 = sum3+xw[i+1]**3
    sum4 = sum4+xw[i+1]**4

    In1[i] = sum1/(i+1)
    In2[i] = sum2/(i+1)
    In3[i] = sum3/(i+1)
    In4[i] = sum4/(i+1)

lim1 = np.zeros(siz)
lim1 = lim1 + In1[len(In1)-1]
lim2 = np.zeros(siz) + In2[len(In2)-1]
lim3 = np.zeros(siz) + In3[len(In3)-1]
lim4 = np.zeros(siz) + In4[len(In4)-1]
# x,y
ig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.plot(l,In1,label='In1')
#ax1.plot(l,lim1,'--')
ax1.plot(l,In2,label='In2')
#ax1.plot(l,lim2,'--')
ax1.plot(l,In3,label='In3')
#ax1.plot(l,lim3,'--')
ax1.plot(l,In4,label='In4')
#ax1.plot(l,lim4,'--')

#plt.title('tor')
ax1.set_xlabel('l')
ax1.set_xscale("log")
ax1.set_ylabel('In')
plot_title = 'In.png'
plt.savefig(plot_title)
ax1.legend()
plt.show()
