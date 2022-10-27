import numpy as np 
a = np.array([1,2,3,4])
num_list =a.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)


import numpy as np
a = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])
b = np.trace(a)
print(b)


import numpy as np
def superieur() :
    l= np.array([[1,2,3,4], [7,9,14,2]])
    for i in l :
            a = [i>2]
            print(a)
superieur()


import numpy as np
def add ():
    l = np.array([1,2,4])
    p = np.array ([2,4,6])
    print(l[0]+p[0])
    print(l[1]+p[1])
    print(l[2]+p[2])
add()

import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)