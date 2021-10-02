from Ass5 import*

print(" Q.1 \n")

def func1(x):
    x = float(x)
    return math.log(x/2,math.e) - math.sin(2.5*x)

print(bisection(func1,1.6,2.4))
print(func1(bisection(func1,1.6,2.4)))
bisectable(func1,1.6,2.4)
print(regula_falsi(func1,1.6,2.4))
print(func1(regula_falsi(func1,1.6,2.4)))
regulatable(func1,1.6,2.4)

print("\n \n Q.2 \n")

def func2(x):
    return -x - math.cos(x)
def dfunc2(x):
    return -1 + math.sin(x)

print(bisection(func2,1.6,2.4))
print(func2(bisection(func2,1.6,2.4)))
bisectable(func2,1.6,2.4)
print(regula_falsi(func2,1.6,2.4))
print(func2(regula_falsi(func2,1.6,2.4)))
regulatable(func2,1.6,2.4)
print(newton_raphson(func2,dfunc2,0.0))
print(newton_table(func2,dfunc2,0.0))

print("\n \n Q.3 \n")
print("The roots of the polynomial are as follows")
print(laguerre(-1,4,[4,0,-5,0,1]))
