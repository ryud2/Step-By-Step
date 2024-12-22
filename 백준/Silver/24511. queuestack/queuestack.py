import sys
from collections import deque

N = int(sys.stdin.readline())

A = deque(map(int,sys.stdin.readline().split()))

B = deque(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

C = deque(map(int,sys.stdin.readline().split()))



for i in range(N):
    if A[i] == 0:
        C.appendleft(B[i])
        
for i in range(M):
    print(C[i] , end = " ")