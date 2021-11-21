import math
import random
#Function to multiply matrices
def multiplyMatrices(a, b):
    arl = 0
    for i in range(len(a)):
        if len(a[i])!=len(a[0]):
            arl = arl+1                              #to determine if all row lenghts are same
    
    if arl == 0:
        for i in range(len(b)):                      
            if len(b[i])!=len(b[0]):                 #to determine if all row lenghts are same
                arl = arl+1
    if arl == 0:
        for i in range(len(a)):                      #to determine if dimensions are compatible
            if len(a[i])!=len(b):
                arl = arl+1
    if arl == 0:
        c = []
        for i in range(len(a)):                       #matrix multiplication
            c.append([])
            for j in range(len(b[0])):
                u = 0
                for k in range(len(b)):
                    u = u + a[i][k]*b[k][j]
                c[i].append(u)
        return c
    else:
        return "Matrix dimensions are incompatible with each other"
#function to find transpose of 3 by 3 matrices    
def transpose3by3(a):
    t = []
    for i in range(len(a[1])):
        t.append([])
        for j in range(len(a)):
            t[i].append(a[j][i])
    return t
#function to find transpose of 1 by 3 matrices
def transpose1by3(a):
    return [[a[0][0]],[a[0][1]],[a[0][2]]]
#function to find dot product
def dot1by3(a,b):
    x = transpose1by3(b)
    y = multiplyMatrices(a,x)
    return y
#function to definw the right bracket
def bracket(f,a,b):
    if f(a)*f(b)<=0:
        return a,b
    else:
        while f(a)*f(b)>0:
            if abs(f(a))>abs(f(b)):
                b = b + 0.5*(b-a)
            else:
                a = a - 0.5*(b-a)
        return a,b
    
#function for bisection method
def bisection(f,a,b):
    a,b = bracket(f,a,b)
    if f(a)*f(b)<0:
        c = (a+b)/2
        while abs(f(c))>0.00001:
            c = (a+b)/2
            if f(c)*f(a)<0:
                b = c
            elif f(c)*f(b)<0:
                a = c
        return c
    elif f(a)==0:
        return a
    elif f(b)==0:
        return b
    else:
        return "wrong brakcet"
    
#function for table of bisection method
def bisectable(f,a,b):
    print("Table by bisection method")
    print("i" + "   " + "f(x)")
    a,b = bracket(f,a,b)
    if f(a)*f(b)<0:
        c = (a+b)/2
        i = 0
        while abs(f(c))>0.00001:
            c = (a+b)/2
            if f(c)*f(a)<0:
                b = c
            elif f(c)*f(b)<0:
                a = c
            i = i+1
            print(str(i) + "   " + str(c))
            
#function for table of regula falsi method
def regulatable(f,a,b):
    print("Table by Regula Falsi method")
    print("i" + "   " + "f(x)")
    a,b = bracket(f,a,b)
    if f(a)*f(b)<0:
        c = float((a*f(b)-b*f(a))/(f(b)-f(a)))
        i = 0
        while abs(f(c))>0.00001:
            c = float((a*f(b)-b*f(a))/(f(b)-f(a)))
            if f(c)*f(a)<0:
                b = c
            elif f(c)*f(b)<0:
                a = c
            i = i+1
            print(str(i) + "   " + str(c))
            
#function for the regula falsi method           
def regula_falsi(f,a,b):
    a,b = bracket(f,a,b)
    if f(a)*f(b)<0:
        c = float((a*f(b)-b*f(a))/(f(b)-f(a)))
        while abs(f(c))>0.00001:
            c = float((a*f(b)-b*f(a))/(f(b)-f(a)))
            if f(c)*f(a)<0:
                b = c
            elif f(c)*f(b)<0:
                a = c
        return c
    elif f(a)==0:
        return a
    elif f(b)==0:
        return b
    else:
        return "wrong brakcet"

#function for newton raphson method
def newton_raphson(f,df,x):
    while abs(f(x))>0.00001:
        if abs(df(x))>0.001:
            x = x - f(x)/df(x)
        else:
            break
    return x

#function for table of newton raphson method
def newton_table(f,df,x):
    i = 0
    print("Table by Newton Raphson method")
    print("i" + "   " + "f(x)")
    while abs(f(x))>0.00001:
        if abs(df(x))>0.001:
            x = x - f(x)/df(x)
            i = i + 1
            print(str(i) + "   " + str(x))

#function for to take coefficiants of polynomial as arguments along with variable x and give out its value at x
def pol(x,args):
    p=0
    for i in range(len(args)):
        p = p + args[i]*pow(x,i)
    return p

#function for derivative of the polynomial
def dpol(x,args):
    p=0
    for i in range(len(args)):
        if  i!=0:
            p = p + i*args[i]*pow(x,i-1)
    return p

#function for second derivative of polynomial
def d2pol(x,args):
    p=0
    for i in range(len(args)):
        if  i!=0 and i!=1:
            p = p + i*(i-1)*args[i]*pow(x,i-2)
    return p

#function to take two values and return the value with the maximum absolute value
def abmax(c,d):
    if abs(c)>abs(d):
        return c
    else:
        return d

#function for synthetic division
def syndiv(c,n,args):
    i = n-1
    newargs = [0]*(n+1)
    newargs[n] = args[n]
    while i>0:
        k = args[i] + newargs[i+1]*c
        newargs[i]=k
        i=i-1
    newargs.pop(0)
    return newargs

#function for laguerre method
def laguerre(x,n,args):
    roots = []
    v = n
    for i in range(v):                      #to refine guess variable with newton raphson method
        while abs(pol(x,args))>0.00001:
            if abs(dpol(x,args))>0.001:
                x = x - pol(x,args)/dpol(x,args)
            else:
                break
        a=1
        while a>0.00001 and pol(x,args)!=0 and dpol(x,args)!=0 and d2pol(x,args)!=0:
            g = dpol(x,args)/pol(x,args)
            h = g*g - dpol(x,args)/pol(x,args)
            a = n/abmax(g + math.sqrt(abs((n-1)*(n*h-g*g))),g - math.sqrt(abs((n-1)*(n*h-g*g))))
            x = x - a
        roots.append(x)
        args = syndiv(x,n,args)                  #synthetic division to get the new polynomial of n-1 degree
        n=n-1
    return roots

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
                if abs(a[j][i])>abs(a[i][i]):
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
        
from Ass3 import *
def backforward(l,u,b):
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    dim = len(u)
    for i in range(dim):
        d = b[i]
        for j in range(i):
            d = d - l[i][j]*y[j]
        y.append(d)
    for i in range(dim):
        d = y[i]
        for j in range(dim):
            d = d - u[i][j]*x[j]
        x.append(d/u[i][i])
    return x
def doolittle(a,b):
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

    return l
def crout(a):
    l = []
    u = []
    if len(a) == len(a[1]):
        for i in range(len(a)):
            l.append([])
            u.append([])
            for j in range(len(a[i])):
                if j<=i:
                    if i<j:
                        u[i].append(0)
                    d = a[i][j]
                    for k in range(j):
                        d = d- l[i][k]*u[k][j]
                    l[i].append(d)
                if i<=j:
                    if i==j:
                        u[i].append(1)
                    else:
                        d = a[i][j]
                        for k in range(i):
                            d = d- l[i][k]*u[k][j]
                        u[i].append(d/l[i][i])

        return l


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
                    l[i].append(math.sqrt(a[i][i]-d))
                else:
                    l[i].append((a[i][j]-d)/l[j][j])
        return l

        
                
def partial_pivot(a, n):
    for i in range (n-1):
        if a[i][i] ==0:
            for j in range (i+1,n):
                if abs(a[j][i]) > abs(a[i][i]):
                    a[i], a[j] = a[j], a[i]
        

def midpoint(f,a,b,n):
    k = 0
    h = (b-a)/n
    for i in range(n):
        k = k + h*f(i*h+a+0.5*h)
    return k
def trapezoid(f,a,b,n):
    k = 0
    h = (b-a)/n
    for i in range(n):
        k = k + 0.5*h*(f(i*h+a) + f(i*h + h + a))
    return k
def simpson(f,a,b,n):
    k = 0
    h = (b-a)/n
    for i in range(n):
        k = k + h*(f(i*h+a) + 4*f(i*h+a+0.5*h) + f(i*h + h + a))/6
    return k
def monteCarlo(f,a,b,n):
    h = b-a
    u = 0
    k = 0
    for j in range(n):
        c = random.uniform(a,b)
        k = k + f(c)
    k = h*k/n
    return k

def euler(f,x1,x2,y,h):
    if x2<x1:
        h = -1*h
    k = math.floor((x2-x1)/h)
    for i in range(k):
        y = y + h*f(x1,y)
        x1 = x1 + h
    return y
def pred_corr(f,x1,x2,y,h):
    if x2<x1:
        h = -1*h
    k = math.floor((x2-x1)/h)
    for i in range(k):
        c = y + h*f(x1,y)
        y = y + 0.5*h*(f(x1,y) + f(x1+h,c))
        x1 = x1 + h
    return y
def rk4(f,x1,x2,y,h):
    if x2<x1:
        h = -1*h
    k = math.floor((x2-x1)/h)
    for i in range(k):
        k1 = h*f(x1,y)
        k2 = h*f(x1+ 0.5*h,y + 0.5*k1)
        k3 = h*f(x1+ 0.5*h,y + 0.5*k2)
        k4 = h*f(x1+ h,y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6
        x1 = x1 + h
    return y
def rk4s(f,f1,x1,x2,y,z,h):
    if x2<x1:
        h = -1*h
    k = math.floor((x2-x1)/h)
    for i in range(k):
        k1y = h*f(x1,z)
        k2y = h*f(x1+ 0.5*h,z + 0.5*k1z)
        k3y = h*f(x1+ 0.5*h,z + 0.5*k2z)
        k4y = h*f(x1+ h,z + k3z)
        k1z = h*f1(x1,y,z)
        k2z = h*f1(x1+ 0.5*h,y + 0.5*k1y,z)
        k3z = h*f1(x1+ 0.5*h,y + 0.5*k2y,z)
        k4z = h*f1(x1+ h,y + k3y,z)
        y = y + (k1y + 2*k2y + 2*k3y + k4y)/6
        y1 = y + (k1z + 2*k2z + 2*k3z + k4z)/6
        x1 = x1 + h
    return y
def rk4d(f,x1,x2,y,z,h):
    if x2<x1:
        h = -1*h
    k = math.floor((x2-x1)/h)
    for i in range(k):
        k1 = h*f1(x1,y,z)
        k2 = h*f1(x1+ 0.5*h,y + 0.5*k1,z)
        k3 = h*f1(x1+ 0.5*h,y + 0.5*k2,z)
        k4 = h*f1(x1+ h,y + k3,z)
        y = y + (k1y + 2*k2y + 2*k3y + k4y)/6
        x1 = x1 + h
    return y






        
        








