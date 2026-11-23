import numpy as np
# scalar airthmetic (it means single value)
'''
# scalar is mean by single value , it is the liner algebra term,
'''
array = np.array([1, 2, 3, 4])

print(array+1)  # output :[2 3 4 5]
print(array-2)  # output :[-1  0  1  2]
print(array*3)  # output :[ 3  6  9 12]
print(array/4)  # output :[0.25 0.5  0.75 1.  ]
# it apply the operation to each element in the array
print(array**5)  # output: [   1   32  243 1024]


# vectorized math function (It is the single dimension)
# such 1D array

arr = np.array([1.0, 2.3, 3.66])
# we can apply the operation to the entire 1D array
print(np.sqrt(arr))  # output [1.         1.41421356 1.73205081 2.        ]
print(np.round(arr))  # output[1. 2. 4.]
print(np.pi)  # output 3.141592653589793


# eg:
radii = np.array([1, 2, 4, 4])
# formula : A=pi*r^2
# output :[ 3.14159265 12.56637061 50.26548246 50.26548246]
print(np.pi * radii ** 2)


# Element-wise airthemetic:
arr1 = np.array([1, 2, 3])
arr2 = np.array([14, 5, 6])

print(arr1-arr2)
print(arr1+arr2)
print(arr1*arr2)
print(arr1/arr2)
print(arr1**arr2)


# Comparison operator
# we can create boolean data , filter data, element wise comparison

score = np.array([78, 52, 83, 100, 34, 56, 53, 34])


# output: [False False False  True False False False False]
print(score == 100)
print(score > 50)  # output:[ True  True  True  True False  True  True False]
print(score >= 40)  # output:[ True  True  True  True False  True  True False]
print(score < 70)  # output:[False  True False False  True  True  True  True]
print(score <= 60)  # output:[False  True False False  True  True  True  True]
print(score != 70)  # output :[ True  True  True  True  True  True  True  True]
