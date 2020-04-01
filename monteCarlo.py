from random import randint
def rand():
    return randint(1,4)
x,t=map(int,input("Enter x and t: ").split())
arr1=[int(i) for i in input().split()]
arr2=[int(i) for i in input().split()]
arr3=[int(i) for i in input().split()]
arr4=[int(i) for i in input().split()]
arr=[[0]*x for i in range(t)]
arr[0],arr[t-1]=arr1,arr4
for i in range(len(arr2)):
    arr[i+1][0]=arr2[i]
for i in range(len(arr3)):
    arr[i+1][x-1]=arr3[i]
def prnt(arr):
    for i in arr:
        print(*i)
prnt(arr)
n=int(input("Enter number of iter: "))
c,d=map(int,input("Initial Coordinates as a and b: ").split())
liss=[]
for i in range(n):
    a,b=c,d
    while(True):
        dirr=rand()
        if dirr==1:
            b-=1
        elif dirr==2:
            b+=1
        elif dirr==3:
            a+=1
        elif dirr==4:
            a-=1
        if arr[a][b]!=0:
            break
    liss.append(arr[a][b])
print("Approximately value is ",sum(liss)/n)
