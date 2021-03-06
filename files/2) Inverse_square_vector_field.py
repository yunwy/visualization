import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


n = 25
X = np.linspace(-2, 2, n)
Y = np.linspace(-2, 2, n)
x, y = np.meshgrid(X, Y)

command = {'left':np.array([-0.1, 0]),
           'right':np.array([0.1, 0]),
           'up':np.array([0, 0.1]),
           'down':np.array([0, -0.1])}

fig= plt.figure(figsize=[9, 7])
ax = plt.axes(xlim = (-2, 2), ylim = (-2, 2))
plt.title('$ \\vec{F} = \\frac{k}{r^2} \\hat{r} $')
ax.set_aspect('equal')

circle = plt.Circle((0,0), 0.05, fc = 'k')
circle.center = np.array([0.0, 0.0])
ax.add_patch(circle)


def Field(x, y, x0=0, y0=0, k=1, s=1):
    rx = x - x0
    ry = y - y0
    r = np.sqrt(rx**2 + ry**2 + 0.01)
    return s*rx/r, s*ry/r, k/r**2


def upd1(event):
    try:
        global xp, yp
        circle.center += command[event.key]
        xp = circle.center[0]
        yp = circle.center[1]

        v1, v2, intense = Field(x, y, x0=xp, y0=yp, k=val_k, s=sdata)
        vec.set_UVC(v1, v2, C=intense)
        plt.draw()

    except:
        pass


def upd2(event):
    if event.inaxes != ax:
        pass
        
    else:
        global xp, yp
        xp = event.xdata
        yp = event.ydata

        circle.center[0] = xp
        circle.center[1] = yp

        v1, v2, intense = Field(x, y, x0=xp, y0=yp, k=val_k, s=sdata)
        vec.set_UVC(v1, v2, C=intense)
        plt.draw()


def upd_intensity(val):
    global val_k
    val_k = slider.val
    v1, v2, intensity = Field(x, y, x0=xp, y0=yp, k=val_k, s=sdata)
    vec.set_UVC(v1, v2, C=intensity)


def upd_sign(label):
    signdict = {'k > 0':1, 'k < 0':-1}
    global sdata
    sdata = signdict[label]
    
    v1, v2, intensity = Field(x, y, x0=xp, y0=yp, k=val_k, s=sdata)
    vec.set_UVC(v1, v2)
    plt.draw()


u1, u2, Intensity = Field(x, y)
vec = ax.quiver(x, y, u1, u2, Intensity, cmap='cool')

fig.colorbar(vec, shrink = 0.5, aspect = 5) 
xp, yp = 0, 0

bar = plt.axes([0.1, 0.02, 0.74, 0.03])
slider = Slider(bar, '|k|', 0, 100, valinit=1)

button = plt.axes([0.77, 0.09, 0.17, 0.17])
radio = RadioButtons(button, ('k > 0', 'k < 0'))

val_k, sdata = 1, 1

slider.on_changed(upd_intensity)
radio.on_clicked(upd_sign)
fig.canvas.mpl_connect('key_press_event', upd1)
fig.canvas.mpl_connect('button_press_event', upd2)


plt.show()
