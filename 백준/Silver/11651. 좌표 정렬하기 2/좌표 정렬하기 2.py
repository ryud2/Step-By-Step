N = int(input())
D = []
for i in range(N):
    D.append(list(map(int,input().split())))

D.sort(key = lambda D:D[0])
D.sort(key = lambda D:D[1])
for i in range(N):
    print(*D[i])