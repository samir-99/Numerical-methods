#Samir Aliyev 652.6e

import math

def a0f(x):
    return x

def anf(x,n,b):
    return x*(math.cos((n*x*math.pi)/b))

def bnf(x,n,b):
    return x*(math.sin((n*x*math.pi)/b))

# input

a=int(input("Lower boundary: "))
b=int(input("Top boundary: "))
numb=100

n=int(input("number of iterations: "))

h=(b-a)/numb 



#calculating coefficent with trapezoid rule

a0=0
x=a

for i in range (1,numb):
    a0=a0+h*(a0f(x)+a0f(x+h))/2
    x=x+h

an=0
x=a

for i in range (1,numb):
    an=an+h*(anf(x,n,b)+anf(x+h,n,b))/2
    x=x+h

bn=0
x=a

for i in range (1,numb):
    bn=bn+h*(bnf(x,n,b)+bnf(x+h,n,b))/2
    x=x+h

a0=(1/b)*a0
an=(1/b)*an
bn=(1/b)*bn

# print

print("a0= ",a0)
print("a= ",an)
print("b= ",bn)
