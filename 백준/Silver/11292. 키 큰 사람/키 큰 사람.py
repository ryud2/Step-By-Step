import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        List = []
        A = []
        for i in range(N):
            List.append(list(map(str,sys.stdin.readline().strip().split())))
        List.sort(key= lambda x:x[1])
        for k in range(1,N+1):
            if List[-k][1] == List[-1][1]:
                A.append(List[-k][0])
            else:
                break
        A.reverse()
        print(*A)