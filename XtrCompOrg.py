def searchDiv(division):
    for i in range(N):
        if(div[i]==division): #searches the division in the initial list given
            return i #and then returns the row number which has the corresponding division name
def goDown(division):
    childs = []
    for i in range(N):
        if(parent[i]==division)
            childs.append(i)
    return childs
def goUp(division):#returns the index of direct parent and the index of other node of that parent
    for i in range(N):
        if(div[i]==division):
            itsParent=parent[i]
            itsChilds=goDown(itsParent)
            return itsChilds[0],itsChilds[1]
line1=input()
N=int(line1.split(" ")[0])
Q=int(line1.split(" ")[1])
#print(N,Q)
div = ["" for x in range(N)]
parent = ["" for x in range(N)]
size1 = ["" for x in range(N)]
size2 = ["" for x in range(N)]
for i in range(N):
    query=input()
    queryDiv=query.split(" ")
    div[i],parent[i],size1[i],size2[i]=queryDiv[0],queryDiv[1],int(queryDiv[2]),int(queryDiv[3])
    #print(div[i],parent[i],size1[i],size2[i])
# for j in range(Q):#Queries the actual array needed for the output
query=input().split(" ")
divisionName,ansType=query[0],int(query[1])
print("here",divisionName,ansType)
if(ansType==1):#for type 1
    row=searchDiv(divisionName)#the row in complete data
    if(size1!=0):
        minim,maxim=size1[row],size1[row]
        print(minim,maxim)
    else:
        if(size2!=0):
            
