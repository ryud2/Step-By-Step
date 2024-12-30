import sys

N , K = map(int,sys.stdin.readline().split())

cost = []

for i in range(N):
    cost.append(int(sys.stdin.readline()))


total = 0

i = 1
count = 0

while K != 0 :
    if K//cost[-i] == 0:
        i += 1
    else:
        temp = K//cost[-i]
        count += temp
        K -= temp*cost[-i]
        
print(count)