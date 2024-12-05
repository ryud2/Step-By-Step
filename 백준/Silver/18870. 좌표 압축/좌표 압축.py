import sys
N = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().split()))
A = sorted(list(set(S)))
D = {}
for k in range(len(A)):
    D[(str(A[k]))] = k
for i in S:
    print(D[str(i)] , end =" ")