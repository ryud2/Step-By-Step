import sys

N,K= map(int,sys.stdin.readline().split())

Temp = N
Result = 1

for i in range(1,K+1):
    Result = Result * Temp // i
    Temp -= 1
    
print(Result)