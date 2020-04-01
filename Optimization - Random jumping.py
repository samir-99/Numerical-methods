import random

def f(x,y):
    return x-y+2*x*x+2*x*y+y*y

n=1000
a=[]
for x in range(n):
    c=random.uniform(0,1)
    b=random.uniform(0,1)
    a.append(f(c,b))

print(min(a))

    
