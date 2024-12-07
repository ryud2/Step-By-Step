import sys

S = sys.stdin.readline().strip()
D = {}
k = 1
for i in range(len(S)):
    for j in range(len(S)):
        D[S[j:j+i]] = 1
    k += 1 
print(len(D))