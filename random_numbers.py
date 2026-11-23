import numpy as np
# for random integer(start,end,size)
rng = np.random.default_rng()

print(rng.integers(1, 34, (3, 4)))

# for random floting point(start,end,size)\

print(np.random.uniform(1, 34, (3, 4)))

# seed is used to reproduce same output

# how to suffle in an array
arr = np.array([[1, 2, 3, 54],
               [4, 6, 7, 5]])
rng.shuffle(arr)
print(arr)


# for random choice
fruits = np.array([["apple", "banana", "orange"],
                  ["grape", "brinjal", "nothing"]])
fruit = rng.choice(fruits, size=(3, 3))
print(fruit)
