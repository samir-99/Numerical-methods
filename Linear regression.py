x=[]
y=[]
n=int(input("number of points: "))
#input values
for i in range(0,n):
	x.append(float(input("x= ")))
	y.append(float(input("y= ")))

sumy=0
sumx=0
sumxx=0
sumxy=0
i=0
while (i<len(x)):
    sumx=sumx+x[i]
    sumy=sumy+y[i]
    sumxx=sumxx+x[i]*x[i]
    sumxy=sumxy+x[i]*y[i]
    i=i+1

print(sumx,sumy,sumxx,sumxy)

slope=(n*sumxy-sumx*sumy)/(n*sumxx-sumx*sumx)
intercept=(sumy-slope*sumx)/n

equation=str(slope)+'x +'+str(intercept)
print(equation)
