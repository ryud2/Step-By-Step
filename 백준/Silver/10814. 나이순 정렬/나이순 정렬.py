import sys
N = int(input())
S = []
for i in range(N):
    S.append(sys.stdin.readline().strip().split())
for i in range(N):
    S[i][0] = int(S[i][0])
S.sort(key = lambda S:S[0])
for i in S:
    print(*i)