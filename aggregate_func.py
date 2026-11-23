# aggrigate function
'''
It summarize the data and return a single value
'''
import numpy as np

arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])

# sum all the element in the array
print(np.sum(arr1))

# mean or average

print(np.mean(arr1))

# standard deviation(it is the messure of spread within the data)
print(np.std(arr1))

# variance is the square of the standard deviation
print(np.var(arr1))

# TO find the minimum
print(np.min(arr1))
# TO find the maximum
print(np.max(arr1))

# to get position use :arg
# for min
print(np.argmin(arr1))
# for max
print(np.argmax(arr1))


# AXIS
# lets sum all the column
print(np.sum(arr1, axis=0))

# lets sum all the row
print(np.sum(arr1, axis=1))
