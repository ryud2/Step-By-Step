import sys

while True :
    A = sum(map(int,sys.stdin.readline().split()))
    if A == 0 :
        break
    else :
        print(A)