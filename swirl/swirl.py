import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0.1, 15, 0.001)
theta = 4 * np.pi * r

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, color='purple', linewidth=5)
ax.set_rmax(5)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5) 
ax.grid(True)
fig.patch.set_facecolor('black')

plt.axis('off')
plt.tight_layout()
plt.savefig('swirl.svg')
plt.show()