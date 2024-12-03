N = int(input())
A = [[0 for i in range(100)] for i in range(100)]
for i in range(N):
    q, p = map(int,input().split())
    for i in range(q,q+10):
        for j in range(p,p+10):
            A[i][j] =1
S= 0
for i in range(100):
    S += A[i].count(1)
print(S)