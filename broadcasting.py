import numpy as np

'''
BROADCASTING:
It allow numpy to perform operation on array
with diifernt shape by virtually expanding the dimension

Rules:
1.The dimension have the same size
OR
2.One of the dimension has a size of 1
'''

arr1 = np.array([[1, 2, 3, 4]])
arr2 = np.array([[1], [2], [3], [4]])

print(arr2.shape)  # output :(4, 1)
print(arr1.shape)  # output :(1, 4)

print(arr1*arr2)
'''output :[[ 1  2  3  4] [ 2  4  6  8] 
            [ 3  6  9 12] [ 4  8 12 16]]
                            '''
