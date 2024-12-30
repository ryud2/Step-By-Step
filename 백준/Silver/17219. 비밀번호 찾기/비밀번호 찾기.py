import sys

N , M = map(int,sys.stdin.readline().split())

Store = {}

for i in range(N):
    site , ps = map(str,sys.stdin.readline().strip().split())
    Store[site] = ps
    
for k in range(M):
    print(Store[sys.stdin.readline().strip()])