import numpy as np

# Create a base 1D NumPy array
base_array = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original Array:", base_array)

# Slice from index 1 to 4 (1:5 -> includes 1, 2, 3, 4)
slice_1 = base_array[1:5]
print("\nSlice 1 - arr[1:5] -> From index 1 to 4:", slice_1)

# Slice from index 4 to the end
slice_2 = base_array[4:]
print("\nSlice 2 - arr[4:] -> From index 4 to the end:", slice_2)

# Slice from the beginning to index 3 (0 to 3)
slice_3 = base_array[:4]
print("\nSlice 3 - arr[:4] -> From start to index 3:", slice_3)

# Slice using negative indexing (from 3rd last to 2nd last)
slice_4 = base_array[-3:-1]
print("\nSlice 4 - arr[-3:-1] -> From 3rd last to 2nd last:", slice_4)
