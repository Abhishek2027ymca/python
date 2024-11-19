
import numpy as np # type: ignore
print(np.__version__)


import math as m
print("value of pi is", m.pi)


a = np.array([[1,2,3,4] , [5,6,7,8]])
b = np.array([[5,7,4,2]])
print(a)

                     
                     

# print(a.itemsize + 1)



print(a.shape)
print(b.shape)
print(a.size)

newshape = a.reshape(2,4)
print(newshape)


newshape = b.reshape(2,2)
print(newshape)

import mymodule2 as m