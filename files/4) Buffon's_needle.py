import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd


N = int(input('바늘의 개수:'))
n = 0

x = rd.uniform(1, 7, N)
y = rd.uniform(1, 5, N)
t = rd.uniform(0, 2*np.pi, N)


def needle(i):
    needle = plt.plot([x[i], x[i] + np.cos(t[i])],
                      [y[i], y[i] + np.sin(t[i])])
    return needle


def line(x):
    return plt.plot([x, x], [0, 6], 'k')


lines = line(np.arange(9))
needles = needle(np.arange(N))

for needle in needles:
    check = [int(i) for i in needle.get_xdata()]

    if check[0] != check[1]:
        n += 1      

ax = plt.gca()
ax.margins(False)

print('Pi :', 2*N/n)
plt.show()
