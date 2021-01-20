import numpy as np

array = [[[0 for k in range(8)] for j in range(5)] for i in range(3)]

arr_np = np.array(array)
print(arr_np.shape)