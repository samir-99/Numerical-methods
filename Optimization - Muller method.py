def f(x):
    return x**2-5*x-6

def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

print("initial guesses")
x1=float(input("x1= "))
x2=float(input("x2= "))
x3=float(input("x3= "))

eps=float(input("epsilon: "))
error=999
while (error>eps):
    y1=f(x1)
    y2=f(x2)
    y3=f(x3)
    c1=(y2-y1)/(x2-x1)
    c2=(y3-y2)/(x3-x2)
    d1=(c2-c1)/(x3-x1)
    s=c2+d1*(x3-x2)
    x4=x3-2*y3/(s+sign(s)*(s*s-4*y3*d1)**1/2)
    error=abs(f(x4))
    x1=x2
    x2=x3
    x3=x4

print(x4)
    
