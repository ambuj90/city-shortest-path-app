import numpy as np

# 1D array using tuple
arr = np.array((1, 2, 3, 4, 5))
print("1D Array:\n", arr)

# 2D array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr1)

# 3D array
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
print("\n3D Array:\n", arr3)

# Dimensionality of different arrays
a = np.array(42)  # 0D
b = np.array([1, 2, 3, 4, 5])  # 1D
c = np.array([[1, 2, 3], [4, 5, 6]])  # 2D
d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])  # 3D

print("\nArray dimensions:")
print("a.ndim (0D):", a.ndim)
print("b.ndim (1D):", b.ndim)
print("c.ndim (2D):", c.ndim)
print("d.ndim (3D):", d.ndim)

# Creating an array with minimum 5 dimensions
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print("\nArray with ndmin=5:\n", arr5)
print("Number of dimensions:", arr5.ndim)
