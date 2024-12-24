import sys

N = int(sys.stdin.readline())

L = []

for i in range(N):
    L.append(int(sys.stdin.readline()))

L.sort()
    
print(round(sum(L)/N))

print(L[N//2])

S = list(set(L))


R = []

M = []

for i in S:
    R.append(L.count(i))

MR = max(R)

if R.count(MR) == 1 :
    print(S[R.index(MR)])
else :
    for k in range(len(R)):
        if R[k] == MR:
            M.append(S[k])
    print(sorted(M)[1])

print(L[-1] - L[0])