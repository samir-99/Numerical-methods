import math
def f(x):
    return x*x*x-math.cos(x)
def fp(x):
    return 3*x*x+math.sin(x)

x0=float(input("Initial guess: "))
eps=float(input("error: "))

x=x0-f(x0)/fp(x0)
while(abs(f(x)-f(x0))>eps):
    x0=x
    x=x0-f(x0)/fp(x0)

print (x)
