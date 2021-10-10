import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize as op

x1 = (0, None)
x2 = (0, None)
x3 = (0, None)
x4 = (0, None)
x5 = (0, None)
x6 = (0, None)
x7 = (0, None)
x8 = (0, None)
x9 = (0, None)
x10 = (0, None)
x11 = (0, None)
x12 = (0, None)
x13 = (0, None)
x14 = (0, None)

c = np.array([3,4,5,7,6,7,7,8,9,4,3,4,0,0])

A_eq = np.array([[1,1,1,1,1,1,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,1,1,1,1,1,1,0,1], [1,0,0,1,0,0,1,0,0,1,0,0,0,0]
                ,[0,1,0,0,1,0,0,1,0,0,1,0,0,0], [0,0,1,0,0,1,0,0,1,0,0,1,0,0]])
B_eq = np.array([200000,60000,50000,100000,50000])

res = op.linprog(c,None,None,A_eq,B_eq,bounds=(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14))
#print(res)
'''
c = np.mat([0,1,0,0])
c = c.T
A = np.mat([[2,-1,-1,0],[0,1,-2,1]])
d = [0.25,0.25,0.25,0.25]
#print(d)
D = np.diag(d)
#print(D)
e = np.mat([1,1,1,1])
et = e.T
E = np.diag([1,1,1,1])

pic = []

n = 4
alpha = 1/3
r = math.sqrt(3)/6
k= 1
for k in range(1,21):
    print(k)
    #print(D)
    b = np.r_[np.matmul(A,D),e]
    #print(b)
    bt = b.T
    b_1 = np.matmul(b,bt)
    b_1 = b_1.I
    #print(r)
    pb = np.matmul(bt,b_1)
    pb = np.matmul(pb,b)
    #print(pb)

    res = -(E-pb)
    #print(res)
    res = np.matmul(res,D)
    dy0 = np.matmul(res,c)
    #print(res)
    #print(dy0)
    dealnum = np.square(dy0)
    dealnum = np.sum(dealnum,0)
    dealnum = math.sqrt(dealnum)
    #print(dealnum)
    y1= et/n + alpha * r *(dy0) / dealnum
    #print(y1)
    x1 = np.matmul(D,y1)
    x1down = np.matmul(et.T, x1)
    #print(x1)
    #print(x1down)
    x1 = x1/x1down
    print(x1)
    x1.reshape(1,n)
    x1 = x1.T
    x1.flatten()
    #print(x1.A[0])
    pic.append(x1.A[0][1])
    D = np.diag(x1.A[0])
    #print(D)

picx = np.linspace(1,20,20)
plt.figure()
plt.plot(picx,pic)
plt.title('6-3')
plt.show()
#print(a1)
'''

