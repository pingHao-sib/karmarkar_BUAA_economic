import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize as op

c = np.mat([0,0,0,0,0,0,0,0,0,0,0,0,1,0])
c = c.T
A = np.mat([[3,8,-1,0,0,0,0,0,0,0,0,0,-6,-4],
            [5,2,0,-1,0,0,0,0,0,0,0,0,1,-7],
            [0,0,0,0,3,5,-3,-5,1,0,0,0,8,-9],
            [0,0,0,0,8,2,-8,-2,0,1,0,0,5,-6],
            [0,0,0,0,-1,0,1,0,0,0,1,0,-1,0],
            [0,0,0,0,0,-1,0,1,0,0,0,1,-1,0],
            [9,6,0,0,-4,-7,4,7,0,0,0,0,-15,0],
            ])
d = [1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14,1/14]
#print(d)
D = np.diag(d)
#print(D)
e = np.mat([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
et = e.T
E = np.diag([1,1,1,1,1,1,1,1,1,1,1,1,1,1])

pic1 = []
pic2 = []
n = 14
alpha = 1/3
r = 1/math.sqrt(14*13)
k= 1
for k in range(1,21):
    print(k)
    #print(D)
    b = np.r_[np.matmul(A,D),e]
    #print(b)
    bt = b.T
    b_1 = np.matmul(b,bt)
    #print(b_1)
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
    #print(x1)
    x1.reshape(1,n)
    x1 = x1.T
    x1.flatten()
    print(x1.A[0])
    pic1.append(x1.A[0][12])
    pic2.append(9*x1.A[0][0]/x1.A[0][13]+6*x1.A[0][1]/x1.A[0][13])
    D = np.diag(x1.A[0])
    #print(D)

picx = np.linspace(1,20,20)
plt.figure()
#plt.plot(picx,pic1,label='karmarkar_type')
plt.plot(picx,pic2,label='raw_type')
plt.title('7-3')
plt.legend(loc='middle right', fontsize=10)
plt.show()
#print(a1)


