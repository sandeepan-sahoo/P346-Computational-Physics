import math
def func1(x):
    x = float(x)
    return math.log(x/2,math.e) - math.sin(2.5*x)
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
            print(str(i) + "   " + str(f(c)))
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
            print(str(i) + "   " + str(f(c)))
            
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
def func2(x):
    return -x - math.cos(x)
def dfunc2(x):
    return -1 + math.sin(x)

def newton_raphson(f,df,x):
    while abs(f(x))>0.00001:
        if abs(df(x))>0.001:
            x = x - f(x)/df(x)
        else:
            break
    if abs(f(x))<=0.00001:
        return x
def newton_table(f,df,x):
    i = 0
    print("Table by Newton Raphson method")
    print("i" + "   " + "f(x)")
    while abs(f(x))>0.00001:
        if abs(df(x))>0.001:
            x = x - f(x)/df(x)
            i = i + 1
            print(str(i) + "   " + str(f(x)))
def pol(x,args):
    p=0
    for i in range(len(args)):
        p = p + args[i]*pow(x,i)
    return p
def dpol(x,args):
    p=0
    for i in range(len(args)):
        if  i!=0:
            p = p + i*args[i]*pow(x,i-1)
    return p
def d2pol(x,args):
    p=0
    for i in range(len(args)):
        if  i!=0 and i!=1:
            p = p + i*(i-1)*args[i]*pow(x,i-2)
    return p
    
def abmax(c,d):
    if abs(c)>abs(d):
        return c
    else:
        return d
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
def laguerre(x,n,args):
    roots = []
    v = n
    for i in range(v):
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
        args = syndiv(x,n,args)
        n=n-1
    return roots

        
                
        
        









        
        
