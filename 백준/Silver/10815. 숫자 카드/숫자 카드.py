import sys
N = int(sys.stdin.readline())
N_L = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_L = list(map(int,sys.stdin.readline().split()))
D = {}
for i  in range(N):
    D[N_L[i]] = 0
for j in range(M):
    if M_L[j] in D :
        print(1,end =" ")
    else :
        print(0,end =" ")