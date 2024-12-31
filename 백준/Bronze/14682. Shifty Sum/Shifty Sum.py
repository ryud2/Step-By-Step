import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

sum = 0

for i in range(k+1):
    sum += N*(10**i)
    
print(sum)