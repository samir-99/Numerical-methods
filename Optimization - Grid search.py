def f(x,y):
    return x**2+y**2

a=int(input("lower boundary: "))
b=int(input("upper boundary: "))

h=float(input())

x=[]
y=[]
while(a<=b):
    x.append(a)
    y.append(a)
    a=a+h

minn=f(x[0],y[0])
for i in x:
    for j in y:
        new=f(i,j)
        if new<minn:
            minn=new
print(minn)
