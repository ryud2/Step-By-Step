import sys

N = int(sys.stdin.readline())

S,M,L,XL,XXL,XXXL = map(int,sys.stdin.readline().split()) 
T , P = map(int,sys.stdin.readline().split())
C = 5

S += T-1
M += T-1
L += T-1
XL += T-1
XXL += T-1
XXXL += T-1


print(S//T + M//T + L //T + XL // T + XXL // T + XXXL // T )
print(N//P , N%P)