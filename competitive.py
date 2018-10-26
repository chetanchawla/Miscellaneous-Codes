inp=['(','(',')',')','(',')']  
p=[]
for i in range(len(inp)):
    p.append(inp[i])

k=0
for i in range(len(p)):
    element=p.pop()
    if(element=='('):
        k=k+1
    else:
        continue
print(k)
