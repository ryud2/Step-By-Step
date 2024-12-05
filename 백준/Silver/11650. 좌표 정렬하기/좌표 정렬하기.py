N = int(input())
D = []
for i in range(N):
    D.append(list(map(int,input().split())))
D.sort()
for i in range(N):
    print(*D[i])