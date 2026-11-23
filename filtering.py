import numpy as np
'''
Filtering:
It is the process of selecting the value in the array that matches the 
certain condition
'''
age = np.array([[23, 12, 34, 54, 56, 23, 34, 89, 76],
                [16, 34, 67, 23, 5, 6, 4, 22, 35]])

child = age[age < 20]
even = age[age % 2 == 0]
print(child)
print(even)
# In this it does not preserve the shape
# by using the np.where we can preserve the shape
# (copndition,name of the array,replace value)
nop = np.where(age > 16, age, "_")
print(nop)
