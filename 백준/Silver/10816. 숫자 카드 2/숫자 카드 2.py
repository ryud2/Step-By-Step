import sys
N = int(sys.stdin.readline().strip())
N_L = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M_L = list(map(int,sys.stdin.readline().split()))
D = {}
for i in range(N):
    if N_L[i] in D:
        D[N_L[i]] += 1
    else :
        D[N_L[i]] = 1
for j in M_L:
    print(D.get(j,0), end =" ")