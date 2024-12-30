import sys

M = int(sys.stdin.readline())

S = []

for i in range(M):
    command = list(map(str,sys.stdin.readline().split()))
    
    if command[0] == "add":
        if command[1] not in S :
            S.append(command[1])
 
    if command[0] == "remove":
        if command[1] in S :
            S.remove(command[1])
    
    if command[0] == "toggle":
        if command[1] not in S :
            S.append(command[1])
        else:
            S.remove(command[1])

    if command[0] == "check":
        if command[1] not in S :
            print(0)
        else:
            print(1)
            
    if command[0] == "all":
        S = [str(i) for i in range(1,21)]
        
    if command[0] == "empty":
        S = []