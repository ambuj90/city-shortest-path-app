import numpy as np

# 1D Array
arr = np.array([1, 2, 3, 4])
print("arr[0] =", arr[0])                # First element
print("arr[1] =", arr[1])                # Second element
print("arr[2] + arr[3] =", arr[2] + arr[3])  # Sum of third and fourth elements

# 2D Array (2 rows x 5 columns)
arr1 = np.array([[1, 2, 3, 4, 5], 
                 [6, 7, 8, 9, 10]])
print("\n2D Array - 2nd element on 2nd row:", arr1[1, 1])  # Element at row 2, column 2 (7)

# 3D Array (2 blocks, each 2x3)
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],     # Block 0
    [[7, 8, 9], [10, 11, 12]]   # Block 1
])
print("\n3D Array - arr3[0, 1, 2] =", arr3[0, 1, 2])  # Block 0, Row 1, Column 2 => 6

# Another 3D Array
arr4 = np.array([
    [[1, 2], [3, 4]],   # Block 0
    [[5, 6], [7, 8]]    # Block 1
])
print("3D Array - arr4[1, 1, 0] =", arr4[1, 1, 0])  # Block 1, Row 1, Column 0 => 7
