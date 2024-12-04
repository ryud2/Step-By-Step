N , M = map(int,input().split())
A = [[0 for p in range(M)] for q in range(N)]
B = []
while True:
    try:
            for q in range(N):
                B = list(map(int,input().split()))
                for p in range(M):
                    A[q][p] = A[q][p] + B[p]
    except:
        break
for i in range(N):
    print(*A[i])