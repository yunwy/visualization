import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp


mu = 2
dt = 0.01
t = np.arange(0, 50, dt)
x0, v0 = 0, 0.1


def vanderpol(t, z, mu):
    x, v = z
    return [v, mu*(1 - x**2)*v - x]


sol = solve_ivp(vanderpol, (t[0], t[-1]), (x0, v0),
                args=[mu], method='RK45', dense_output=True)
z = sol.sol(t)

fig = plt.figure(figsize=(10, 5))
plt.subplots_adjust(bottom=0.25)

ax1 = plt.subplot(1,2,1)
ax1.set_ylim([-3, 3])
line = plt.plot(t, z[0])[0]
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('$\ddot{x}-\mu(1-x^2)\dot{x}+x=0$')
plt.grid()

ax2 = plt.subplot(1,2,2)
ax2.set_ylim([-7, 7])
curve = plt.plot(z[0], z[1])[0]
plt.xlabel('$x(t)$')
plt.ylabel('$\dot{x}(t)$')
plt.title('Phase plane')
plt.grid()


ax_mu = plt.axes([0.13, 0.12, 0.74, 0.03])
ax_x0 = plt.axes([0.13, 0.07, 0.74, 0.03])
ax_v0 = plt.axes([0.13, 0.02, 0.74, 0.03])

slider_mu = Slider(ax_mu, '$\mu$', 0, 4, valinit=mu)
slider_x0 = Slider(ax_x0, '$x_0$', -2, 2, valinit=x0)
slider_v0 = Slider(ax_v0, '$\dot{x}_0$', -6, 6, valinit=v0)


def upd(val):
    val_mu = slider_mu.val
    val_x0 = slider_x0.val
    val_v0 = slider_v0.val
    
    update = solve_ivp(vanderpol, (t[0], t[-1]), (val_x0, val_v0),
                        args=[val_mu], method='RK45', dense_output=True)
    z = update.sol(t)
    
    line.set_ydata(z[0])
    curve.set_xdata(z[0])
    curve.set_ydata(z[1])
    

slider_mu.on_changed(upd)
slider_x0.on_changed(upd)
slider_v0.on_changed(upd)

plt.show()
