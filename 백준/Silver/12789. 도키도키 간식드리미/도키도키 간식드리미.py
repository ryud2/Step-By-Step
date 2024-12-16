import sys

N = int(sys.stdin.readline())

Number = list(map(int,sys.stdin.readline().split()))

Side = []

k = 1

i = 0

while i < N :
    
    if Number[i] == k:
        k += 1
        
    elif len(Side) != 0 and Side[-1] == k :
        Side.pop()
        k += 1
        i -= 1

    else :
        Side.append(Number[i])
    
    i += 1

for i in range(len(Side) -1):
    if Side[i] == Side[i+1] +1 :
        pass
    else :
        print("Sad")
        break
else :
    print("Nice")