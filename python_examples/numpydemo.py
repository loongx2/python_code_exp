import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy.integrate
import scipy.optimize

a = np.array([1.2, 5.5, -4.3, 9.1, 0.2, -3.3], dtype='double')
print(f"a is now:\n{a!s}")
# Expected output: a is now:
#                  [ 1.2  5.5 -4.3  9.1  0.2 -3.3]
a = a.reshape((2, 3))
print(f"a is now:\n{a!s}")
# Expected output: a is now:
#                  [[ 1.2  5.5 -4.3]
#                   [ 9.1  0.2 -3.3]]
a = a.reshape(6)
print(f"a is now:\n{a!s}")
# Expected output: a is now:
#                  [ 1.2  5.5 -4.3  9.1  0.2 -3.3]

# Unlike Python lists, slicing and views share underlying data.

b = a[2:4]
print(f"b is now:\n{b!s}")
# Expected output: b is now:
#                  [-4.3  9.1]
a[2] = 2.54
print(f"b is now:\n{b!s}")
# Expected output: b is now:
#                  [2.54 9.1 ]

# Arithmetic works differently for numpy arrays and Python lists.

pl = [1, 2, 3]
print(f"Python list addition: {pl + pl}")
# Expected output: Python list addition: [1, 2, 3, 1, 2, 3]
print(f"Python list multiplication: {pl * 3}")
# Expected output: Python list multiplication: [1, 2, 3, 1, 2, 3, 1, 2, 3]
na = np.array([1, 2, 3])
print(f"Numpy array addition: {na + na}")
# Expected output: Numpy array addition: [2 4 6]
print(f"Numpy array multiplication: {na * na}")
# Expected output: Numpy array multiplication: [1 4 9]

# Ufuncs apply separately to each element of the array. This
# eliminates the need for us to write that loop explicitly. Often
# we do not wish to use list comprehension, since that could not
# operate in a numpy array in place, which might be important if
# the array is humongous.

a = a + np.cos(a)
print(f"a is now:\n{a!s}")
# Expected output: a is now:
#                  [ 1.56235775  6.20866977  1.71556471  8.1522784   1.18006658 -4.28747977]

# When combining tensors of different ranks, the smaller tensor
# is automatically broadcast into higher dimensions so that the
# shapes of the two matrices are compatible for that operation.

c = np.array([1, 2, 3, 4, 5, 6])
c = c.reshape((2, 3))  # shape (2, 3)
d = np.array([1, 2, 3])  # broadcast into (2, 3)
print("c + d equals:")
print(c + d)
# Expected output: c + d equals:
#                  [[2 4 6]
#                   [5 7 9]]

# Cherry picking elements by indexing with a truth-valued array.

v = a > 3  # A truth-valued array from element-wise comparisons.
print(f"v is now: {v}")
# Expected output: v is now: [False  True False  True False False]
print(f"a[v] is: {a[v]}")
# Expected output: a[v] is: [6.20866977 8.1522784 ]


# Then, onto scipy and its basic functions in style MATLAB.

# Scipy offers a host of numerical integration functions.


# First, let's make up a function to integrate.

def f(x_):
    return x_ * (x_ - 4) / (3 + np.cos(2 * (x_ + 1) + 4 * np.sin(x_ / 10)))


# Integration, given a function f that works in any single point.
print(f"Quad: {scipy.integrate.quad(f, -5, 5)[0]:.6f}")
# Expected output: Quad: 30.771998
print(f"Romberg: {scipy.integrate.romberg(f, -5, 5):.6f}")
# Expected output: Romberg: (Note: romberg may not be available in newer scipy versions)
print(f"Fixed quad: {scipy.integrate.fixed_quad(f, -5, 5)[0]:.6f}")
# Expected output: Fixed quad: 33.995322

# Integration, given a fixed set of samples of values of f.
xx = np.linspace(-5, 5, 100)
yy = f(xx)
print(f"Trapezoidal: {scipy.integrate.trapz(yy, x=xx):.6f}")
# Expected output: Trapezoidal: 30.770638 (Note: trapz may be deprecated, use trapezoid)
print(f"Simpson: {scipy.integrate.simps(yy, x=xx):.6f}")
# Expected output: Simpson: (Note: simps may not be available in newer scipy versions)

# Next, the minimization of some function f. (To maximize f,
# you can always simply minimize -f.)

result = scipy.optimize.minimize(f, np.array([0]), method='BFGS')
print(f"Function is minimized at x = {result.x[0]:.5f}.")
# Expected output: Function is minimized at x = 0.88158.

# The lower resolution data points from interval [0, 10].
x = np.linspace(0, 10, 10)
# The higher resolution data points on same interval [0, 10].
xx = np.linspace(0, 10, 500)

# Ufuncs again apply to all elements of the array.
y = f(x)

# Last, interpolation of values between given data points.

# Create function to represent the interpolation.
f_linear = scipy.interpolate.interp1d(x, y, kind='linear')
f_cubic = scipy.interpolate.interp1d(x, y, kind='cubic')

# Apply that function to values on higher resolution.
y_linear = f_linear(xx)
y_cubic = f_cubic(xx)

# Create the figure to display.
plt.figure(1)

# Classic MATLAB plotting syntax, two plots in the same graph.
# Good thing that Python functions can handle any number of
# any type of arguments given to them with *args and **kwargs.
plt.plot(x, y, 'o', xx, y_linear, 'r', xx, y_cubic, 'g')
plt.show()
