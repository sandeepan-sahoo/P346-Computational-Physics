import math
def augment(a,b):
    k = []
    for i in range(len(a)):
        k.append(a[i])
        k[i].append(b[i])
    return k
def sortout(a):
    for i in range(len(a)):
        if a[i][i]==0:
            for j in range(len(a)):
                if a[j][i]!=0 and a[i][j]!=0:
                    a[j],a[i]=a[i],a[j]
                
    return a

def swapnum(c):
    a = c
    d = 0
    for i in range(len(a)):
        if a[i][i]==0:
            for j in range(len(a)):
                if a[j][i]!=0 and a[i][j]!=0:
                    d = d+1
                
    return pow(-1,d)
           
def addrow(a,b):
    c = []
    if len(a)==len(b):
        for i in range(len(a)):
            c.append(a[i] + b[i])
        return c
    else:
        return "row dimensions incompatible"
    
def multiplyrow(a,c):
    b = []
    for i in range(len(a)):
        b.append(float(a[i])*c)
    return b

def determinant(a):
    d=sortout(a)
    s=swapnum(a)
    for i in range(len(d)):
        for j in range(len(d)):
            if j!=i:
                k = multiplyrow(d[i],-1*d[j][i]/d[i][i])
                d[j]= addrow(d[j], k)
    det = 1
    for i in range(len(d)):
        det = det*d[i][i]
    det = det*s
    return det
            
def gaussjordan(a,b):
    if len(a)==len(b):
        d = augment(a,b)
        d = sortout(d)
        u = []
        for i in range(len(d)):
            for j in range(len(d)):
                if j!=i:
                    k = multiplyrow(d[i],-1*d[j][i])
                    v = multiplyrow(d[j],d[i][i])
                    d[j]= addrow(v,k)
                d[j] = multiplyrow(d[j],1/d[i][i])
                    
        return d
def identity(n):
    u = []
    for i in range(n):
        u.append([])
        for k in range(n):
            if k==i:
                u[i].append(1)
            else:
                u[i].append(0)
    return u
def augiden(c):
    u = identity(len(c))
    a = c
    for i in range(len(a)):
        if a[i][i]==0:
            for j in range(len(a)):
                if a[j][i]!=0 and a[i][j]!=0:
                    a[j],a[i]=a[i],a[j]
                    u[j],u[i]=u[i],u[j]
    return u
            
def inverse(a):
    u = augiden(a)
    d = sortout(a)
    for i in range(len(d)):
        for j in range(len(d)):
            if j!=i:
                k = multiplyrow(d[i],-1*d[j][i])
                m = multiplyrow(u[i],-1*d[j][i])
                v = multiplyrow(d[j],d[i][i])
                p = multiplyrow(u[j],d[i][i])
                d[j]= addrow(v,k)
                u[j]= addrow(m,p)
            u[j] = multiplyrow(u[j],1/d[i][i])
            d[j] = multiplyrow(d[j],1/d[i][i])
               
    return u
    

def solution(a,b):
    u = gaussjordan(a,b)
    sol = []
    for w in u:
        sol.append(round(w[-1],5))
    return sol
        



        
                
            
