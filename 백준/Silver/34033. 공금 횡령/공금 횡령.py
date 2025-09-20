import sys
N , M = map(int,input().split())
Junga = {}
sus = 0
for i in range(N):
    a , b = map(str,sys.stdin.readline().split())
    Junga[a] = int(b) 
for j in range(M):
    c , d = map(str,sys.stdin.readline().split())
    if Junga[c]*1.05 < int(d):
        sus +=1
print(sus)