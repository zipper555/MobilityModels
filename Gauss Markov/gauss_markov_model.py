import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Set initial coordinates
x0 = 0
y0 = 0

# Initialize array of coordinates history
x_ac = [x0]
y_ac = [y0]

# Set initial angle and step size
angle = np.random.uniform(0,2*np.pi)
step = 0.1

def update(frame_number):
    global x0, y0, angle, step

    # Task 7.3.1
    x0 = x0 + step * np.cos(angle)
    y0 = y0 + step * np.sin(angle)
    
    x_ac.append(x0)
    y_ac.append(y0)
    
    angle = angle + 2*np.pi*np.random.normal()
    step = step + np.random.normal()
    #print "Angle: {} Step: {}".format(angle, step)

    ax.clear()
    plt.plot(x_ac, y_ac)
    plt.plot(x0,y0,'o')


# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, interval=10)
plt.show()