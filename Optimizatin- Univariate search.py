from sympy import *
import re

def func(x1,x2):
    #return x1-x2+2*x1**2+2*x1*x2+x2**2
    return 100*(x2-x1**2)**2+(1-x1**2)**2
def findL(a,b):
    s='100*(x2-x1**2)**2+(1-x1**2)**2'
    s=re.sub(r'x1', "({})".format(a),s)
    s=re.sub(r'x2', "({})".format(b),s)
    #print(simplify(s),"\n",s,"\n",a,b)
    return solve(diff(simplify(s),"a"))  #use eval()
X=[float(i) for i in input("Enter Starting Point as x1 and x2 : ").split()]
S=[float(i) for i in input("Enter Search direction as s1 and s2 : ").split()]
e=float(input("Enter probe length: "))
ee=0.0000000000000000000000000001
i=0
fL=func(X[0],X[1])
symbolsToDelete = ('a', 'b')
while(True):
    a,b=symbols('a b')
    f=func(X[0],X[1])
    fp=func(X[0]+e*S[0],X[1]+e*S[1])
    fm=func(X[0]-e*S[0],X[1]-e*S[1])
    dirr=0
    if fp<f:
        dirr=1
    elif fm<f:
        dirr=-1
    #print("Direc ",dirr)
    lamb=findL(X[0]+dirr*S[0]*a,X[1]+dirr*S[1]*a)
    if(len(lamb)==0):
        break
    X[0]=X[0]+dirr*min(lamb)*S[0]
    X[1]=X[1]+dirr*min(lamb)*S[1]
    i+=1
    if i%2!=0:
        S=[0,1]
    else:
        S=[1,0]
    for z0 in symbolsToDelete:
        del globals()[z0]
    if(abs(func(X[0],X[1])-f)<ee):
        break
print("X* is {}".format(str(X)))
print("Value of Func at X is {}".format(str(func(X[0],X[1]))))
