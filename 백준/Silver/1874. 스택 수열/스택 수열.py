import sys
from collections import deque

N = int(sys.stdin.readline())

A = [int(sys.stdin.readline()) for _ in range(N)]

L = deque(i for i in range(1,N+1))

Temp = deque()

S = []

T = []

k = 0

try:
    Temp.append(L.popleft())
    T.append("+")

    while S != A:
        if len(Temp) != 0 and Temp[-1] == A[k] :
            k += 1
            T.append("-")
            S.append(Temp.pop())
            
        elif len(L) != 0:
            Temp.append(L.popleft())
            T.append("+")
        else:
            del(T)
            break
    for p in T:
        print(p)
    
except:
    print("NO")