import numpy as np
print(np.__version__)
task1 = np.zeros(10)
print(task1)
task2 = np.array([1,2,3,4,5])
print(task2.nbytes)
help(np.add)
task3 = np.zeros(10)
task3[4] =  1
print(task3)

#### 30. How to find common values between two arrays? (★☆☆)
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,3,9,10])
common = np.intersect1d(array1,array2)
print(common)