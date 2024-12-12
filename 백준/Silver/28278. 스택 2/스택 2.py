import sys

N = int(sys.stdin.readline())
L = []
for i in range(N):

    command = list(map(int,sys.stdin.readline().split()))
    if command[0] == 1 :
        L.append(command[1])
    if command[0] == 2 :
        if len(L) == 0:
            print(-1)
        else :
            print(L.pop())
            
    if command[0] == 3 :
        print(len(L))
    if command[0] == 4 :
        if len(L) == 0:
            print(1)
        else :
            print(0)    
    if command[0] == 5 :
        if len(L) == 0:
            print(-1)
        else :
            print(L[-1])