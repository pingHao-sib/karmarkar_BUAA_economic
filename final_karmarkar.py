import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize as op

c_com = np.mat([5,10,5,20,6])
c_com = c_com * math.sqrt(91/3084)
a_com = np.mat([
    [1,0,0,1,0],
    [0,1,0,1,0],
    [0,0,1,1,0],
    [1,0,0,0,1],
    [0,1,0,0,1],
    [0,0,1,0,1],
    [0,0,0,1,0],
    [0,0,0,0,1]
])
com_b = np.mat([3,4,5,4,3,4,0,0]).T

v = com_b - np.matmul(a_com,c_com.T)
print(v)
print(c_com * math.sqrt(91/3084))

a = np.mat([[1,0,0,1,0,0,1,0,0,1,0,0,0,0],
            [0,1,0,0,1,0,0,1,0,0,1,0,0,0],
            [0,0,1,0,0,1,0,0,1,0,0,1,0,0],
            [1,1,1,1,1,1,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,0,1],
            ])

para_c = np.mat([3,4,5,7,6,7,7,8,9,4,3,4,0,0]).T
para_b = np.mat([5,10,5,20,6]).T
#print(para_b-np.matmul(a,np.mat(np.ones(a.shape[1])).T))
A = np.c_[a,np.zeros((a.shape[0],
                      2*a.shape[0]+a.shape[1])),
          para_b-np.matmul(a,np.mat(np.ones(a.shape[1])).T),
          -para_b]
tmp_s = np.c_[np.zeros((a.shape[1],a.shape[1])),
              a.T,
              -a.T,
              np.diag(np.ones(a.shape[1])),
              para_c -np.mat(np.ones(a.shape[1])).T,
              -para_c]
tmp_t = np.c_[para_c.T,
              -para_b.T,
              para_b.T,
              np.mat(np.zeros(a.shape[1])),
              -np.matmul(para_c.T, np.ones(a.shape[1]).T),0]

A = np.r_[A, tmp_s, tmp_t]





n = 2*(a.shape[0]+a.shape[1]+1)



c = np.mat(np.zeros(2*(a.shape[0]+a.shape[1])))
tmp_c = np.mat([1,0])
c = np.c_[c, tmp_c]
c = c.T

D = np.diag(np.ones(2*(a.shape[0]+a.shape[1]+1))/n)
e = np.mat(np.ones(2*(a.shape[0]+a.shape[1]+1)))
et = e.T
E = np.diag(np.ones(2*(a.shape[0]+a.shape[1]+1)))


pic1 = []
pic2 = []
alpha = 1/3
r = (1/math.sqrt(n*(n-1)))

for k in range(1,91):
    print(k)
    b = np.r_[np.matmul(A,D),e]
    bt = b.T
    b_1 = np.matmul(b,bt)
    b_1 = b_1.I
    pb = np.matmul(bt,b_1)
    pb = np.matmul(pb,b)

    res = -(E-pb)
    res = np.matmul(res,D)
    dy0 = np.matmul(res,c)

    print(dy0)

    dealnum = np.square(dy0)
    dealnum = np.sum(dealnum,0)
    dealnum = math.sqrt(dealnum)
    y1= et/n + alpha * r *(dy0) / dealnum

    print(y1)
    x1 = np.matmul(D,y1)
    x1down = np.matmul(et.T, x1)
    x1 = x1/x1down
    print(x1)

    x1.reshape(1,n)
    x1 = x1.T
    x1.flatten()
    pic1.append(x1.A[0][n-2])
    store = x1.A[0][0:a.shape[1]]/x1.A[0][n-1]
    print(sum(store))
    pic2.append(np.matmul(para_c.T,store).A[0])
    D = np.diag(x1.A[0])

print(pic2)
picx = np.linspace(1,90,90)
plt.figure()
plt.plot(picx,pic1,label='karmarkar_type')
#plt.plot(picx,pic2,label='raw_tpe')
plt.title('8-3')
plt.legend(loc='upper right', fontsize=10)
plt.show()
#print(a1)


