import sys
N = int(input())
S = []
for i in range(N):
    S.append(sys.stdin.readline().strip())
S = list(set(S))
S.sort()
S.sort(key = len)
for i in S:
    print(i)