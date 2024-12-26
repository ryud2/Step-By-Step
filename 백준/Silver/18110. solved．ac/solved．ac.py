import sys

def Round(num):
    if num - int(num) >= 0.5:
        return int(num) +1
    else :
        return int(num)
    
N = int(sys.stdin.readline())

S = []

if N == 1 or N == 2 or N == 3:
    
    for i in range(N):
        S.append(int(sys.stdin.readline()))
        
    print(Round(sum(S)/len(S)))
    
else:
    
    for i in range(N):
        S.append(int(sys.stdin.readline()))

    S.sort()

    D = Round(N*0.15)

    print(Round(sum(S[D:-D])/int(len(S) - 2*D))if len(S[D:-D]) else 0 )