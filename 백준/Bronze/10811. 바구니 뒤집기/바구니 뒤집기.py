N , M = map(int,input().split())
A = [p for p in range(1,N+1)]
for k in range(M):
    i , j = map(int,input().split())
    A[i-1:j] = reversed(A[i-1:j])
print(*A)