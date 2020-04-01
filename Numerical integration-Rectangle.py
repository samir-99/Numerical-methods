def f(x):
    return x**2

a=float(input('Enter the lower boundary: '))
b=float(input('Enter the upper boundary: '))
n=int(input('Number of steps: '))
h=(b-a)/n

result=0
i=0

flist=[]
while i<=n:
    x=a+i*h
    flist.append(x)
    i=i+1

i=0
while i<n:
    result=result+h*flist[i]
    i=i+1

print("Approximate value: ",result)
