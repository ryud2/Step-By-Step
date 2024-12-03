N , M = map(int,input().split())
A = list(map(int,input().split()))
B = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or i == k or j == k:
                continue
            else:
                if (A[i]+A[j]+A[k] - M) <= 0:
                    B.append((A[i]+A[j]+A[k]))
print(max(B))