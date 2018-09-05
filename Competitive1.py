n=input()
n=int(n)
arr=[]
arrO=[]
for i in range(n):
    arr.append(int(input()))
A=0
B=0
C=0
def minim(Ad,Bd,Cd):
    if(Ad<=Bd and Ad<=Cd):
        return 'A'
    elif(Bd<=Ad and Bd<=Cd):
        return 'B'
    elif(Cd<=Ad and Cd<=Bd):
        return 'C'
for i in range(n):
    konsa=minim(A,B,C)
    arrO.append(konsa)
    if(konsa=='A'):
        A=A+arr[i]
    elif(konsa=='B'):
        B=B+arr[i]
    if(konsa=='C'):
        C=C+arr[i]
print(arrO)
