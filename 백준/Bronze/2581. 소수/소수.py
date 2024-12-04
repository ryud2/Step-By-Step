N = int(input())
M = int(input())
S = []
for i in range(N, M+1):
    A = [k for k in range(1, i+1) if i % k == 0]
    if len(A) == 2:
        S.append(i)
if len(S) == 0:
    print("-1")
else:
    print(sum(S))
    print(min(S))