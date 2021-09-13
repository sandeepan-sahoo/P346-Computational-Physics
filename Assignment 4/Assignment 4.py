import math
from Ass3 import *
from Assn4 import *

#Q2 inverse of the matrix
a = [[0,2,8,6],[0,0,1,2],[0,1,0,1],[3,7,1,0]]
a = partial_pivot(a,4,m)
m = identity(4)
if determinant(a)!=0:
    print("matrix is invertible")
l,u = doolittle(a)
print("inverse of the matrix is")
for h in m:
    s=backforward(l,u,h)
    print(s)

#Q3
d = [[10,1,0,2.5],[1,12,-0.3,1.1],[0,-0.3,9.5,0],[2.5,1.1,0.0,6.0]]
g=cholesky(d)
print("the cholesky decomposed lower triangular matrix is matrix is")
print(g)
e = [2.2,2.85,2.79,2.87]
print("the solution is")
t = transpose(g)
print(t)
print(backforward(g,t,e))

#Q1
v = [[1,1,-1,2],[0,1,-2,0],[1,2,-3,0],[2,1,3,-2]]
v = partial_pivot(v,4)
l,u = doolittle(v)
b = [9,-3,-2,0]
print("the solution is")
print(backforward(l,u,b))
