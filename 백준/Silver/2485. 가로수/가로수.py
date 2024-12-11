import sys
import math
N = int(sys.stdin.readline())
D = []
M = {}
for i in range(N):
    D.append(int(sys.stdin.readline()))
for i in range(N-1):
    M[D[i+1] - D[i]] = 0
M = list(M)
print((max(D) -min(D))// math.gcd(*M) -len(D) +1)