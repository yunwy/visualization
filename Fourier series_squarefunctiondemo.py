import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


t = np.arange(-3*np.pi, 3*np.pi + 0.1, 0.1)

#Square function
def sqf(x):
    k = np.floor(x/np.pi)
    if k%2 == 0:
        return np.pi/2
    else:
        return -np.pi/2
        return -np.pi/2


#Coefficient
def coeff(n):
    return (1-np.cos(n*np.pi))/n


N_array = lambda n: np.arange(1, n + 1)

#Combine series
def Fourier(n):
    i = 1
    F = 0*t
    while i < n:
        F = F + coeff(i)*np.sin(i*t)
        i = i + 1
    return F


f1 = np.array(list(map(sqf, t)))
f2 = Fourier(2)
        
plt.figure(figsize=(10, 6))
plt.plot(t, f1, label='Square function')
Series,  = plt.plot(t, f2, label='Fourier Series')
plt.grid()
plt.legend()
plt.title('Fourier series of square function')
plt.xticks([-3*np.pi, -2*np.pi, -1*np.pi, 0, np.pi, 2*np.pi, 3*np.pi],
            ['$-3\pi$', '$-2\pi$', '$-\pi$', '$0$', '$\pi$',
            '$2\pi$','$3\pi$'])
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'])

#For slider bar
bar = plt.axes([0.13, 0.01, 0.74, 0.03])
slider = Slider(bar, 'n', 0, 200, valinit=2, valstep=1)

#Update value of n
def update(val):
    val_n = slider.val
    Series.set_ydata(Fourier(val_n))

slider.on_changed(update)

plt.show()
