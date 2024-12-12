import sys

K = int(sys.stdin.readline())

L = []

for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        L.pop()
    else:
        L.append(N)
        
print(sum(L))