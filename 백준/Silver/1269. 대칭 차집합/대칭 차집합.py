import sys

N , M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
D = {}
C = 0
for i in range(N):
    if A[i] in D:
        D[A[i]] += 1
    else:
        D[A[i]] = 1
for i in range(M):
    if B[i] in D:
        D[B[i]] += 1
    else:
        D[B[i]] = 1
for V in D.values():
    if V == 1 :
        C +=1
print(C)