add=0
answer=0
def searchDiv(division):
    for i in range(N):
        if(div[i]==division): #searches the division in the initial list given
            return i #and then returns the row number which has the corresponding division name
def goDown(division):
    childs = []
    for i in range(N):
        if(parent[i]==division):
            childs.append(i)
    return childs
def goUp(division):#returns the index of direct parent and the indices of other nodes of that parent
    for i in range(N):
        if(div[i]==division):
            itsParent=parent[i]
            if(itsParent!="NONE"):
                itsChilds=goDown(itsParent)
                for m in range(N):
                    if(div[m]==itsParent):
                        return m,itsChilds
            else:
                return [],[]
def calcSum(childrenL):
    addL=0
    for l in childrenL:
        if(size2[l]!=0):
            addL=addL+size2[l]
        else:
            furChild=goDown(div[l])
            if(furChild!=[]):
                addL=addL+calcSum(furChild)
            else:
                continue
                flag=1#Flag to be included
    return addL
def size2Neigh(neighbors,row):
    add=0
    for m in neighbors:
        if(m!=row):
            add=add+size2[m]
        else:
            continue
    return add
def fetchAll(divisionName,row):
    Pnode, children = goUp(divisionName)
    Psize2=size2[Pnode]
    Psize1=size1[Pnode]
    print("P",Pnode, children)
    if(Psize1!=0 and Psize2!=0):
        total=Psize2-Psize1
        neighSize2=size2Neigh(children,row)
        return (total-neighSize2)
    elif(Psize2==0):
        size2[Pnode]=fetchAll(div[Pnode],Pnode)
        fetchAll(divisionName,row)
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
for j in range(Q):#Queries the actual array needed for the output
    query=input().split(" ")
    divisionName,ansType=query[0],int(query[1])
    #print(divisionName,ansType)
    if(ansType==1):#for type 1
        print("ansType 1 me")
        row=searchDiv(divisionName)#the row in complete data
        if(size1[row]!=0):
            minim,maxim=size1[row],size1[row]
            #print(goDown(divisionName))
            #print(goUp(divisionName))
            print(minim,maxim)
        else:
            #print("ansType 1 ke else me- when size is not given directly")
            add=0;
            flag=0;
            if(size2[row]!=0):
                children=goDown(divisionName)
                if(children!=[]):
                    addLoc=calcSum(children)
                    add=add+addLoc
                    if(flag==0):
                        minim, maxim=size2[row]-add,size2[row]-add
                    else:
                        minim, maxim=1,size2[row]-add
            else:
                fetchSize2=fetchAll(divisionName,row)
                print(fetchSize2)
                addDown=0
                children=goDown(divisionName)
                flag=0
                addDown=addDown+calcSum(children)
                if(flag==0):
                    minim,maxim=fetchSize2-addDown
                else:
                    print("to be coded")
            
    elif(ansType==2):
        print("ansType 2 me")
        row=searchDiv(divisionName)
        if(size2[row]!=0):
            maxim, minim=size2,size2
        else:
            total=0
            itsSize2=fetchAll(divisionName, row)
            # Pnode, children = goUp(divisionName)
            # Psize2=size2[Pnode]
            # Psize1=size1[Pnode]
            # print("P",Pnode, children)
            # if(Psize1!=0 and Psize2!=0):
            #     total=Psize2-Psize1
            #     neighSize2=size2Neigh(children,row)
            minim,maxim=itsSize2,itsSize2
        print(minim,maxim)
