from math import exp, cos, pi
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.animation as anime
from time import sleep

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def u_t(u_0, v_0, a_0, dt):
    return u_0 + dt * v_0 + 1 / 2.0 * a_0 * pow(dt, 2)


def u_x(x):
    return 0
    return exp(-100 * (x - .5) ** 2)


def v(v_0, dt, a_0, a_1, a_2):
    return (v_0 + dt / 2.0 * (a_0 + a_1 + a_2))/(1 + beta[3] * dt)


def a(data, x, dx, t):
    return (data[x - 1][t] + data[x + 1][t] - 2 * data[x][t]) / pow(dx, 2) * 1.0


def a_beta(data, x, dx, t, v_t):
    return (data[x - 1][t] + data[x + 1][t] - 2 * data[x][t]) / pow(dx, 2) * 1.0 - 2 * beta[3] * v_t

def a_F(x, x_0, t):
    if x * d_x == x_0:
        return cos(pi / 2.0 * t * d_t) + cos(pi / 2.0 * (t + 1) * d_t)
    else:
        return 0


d_x = 0.01
d_t = 0.005
N_x = 101
N_t = int(10 / d_t)
u_data = []
v_data = []
a_data = []
time = [t * d_t for t in range(N_t)]
position = [i * d_x for i in range(N_x)]
beta = [.5, 2, 4, 1]

for i in position:
    u_data.append([u_x(i)] * N_t)
    v_data.append([0] * N_t)
    a_data.append([0] * N_t)
for t in range(1, N_t):
    for x in range(0, N_x):
        u_data[x][t] = u_t(u_data[x][t - 1], v_data[x][t - 1], a_data[x][t - 1], d_t)
    for x in range(0, N_x):
        if N_x - 1 > x > 0:
            a_data[x][t] = a_beta(u_data, x, d_x, t, v_data[x][t - 1])
        elif x == 0:
            a_data[x][t] = a_beta(u_data, x + 1, d_x, t, v_data[x][t - 1])
        elif x == N_x - 1:
            a_data[x][t] = a_beta(u_data, x - 1, d_x, t, v_data[x][t - 1])

    for x in range(1, N_x - 1):
        v_data[x][t] = v(v_data[x][t - 1], d_t, a(u_data, x, d_x, t), a_data[x][t - 1], a_F(x,0.5, t))


def plot_x_y(data_x, data_y, iterate):
    ax.plot(data_x, data_y, 'b')
    ax.set(xlabel='x [m]', ylabel="y [m]", title="")
    plt.ylim([-1, 1])
    plt.savefig("vel/veletra_const_" + str(iterate) + ".png")
    # sleep(0.2)
    #plt.show()
    #plt.close()


u_data_1 = []
for t in range(N_t):
    u_data_1.append([])
    for x in range(N_x):
        u_data_1[t].append(u_data[x][t])

time.append(0)

data = pd.DataFrame(data=u_data)
# data = data.pivot(index='x', columns='t', values='u')
sns.heatmap(u_data, cmap="YlGnBu")
#plt.show()
print(u_data)
period_list = [0]
for i in range(0, N_t):
    if u_data[50][0] - 0.00001 <= u_data[50][i] <= u_data[50][0] + 0.00001:
        period_list.append((i - period_list[-1]) * 2)

print(period_list)
