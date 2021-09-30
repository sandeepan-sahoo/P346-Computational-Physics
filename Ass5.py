import math
def func1(x):
    x = float(x)
    return math.log(x/2,math.e) - math.sin(2.5*x)
def bisection(f,a,b):
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

def bisectable(f,a,b):
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
            print(str(i) + "   " + str(f(c)))
def regulatable(f,a,b):
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
            print(str(i) + "   " + str(f(c)))
            
def regula_falsi1(f,a,b):
    if f(a)*f(b)<0:
        c = float((a*f(b)-b*f(a))/(f(b)-f(a)))
        while abs(func1(c))>0.00001:
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
def func2(x):
    return -x - math.cos(x)
def dfunc2(x):
    return -1 + math.sin(x)

def newton_raphson2(x):
    while abs(f(x))>0.00001:
        if abs(df(x))>0.001:
            x = x - func2(x)/dfunc2(x)
        else:
            break
    if abs(f(x))<=0.00001:
        return x
def newton_table2(x):
    i = 0
    while abs(f(x))>0.00001:
        if abs(df(x))>0.001:
            x = x - f(x)/df(x)
            i = i + 1
            print(str(i) + "   " + str(f(x)))
def func3(x):
    return pow(x,4) - (5*pow(x,2)) + 4
def dfunc3(x):
    return 4*pow(x,3) - (10*x)
def d2func3(x):
    return 12*pow(x,2) - 10
def abmax(c,d):
    if abs(c)>abs(d):
        return c
    else:
        return d
global roots = []
def laguerre(f,df,d2f,x,n):
    while f(x)>0.00001:
        g = df(x)/f(x)
        h = g*g - d2f(x)/f(x)
        a = n/abmax(g + math.sqrt((n-1)*(n*h-g*g)),g - math.sqrt((n-1)*(n*h-g*g)))
        x = x - a
        roots.append(x)
        f=syndiv(f,x)
        laguerre(f,df,d2f,x,n)
        
                
        
        









        
        
