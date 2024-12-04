N = int(input())
A = [int(input()) for i in range(N)]
A.sort()
print(*A,sep="\n")