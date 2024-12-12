import sys

T = int(sys.stdin.readline())

L = []

for i in range(T):
    S = list(sys.stdin.readline().strip())
    L = []
    for k in S:
        
        if k == ")":
            try:
                if L[-1] =="(":
                    L.pop()
                    continue
                else:
                    print("NO")
                    break
            except:
                print("NO")
                break
        L.append(k)
    else:
        if len(L) == 0 :
            print("YES")
        else :
            print("NO")