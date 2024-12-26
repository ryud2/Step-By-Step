import sys

N = int(sys.stdin.readline())

D = []
R = []

for i in range(N):
    D.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    count = 1
    for j in range(N):
        if D[i][0] < D[j][0] and D[i][1] < D[j][1]:
            count += 1
    R.append(count)
    
for i in R:
    print(i , end = " ")