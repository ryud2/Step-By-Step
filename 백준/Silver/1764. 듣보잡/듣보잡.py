import sys

N , M = map(int,sys.stdin.readline().split())
H = {}
S = {}
HS = {}
K = 0

for i in range(N):
    H[sys.stdin.readline().strip()] = 0
for j in range(M):
    temp = sys.stdin.readline().strip()
    if temp in H:
        HS[temp] = 0
        K += 1
    
print(K)
print("\n".join(sorted(HS.keys())))