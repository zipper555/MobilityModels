import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create new Figure and an Axes which fills it.
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

# Set initial angle and step size
angle = np.random.uniform(0,2*np.pi)
step = 0.1
compute = True
stepx = 0.1
stepy = 0.1
y_intercept = 0

def update(frame_number):
    global x0, y0, x_ac, y_ac, x_curr, y_curr, step, angle, stepx, stepy
    # Task 7.2.1
    x_curr = x0 + stepx * np.cos(angle)
    y_curr = y0 + stepy * np.sin(angle)
    slope = (y0 - y_curr)/(x0 - x_curr)
    #print "Slope: {} tan: {}".format(slope, np.tan(angle))
    y_intercept = y0 - slope * x0
    
    if x_curr > 1 or x_curr < -1:
        x_curr_t = (1 if x_curr > 1 else -1)
        y_curr_t = slope * x_curr_t + y_intercept
        x_ac.append(x_curr_t)
        y_ac.append(y_curr_t)  
        x0, y0 = x_curr_t, y_curr_t
        stepx = -1 * stepx
        x_curr = x0 + stepx * np.cos(angle)
        y_curr = y0 + stepy * np.sin(angle)
        y_intercept = y0 - np.tan(angle) * x0
    
    if y_curr > 1 or y_curr < -1:
        y_curr_t = (1 if y_curr > 1 else -1)
        x_curr_t = (y_curr_t - y_intercept)/slope
        x_ac.append(x_curr_t)
        y_ac.append(y_curr_t)
        x0, y0 = x_curr_t, y_curr_t
        stepy = -1 * stepy
        y_curr = y0 + stepy * np.sin(angle)
        x_curr = x0 + stepx * np.cos(angle)
        y_intercept = y0 - np.tan(angle) * x0
    
    x_ac.append(x_curr)
    y_ac.append(y_curr)
    
    x0 = x_curr
    y0 = y_curr
   
    ax.clear()
    plt.plot(x_ac, y_ac)
    plt.plot(x0, y0, 'o')
    ax.set_xlim(-1, 1), ax.set_xticks([])
    ax.set_ylim(-1, 1), ax.set_yticks([])



# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, interval=10)
plt.show()