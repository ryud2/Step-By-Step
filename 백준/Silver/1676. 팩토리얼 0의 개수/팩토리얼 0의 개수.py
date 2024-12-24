import sys

N = int(sys.stdin.readline())
Sum = 1

for i in range(1 , N+1):
    Sum *=i

k = 0

while Sum % 10 == 0:
    Sum = Sum // 10 
    k +=1
    
print(k)