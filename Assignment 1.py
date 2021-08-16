#Question 1
    #Sum of first n natural numbers
import math
n = input("Enter a natural number: ")
n = int(n)
k= math.floor(n)
s=0
if (n-k) ==0 and n>0:
    for i in range(1,n+1):
        s = s + i
    print("The sum of first n natural numbers is " + str(s))
else:
    print("Not a natural number")

    #Sum of first n Odd numbers
odno = input("enter the number of odd numbers whose sum you want to calculate: ")
odno = int(odno) 
h = math.floor(odno)
osum = 0
if (odno - h) == 0 and odno>0: 
    for i in range(1, 2*odno):
        if i%2==1:
            osum = osum + i
    print("The sum of first n odd numbers is " + str(osum))
else:
    print("Not a natural number")



#Question 2
    #Sum of N terms of an AP having common difference 1.5
a = input("Enter the initial value of AP: ")
a = int(a)
apt = input("Entere the term number of AP: ")
apt = int(apt)
apt = int(apt)
apsum = 0
if (apt- math.floor(apt))==0 and apt>0:
    for i in range(apt):
        apsum = apsum + a
        a = a+1.5
    print("The sum of " + str(apt)+" terms of AP is " + str(apsum))
else:
    print("Term number is unacceptable")

#Sum of N terms of a GP with common ratio 0.5
g = input("Enter the initial value of GP: ")
g = int(g)
gpt = input("Entere the term number of GP: ")
gpt = int(gpt)
gpsum = 0
if (gpt - math.floor(gpt))==0 and gpt>0:
    for i in range(gpt):
        gpsum = gpsum + g
        g = g*0.5
    print("The sum of " + str(gpt)+" terms of GP is " + str(gpsum))
else:
    print("Term number is unacceptable")
        
#Sum of N terms of HP having common difference 0.5
h = input("Enter the initial value of HP: ")
h = float(h)
hpt = input("Entere the term number of HP: ")
hpt = int(hpt)
hpsum = 0
if (hpt - math.floor(g=hpt))==0 and hpt>0 and h!=0: 
    for i in range(hpt):
        hpsum = hpsum + h
        h = 1/h
        h = h + 0.5
        h = 1/h
    print("The sum of " + str(hpt)+" terms of HP is " + str(hpsum))
elif h==0:
    print("Initisl number value cannot be zero")
else:
    print("Term number is unacceptable")

#N factorial
n = input("Enter the number whose factorial you wish to find: ")
n = int(n)
def factorial(n):
    fact = 1
    if (n-math.floor(n)) ==0 and n>0:
        for i in range(1,n+1):
            fact = fact*i
    return fact
if n!=0:
    print("factorial of " + str(n) + " is " + str(factorial(n)))
if n==0:
    print("factorial of O is 1")


#Sin x
x = input("Enter small x: " )
x = float(x)
sinx = 0
for i in range(40):
          sinx = sinx + pow(-1,i)*pow(x,2*i+1)/factorial(2*i+1)
if sinx-sin(x)<=0.00001:
    print(sinx)
else:
    print("x ain't small enough")

#exp x
x = input("Enter small x: " )
x = float(x)
expx = 0
for i in range(10):
    expx = expx + pow(x,i)/factorial(i)
print(expx)
         


        
        

    

