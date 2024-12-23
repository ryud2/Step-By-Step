import sys

while True:
    N = list(sys.stdin.readline().strip())
    if N == ['0'] :
        break
    for i in range(1,len(N)//2 +1):
        if N[i-1] == N[-i]:
            pass
        else :
            print("no")
            break
    else:
        print("yes")