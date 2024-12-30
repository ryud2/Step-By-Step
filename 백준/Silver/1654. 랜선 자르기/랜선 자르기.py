import sys

K , N = map(int,sys.stdin.readline().split())

L = []

for i in range(K):
    L.append(int(sys.stdin.readline()))

start = 1
end = max(L)

while start <= end :
    mid = (start+end) //2
    
    T = 0
    
    for i in L:
        T += i//mid
    
    if T < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)