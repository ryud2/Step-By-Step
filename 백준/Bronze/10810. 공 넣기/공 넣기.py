N , M = map(int,input().split())
A = []
for i in range(N):
    A.append(0)
for p in range(M):
    i , j , k = map(int,input().split())
    for q in range(i-1,j):
        A[q] = k
for u in A:
    print(u , end = " ")