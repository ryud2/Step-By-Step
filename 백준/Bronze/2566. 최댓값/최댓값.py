A = [list(map(int,input().split())) for i in range(9)]
B = [max(A[i]) for i in range(9)]
print(max(B))
for p in range(9):
    for q in range(9):
        if A[p][q] == max(B):
            print(p+1 , q+1)