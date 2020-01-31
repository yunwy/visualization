import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


mu = 3.5
dt = 0.01
t = np.arange(0, 50, dt)
x0, y0 = 0, 0.1


def vanderpol(mu, x0, y0):
    x = [x0]
    y = [y0]

    for _ in t:
        X, Y = x[-1], y[-1]
        x.append(X + Y*dt)
        y.append(Y + (mu*(1 - X**2)*Y - X)*dt)
        
    del x[-1], y[-1]

    return (x, y)


(xt, yt) = vanderpol(mu, x0, y0)

fig = plt.figure(figsize=(10, 5))
plt.subplots_adjust(bottom=0.25)

plt.subplot(1,2,1)
line = plt.plot(t, xt)[0]
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('$\ddot{x}-\mu(1-x^2)\dot{x}+x=0$')
plt.grid()

plt.subplot(1,2,2)
curve = plt.plot(xt, yt)[0]
plt.xlabel('$x(t)$')
plt.ylabel('$\dot{x}(t)$')
plt.title('Phase plane')
plt.grid()


ax_mu = plt.axes([0.13, 0.12, 0.74, 0.03])
ax_x0 = plt.axes([0.13, 0.07, 0.74, 0.03])
ax_y0 = plt.axes([0.13, 0.02, 0.74, 0.03])

slider_mu = Slider(ax_mu, '$\mu$', 0, 20.0, valinit=mu)
slider_x0 = Slider(ax_x0, '$x_0$', -2, 2, valinit=x0)
slider_y0 = Slider(ax_y0, '$\dot{x}_0$', -6, 6, valinit=y0)


def upd(val):
    val_mu = slider_mu.val
    val_x0 = slider_x0.val
    val_y0 = slider_y0.val
    
    update = vanderpol(val_mu, val_x0, val_y0)
    
    line.set_ydata(update[0])
    curve.set_xdata(update[0])
    curve.set_ydata(update[1])


slider_mu.on_changed(upd)
slider_x0.on_changed(upd)
slider_y0.on_changed(upd)

plt.show()
