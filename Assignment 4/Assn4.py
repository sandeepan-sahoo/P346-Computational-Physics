import math
from Ass3 import *
def backforward(l,u,b):
    dim = len(b)
    x = [0 for i in range(dim)]
    y = [0 for i in range(dim)]
    y[0]=b[0]
    for i in range(dim):
        d = b[i]
        for j in range(i):
            d = d - l[i][j]*y[j]
        y[i]=d
    for i in range(dim):
        d = y[i]
        for j in range(dim):
            d = d - u[i][j]*x[j]
        x[i]=d/u[i][i]
    return x

def partial_pivot(a, n):
    for i in range (n-1):
        if a[i][i] ==0:
            for j in range (i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[i], a[j] = a[j], a[i]
    return a
    
def doolittle(a):
    a = sortout(a)
    l = []
    u = []
    if len(a) == len(a[0]):
        for i in range(len(a)):
            l.append([])
            u.append([])
            for j in range(len(a[i])):
                if j<=i:
                    if i == j:
                        l[i].append(1)
                    else:
                        u[i].append(0)
                        d = a[i][j]
                        for k in range(j):
                            d = d- l[i][k]*u[k][j]
                        l[i].append(d/u[j][j])
                if i<=j:
                    if i<j:
                        l[i].append(0)
                    d = a[i][j]
                    for k in range(i):
                        d = d- l[i][k]*u[k][j]
                    u[i].append(d)

    return l,u
def cholesky(a):
    l = []
    if len(a) == len(a[1]):
        for i in range(len(a)):
            l.append([])
            for j in range(i+1):
                d = 0
                for k in range(j):
                    d = l[i][k]*l[j][k]
                if i == j:
                    l[i].append(round(math.sqrt(a[i][i]-d),4))
                else:
                    l[i].append(round((a[i][j]-d)/l[j][j],4))
        return l
            


