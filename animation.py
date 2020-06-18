import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = [0]
y_data = [0]

all_x = []
all_sin = []
all_cos = []

fig, ax = plt.subplots(3,1, figsize=(15,15))

for a in ax:
    a.axis('off')

ax[0].axis('scaled')
ax[0].set_xlim(-2,2)
ax[0].set_ylim(-2,2)

ax[1].set_xlim(0,360)
ax[1].set_ylim(-1,1)

ax[2].set_xlim(0,360)
ax[2].set_ylim(-1,1)

line_x, = ax[0].plot(0,0, color='red', marker='o', linestyle='dashed')
line_y, = ax[0].plot(0,0, color='green', marker='o', linestyle='dashed')
line_c, = ax[0].plot(0,0, color='blue', marker='o', linestyle='dashed')

line_sin, = ax[1].plot(0,0, color='green')
line_cos, = ax[2].plot(1,0, color='red')

def animation_frame(i):
    x_data[0]=np.cos(np.deg2rad(i))
    y_data[0]=np.sin(np.deg2rad(i))

    if i==0:
        all_x.clear()
        all_sin.clear()
        all_cos.clear()

    all_x.append(i)
    all_sin.append(y_data[0])
    all_cos.append(x_data[0])

    line_c.set_xdata(x_data)
    line_c.set_ydata(y_data)

    line_x.set_xdata(x_data)
    line_x.set_ydata([0])

    line_y.set_xdata([0])
    line_y.set_ydata(y_data)

    line_sin.set_xdata(all_x)
    line_sin.set_ydata(all_sin)

    line_cos.set_xdata(all_x)
    line_cos.set_ydata(all_cos)

    return

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0,360,2), interval=20)
# Use the following line to save the animation with imagemagick
# animation.save('animation.gif', writer='imagemagick', fps=60)
plt.show()
