import sys
N  = int(input())
A = [int(sys.stdin.readline().strip()) for i in range(N)]
print(*sorted(A),sep="\n")