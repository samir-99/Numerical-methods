def f(x):
    return x**2

a=float(input('Enter the lower boundary: '))
b=float(input('Enter the upper boundary: '))
n=int(input('Number of steps( number of steps must be even): '))
h=(b-a)/n

result=0
i=0

flist=[]
while i<=n:
    x=a+i*h
    flist.append(x)
    i=i+1

i=0
while (i<=n):
    if i==0 or i==n:
        result=result+flist[i]
    elif i%2 != 0 :
        result=result+4*flist[i]
    else:
        result=result+2*flist[i]
    i=i+1

result=result*(h/3)
print("Approximate value: ",result)

