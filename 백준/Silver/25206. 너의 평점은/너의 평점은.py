S = 0 
n = 0
Hak = ["F","D0","D+","C0","C+","B0","B+","A0","A+"]
for i in range(20):
    A = []
    A = input().split()
    if A[2] == "P" :
        continue
    else :
        n += float(A[1])
        if A[2] == "F" :
            pass
        else:
            S += float(A[1]) *( (Hak.index(A[2])/2) + 0.5)
print( S / n)