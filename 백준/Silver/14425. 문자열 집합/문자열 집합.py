import sys
N , M = map(int,input().split())
A = []
B = []      
for i in range(N):
    A.append(sys.stdin.readline().strip())
for j in range(M):
    B.append(sys.stdin.readline().strip())
C = 0
D = {}
for i in range(N):
    D[A[i]] = 0
for j in range(M):
    if B[j] in A:
        C +=1
print(C)