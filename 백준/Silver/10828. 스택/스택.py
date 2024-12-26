import sys

N = int(sys.stdin.readline())

S = []

for i in range(N):
    
    command = list(map(str,sys.stdin.readline().split()))
    
    if command[0] == "push" :
        S.append(command[1])
        
    if command[0] == "pop":
        if len(S) == 0:
            print(-1)
        else :
            print(S.pop())
            
    if command[0] == "size":
        print(len(S))
        
    if command[0] == "empty":
        if len(S) == 0:
            print(1)
        else :
            print(0)
    
    if command[0] == "top":
        if len(S) == 0:
            print(-1)
        else :
            print(S[-1])