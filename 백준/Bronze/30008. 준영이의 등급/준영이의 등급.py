import sys

D = 0
S = []

N , K = map(int,sys.stdin.readline().split())

G = list(map(int,sys.stdin.readline().split()))

for i in range(K):
    D = int( G[i]/N *100 )
    if D <= 4 :
        S.append(1)
    elif D <= 11 :
        S.append(2)
    elif D <= 23 :
        S.append(3)
    elif D <= 40 :
        S.append(4)
    elif D <= 60 :
        S.append(5)
    elif D <= 77 :
        S.append(6)
    elif D <= 89 :
        S.append(7)
    elif D <= 96 :
        S.append(8)
    else :
        S.append(9)

print(*S)