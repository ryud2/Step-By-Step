import sys

T = int(sys.stdin.readline())

for i in range(T):
    
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    Ho = [i for i in range(1,n+1)]
    
    for i in range(k):
        for j in range(1,n):
            Ho[j] = Ho[j] + Ho[j-1]
    
    print(Ho[n-1])