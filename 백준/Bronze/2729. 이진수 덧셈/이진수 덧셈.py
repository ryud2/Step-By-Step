import sys

T = int(sys.stdin.readline())

for i in range(T):
    A , B = map(str,sys.stdin.readline().split())
    A = int(A , 2)
    B = int(B , 2)
    print(format(A+B, 'b'))