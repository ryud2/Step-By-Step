import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    N , M = map(int,sys.stdin.readline().split())
    L = deque(map(int,sys.stdin.readline().split()))
    k = 0
    for i in L:
        L[k] = (i,k)
        k += 1
    c = 1
    while True:
        if L[0][0] == max(L , key = lambda x:x[0])[0]:
            if L[0][1] == M:
                print(c)
                break
            else:
                del L[0]
                c += 1
        else:
            L.append(L.popleft())