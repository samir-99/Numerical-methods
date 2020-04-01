import random

def f(x):
    x1=x[0]
    x2=x[1]
    return (x1**2+x2-11)**2+(x1+x2**2-7)**2

l=0
u=2

maxit=int(input('max numb of iterations: '))

x=[0.5,0.5]
fx=f(x)


i=0
xtmp=x


while(i<=maxit):
    r=random.random()
    if i%2==0:
        xtmp[0]=x[0]+((u-l)/6)*(r-0.5)
        fxtmp=f(xtmp)
        if (xtmp[0]<l or xtmp[0]>u):
            continue

        i=i+1

        if(fxtmp<fx):
            x[0]=xtmp[0]
            fx=fxtmp
        else:
            continue

    else:
        xtmp[1]=x[1]+((u-l)/6)*(r-0.5)
        fxtmp=f(xtmp)
        if (xtmp[1]<l or xtmp[1]>u):
            continue

        i=i+1

        if(fxtmp<fx):
            x[1]=xtmp[1]
            fx=fxtmp
        else:
            continue


print('minimum: ',x)
print('value: ',fx)
        
        
