import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplots3d import Axes3D


# Set sample values
beta = 3.0
omega1 = 1.0
omega2 = 2.0

# Create a grid of x1 and x2 values
x1_vals = np.linspace(-5, 5, 50)
x2_vals = np.linspace(-5, 5, 50)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

# Compute y values based on the linear plane formula
Y = beta + omega1 * X1 + omega2 * X2

# Plotting the 3D surface
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='plasma', edgecolor='k', alpha=0.85)

# Labels and title
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')
ax.set_title('3D Linear Plane: $y = 3 + 1x_1 + 2x_2$')

plt.tight_layout()
plt.show()
