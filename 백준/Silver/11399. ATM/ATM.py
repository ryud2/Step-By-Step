import sys

N = int(sys.stdin.readline())

L = list(map(int,sys.stdin.readline().split()))

L.sort()

total = 0

temp = 0

for i in L:
    temp += i
    total += temp
print(total)