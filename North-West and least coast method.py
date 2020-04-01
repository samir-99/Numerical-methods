def north_west(mas,supply,demand):
        i=0
        j=0
        s=0
        while (i!=len(supply)-1 or j!=len(demand)-1):
                #print("Active x=",mas[i][j])
                #print("Active supply=",supply[i])
                #print("Active demand=",demand[j])
                if supply[i]>=demand[j]:
                        #print("Case 1")
                        s+=mas[i][j]*demand[j]
                        supply[i]-=demand[j]
                        j+=1
                else:
                        #print("Case 2")
                        s+=mas[i][j]*supply[i]
                        demand[j]-=supply[i]
                        i+=1
        s+=mas[i][j]*supply[i]
        
        return s

def min_in_mas(mas):
        mincost=min(mas[0])
        mini=0
        for x in range(1,len(mas)):
                if min(mas[x])<mincost:
                        mincost=min(mas[x])
                        mini=x
        minj=0
        for x in range(len(mas[mini])):
                if mincost==mas[mini][x]:
                        minj=x
        m=[mini,minj]

        print(m,mincost)
        return m

def least_cost(mas,supply,demand):
        s=0
        while (mas):
                pos=min_in_mas(mas)
                if supply[pos[0]]>=demand[pos[1]]:
                        print("Case 1")
                        s+=mas[pos[0]][pos[1]]*demand[pos[1]]
                        supply[pos[0]]-=demand[pos[1]]
                        demand=demand[:pos[1]]+demand[pos[1]+1:]
                        for x in range(len(mas)):
                                mas[x]=mas[x][:pos[1]]+mas[x][pos[1]+1:]
                                if len(mas[x])==0:
                                        mas=mas[:x]+mas[x+1:]
                else:
                        print("Case 2")
                        s+=mas[pos[0]][pos[1]]*supply[pos[0]]
                        demand[pos[1]]-=supply[pos[0]]
                        supply=supply[:pos[0]]+supply[pos[0]+1:]
                        mas=mas[:pos[0]]+mas[pos[0]+1:]
                print("MATRIX")
                for x in mas:
                        print(x)
                print("SUPPLY")
                print(supply)
                print("DEMAND")
                print(demand)
                print("S=",s)
        return s


n,m=map(int,input().split())
mas=[]
print("Enter Matrix")
for q in range(m):
        #print("Enter the",q+1,"row:")
        z=[float(x) for x in input().split()]
        mas.append(z)
print("Enter the Supply:")
supply=[float(x) for x in input().split()]
print("Enter the Demand:")
demand=[float(x) for x in input().split()]
#print("North West:",north_west(mas,supply,demand))
print("Least Cost:",least_cost(mas,supply,demand))
input("Press any key to leave...")
