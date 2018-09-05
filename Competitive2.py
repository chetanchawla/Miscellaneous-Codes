n=int(input())
arrI=[]
count=0
for i in range(n):
    arrI.append(int(input()))
for i in range(n):
    temp1=arrI[i]
    for j in range(i+1,n):
        temp2=arrI[j]
        if((int(temp1)+int(temp2))%60==0):
            count=count+1
        else:
            continue
print(count)
