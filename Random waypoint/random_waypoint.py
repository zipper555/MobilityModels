import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-1, 1), ax.set_xticks([])
ax.set_ylim(-1, 1), ax.set_yticks([])

# Set initial coordinates
x0 = 0
y0 = 0

# Set current coordinates
x_curr = x0
y_curr = y0

# Initialize array of coordinates history
x_ac = [x0]
y_ac = [y0]


# Initialize destination coordinates
xd = x0
yd = y0

# Set number and index of steps
n_steps = 20
step_i = 0

# Set waiting parameters
waiting = True
n_waiting = 5
wait_i = 0

delta_x = 0
slope = 0
y_intercept = 0

def update(frame_number):
    global step_i, waiting, wait_i, x_curr, y_curr, x0, y0, xd, yd, delta_x, slope, y_intercept
    
    if not waiting and xd!=x0:
        if step_i < n_steps:
            # Task 7.1.1
            x_curr = x_curr + delta_x
            y_curr = slope * x_curr + y_intercept
            step_i += 1
        else:

            # Task 7.1.1
            step_i = 0
            waiting = True

        # Accumulate coordinates
        #print "Updating x_curr: {} y_curr: {}".format(x_curr, y_curr)
        x_ac.append(x_curr)
        y_ac.append(y_curr)

    else:
        if wait_i <= n_waiting:
            wait_i += 1
        else:
            wait_i = 0
            # Task 7.1.1
            xd = np.random.uniform(-1,1)
            yd = np.random.uniform(-1,1)
            x0 = x_curr
            y0 = y_curr
            slope = float(y0 - yd)/(x0 - xd)
            y_intercept = yd - slope * xd
            delta_x = (xd - x0)/20.0

            waiting = False

    # Plot animation
    ax.clear()
    plt.plot(x_ac, y_ac)
    plt.plot(x_curr,y_curr,'o')
    ax.set_xlim(-1, 1), ax.set_xticks([])
    ax.set_ylim(-1, 1), ax.set_yticks([])


# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, interval=10)
plt.show()
