import sys

S = 1
for i in range(1 , int(sys.stdin.readline())+1):
    S *= i
print(S)