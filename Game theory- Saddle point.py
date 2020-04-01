def maxir(mas):
        mi=mas[0][0]
        for x in mas:
                if mi>max(x):
                        mi=max(x)
        return mi

def minir(mas):
        n=len(mas)
        mim=[]
        for x in range(n):
                m=mas[x][0]
                for y in range(1,n):
                        if m>mas[x][y]:
                                m=mas[x][y]
                mim.append(m)
        return max(mim)

n=int(input())
mas=[]
for x in range(n):
        row=[float(s) for s in input().split()]
        mas.append(row)

maxr=maxir(mas)
minr=minir(mas)
print(maxr,minr)
if maxr==minr:
        print("Saddle point exists")
else:
        print("Saddle point doesn't exist")
