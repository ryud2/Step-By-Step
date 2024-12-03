import math
N = int(input())
A = []
C = 0
for p in range(1,N):
    A =[]
    i = p
    for k in range(int(math.log10(i)),-1,-1):
        temp = i//(10**k)
        A.append(temp)
        i -= temp*10**k
    if sum(A) + p == N:
        print(p)
        break
    else :
        C += 1
if C == N-1:
    print(0)
