import math

def f(x):
    return math.exp(-x**2)

a=int(input("Lower boundary: "))
b=int(input("Top boundary: "))
numb=1000



h=(b-a)/numb
a=0
x=a

for i in range (1,numb):
    a+=h*(f(x)+f(x+h))/2
    x+=h

print(a)

