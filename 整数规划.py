import numpy as np
from scipy import optimize as op

z = np.array([40,90])
A = np.array([[9,7],[7,20]])
B = np.array([56,70])

#x1 = (5,15)
x1 = (0,4)
x2 = (3,10)

res = op.linprog(-z,A,B,bounds=(x1,x2))
print(res)
