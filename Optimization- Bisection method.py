import math

def f(x):
    return  x*x*x-math.cos(x)

xl=float(input('lower boundary'))
xu=float(input('upper boundary'))
root=0.8655
eps=0.0001

xc=(xu+xl)/2

while (abs(xc-root)>eps):
    if (f(xl)*f(xc)<0):
        xu=xc
    elif f(xl)*f(xc)>0:
        xl=xc
    elif f(xl)*f(xr)==0:
        break

    xc=(xl+xu)/2
    

print(xc)
