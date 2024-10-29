import math
import numpy as np
import matplotlib.pyplot as plt

def RK4(f, x_0, t_0, t, n):
    delta_t = (t - t_0) / n

    t_i = t_0
    x_i = x_0

    for i in range(n):
        k1 = f(t_i, x_i)
        k2 = f(t_i + delta_t / 2, x_i + k1 * delta_t / 2)
        k3 = f(t_i + delta_t / 2, x_i + k2 * delta_t / 2)
        k4 = f(t_i + delta_t, x_i + k3 * delta_t)

        x_i += (delta_t / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t_i += delta_t

    return x_i

time = [t for t in np.linspace(-10, 10, 10)]
RK = [RK4(lambda t, x: x, 1, t, 0, 100) for t in time]

plt.plot(time, RK)
plt.show()