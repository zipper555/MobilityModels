import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

pursuer = None
pursued = None

# Select theme
theme_football = True
if theme_football:
    pursuer = plt.imread('player.png')
    pursued = plt.imread('ball.png')
else:
    pursuer = plt.imread('duckli.png')
    pursued = plt.imread('duck.png')

im = OffsetImage(pursuer, zoom=0.5)
im2 = OffsetImage(pursued, zoom=0.5)


# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Set initial positions of pursued and pursuers
x_pursued0 = 0
y_pursued0 = 0

x_pursuer1 = 10
y_pursuer1 = 10

x_pursuer2 = 10
y_pursuer2 = -10

x_pursuer3 = -10
y_pursuer3 = 10

# Initialize array of coordinates history
x_ac = [x_pursued0]
y_ac = [y_pursued0]

# Select initial angle and step
angle = np.random.uniform(0,2*np.pi)
step = 1

# Auxiliary variables
lx,ux = -20,20
ly,uy = 20,20

def update(frame_number):
    global x_pursued0, y_pursued0, angle, step, x_pursuer1, y_pursuer1, x_pursuer2, y_pursuer2, x_pursuer3, y_pursuer3, lx, ux, ly, uy
    # Task 7.4.1
    x_pursued0 = x_pursued0 + step * np.cos(angle)
    y_pursued0 = y_pursued0 + step * np.sin(angle)
    
    dx = np.random.rand()
    x_pursuer1 = x_pursued0 - 0.5 * dx
    x_pursuer2 = x_pursuer1 - 1.5 * dx
    x_pursuer3 = x_pursuer2 - 2.5 * dx
    
    dy = np.random.rand()
    y_pursuer1 = y_pursued0 - 0.5 * dy
    y_pursuer2 = y_pursuer1 - 1.5 * dy
    y_pursuer3 = y_pursuer2 - 2.5 * dy

    x_ac.append(x_pursued0)
    y_ac.append(y_pursued0)
    
    angle = 2*np.pi*np.random.randn()
    step = np.random.randn()

    ax.clear()
    plt.plot(x_ac, y_ac)
    plt.plot(x_pursued0, y_pursued0, 'o')
    
    # Move the axes when the points move away
    if not lx < x_pursued0 < ux:
        lx = x_pursued0 - 20
        ux = x_pursued0 + 20
    if not ly < y_pursued0 < uy:
        ly = y_pursued0 - 20
        uy = y_pursued0 + 20
    ax.patch.set_alpha(0)
    ax.set_xlim(lx, ux)
    ax.set_ylim(ly, uy)

    ab1 = AnnotationBbox(im, (x_pursuer1, y_pursuer1), xycoords='data', frameon=False)
    ab2 = AnnotationBbox(im, (x_pursuer2, y_pursuer2), xycoords='data', frameon=False)
    ab3 = AnnotationBbox(im, (x_pursuer3, y_pursuer3), xycoords='data', frameon=False)
    ab0 = AnnotationBbox(im2, (x_pursued0, y_pursued0), xycoords='data', frameon=False)
    ax.add_artist(ab1)
    ax.add_artist(ab2)
    ax.add_artist(ab3)
    ax.add_artist(ab0)
    
# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, interval=100)
plt.show()