import sys
N ,M = map(int,sys.stdin.readline().split())
DNum= {}
DName = {}
for i in range(1,N+1):
    P = sys.stdin.readline().strip()
    DName[P] = i
    DNum[i] = P
for j in range(M):
    K = sys.stdin.readline().strip()
    try:
        print(DNum.get(int(K)))
    except:
        print(DName.get(K))