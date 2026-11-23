import numpy as np

# slicing

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# array [start:end:step]
# row selection
print(array[0:3:2])
print(array[::-2])

# column selection

print(array[:, 0])
print(array[:, 2])

print(array[:, 1:])
print(array[:, ::2])
