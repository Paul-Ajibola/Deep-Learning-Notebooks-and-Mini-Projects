# import libraries
import numpy as np
import matplotlib.pyplot as plt



# define a 1D linear function
def linear_function_1D(x, beta, omega):
    return beta + omega * x


# create an array of x values 
x = np.arange(0, 10, 0.01)


# set parameters
beta = 3.0
omega = 1.5 

# compute y values 
y = linear_function_1D(x, beta, omega)

# plot 
plt.figure(figsize=(7,4))
plt.plot(x,y,linewidth=2)
plt.title("1D Linear Function")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

