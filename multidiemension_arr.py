# Multidimension array

import numpy as np

arr = np.array('A')  # zero dimension array
print(arr.ndim)

arr1 = np.array(['a', 'b'])  # one dimesion array
print(arr1.ndim)

arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [4, 4, 3]])  # two dimesion array

print(arr2.ndim)

arr3 = np.array([[[1, 2, 3], [4, 5, 6], [4, 4, 3]],
                [[1, 2, 3], [4, 5, 6], [4, 4, 3]],
                [[1, 2, 3], [4, 5, 6], [4, 4, 3]]])  # three dimension array

print(arr3.ndim)


arr4 = np.array([[[[1, 2, 3], [4, 5, 6], [4, 4, 3]],
                  [[1, 2, 3], [4, 5, 6], [4, 4, 3]],
                  [[1, 2, 3], [4, 5, 6], [4, 4, 3]],
                  [[1, 2, 3], [4, 5, 6], [4, 4, 3]]]])  # four dimension array

print(arr4.ndim)

# shape syntax : it shows no of layer , no of row , no of cloumn

print(arr3.shape)  # output (3, 3, 3) (no of layer , no of row , no of cloumn)

# indexing

print(arr3[1][0][2])  # chain indexing

print(arr3[1, 0, 1])  # multidimension indexing is faster than chain indexing


# concatination

arry_strinf = np.array([[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                        [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
                        [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', ' ']]
                        ])

word = arry_strinf[2, 1, 0]+arry_strinf[0, 2, 2] + \
    arry_strinf[2, 0, 0]+arry_strinf[0, 2, 1] + \
    arry_strinf[0, 0, 0]+arry_strinf[1, 0, 2]  # [layer , row , cloumn]
print(word)
