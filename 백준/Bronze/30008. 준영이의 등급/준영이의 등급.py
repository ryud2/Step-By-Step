import sys

D = 0
S = []
C = [4,11,23,40,60,77,89,96,100]
N , K = map(int,sys.stdin.readline().split())

G = list(map(int,sys.stdin.readline().split()))

for i in range(K):
    D = int( G[i]/N *100 )
    for j in range(9):
        if D <= C[j]:
            S.append(j+1)
            break
print(*S)