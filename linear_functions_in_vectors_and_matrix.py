import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplots3d import Axes3D


def linear_function_3D(x1, x2, x3, beta, omega1, omega2, omega3):
    return beta + omega1 * x1 + omega2 * x2 + omega3 * x3


# Sample input
x1 = 4
x2 = -1
x3 = 2

# Parameters
beta1 = 0.5
beta2 = 0.2
omega11, omega12, omega13 = -1.0, 0.4, -0.3
omega21, omega22, omega23 = 0.1, 0.1, 1.2

# Compute outputs individually
y1 = linear_function_3D(x1, x2, x3, beta1, omega11, omega12, omega13)
y2 = linear_function_3D(x1, x2, x3, beta2, omega21, omega22, omega23)

# Matrix-vector form
import numpy as np

# Inputs as vector
x_vec = np.array([[x1], [x2], [x3]])

# Weight matrix
omega_mat = np.array([
    [omega11, omega12, omega13],
    [omega21, omega22, omega23]
])

# Bias vector
beta_vec = np.array([[beta1], [beta2]])

# Compute matrix-vector output
y_vec = beta_vec + np.matmul(omega_mat, x_vec)

print("Individual Equations:")
print(f"y1 = {beta1} + ({omega11} * {x1}) + ({omega12} * {x2}) + ({omega13} * {x3}) = {y1:.3f}")
print(f"y2 = {beta2} + ({omega21} * {x1}) + ({omega22} * {x2}) + ({omega23} * {x3}) = {y2:.3f}")

print("\nMatrix-Vector Form:")

print("x vector:")
print(x_vec)

print("\nOmega (weight) matrix:")
print(omega_mat)

print("\nBeta (bias) vector:")
print(beta_vec)

print("\nComputed output vector (y = β + Ωx):")
print(y_vec)