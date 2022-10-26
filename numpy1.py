from array import *
from optparse import Values
array_num = array('i', [])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)


import numpy as np
arr= np.arange()
arr= np.reshape(arr,())
a=np.diagonal(arr,)
result=sum(a)
print(result)

import numpy as np
a=np.arange().reshape()
print("original matrix is :\n",a)
m=np.trace(a)
print("trace of matrix :", m)


def solve():
   left_items = filter(lambda a: a < x, values)
   return list(left_items)
values = [1,5,8,3,6,9,12,77,55,36,2,5,6,12,87]
x = 50
print(solve(values, x))

import numpy as np
a = np.array([])
np.shape(a)
b = np.array([[],[]])
np.shape(b)


A=[]
B=[]
C=[]
for i in range(len(A)):
    C.append(A[i])
    C.append(B[i])
print(C)

import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)