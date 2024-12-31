import sys

N1 , N2 , N12 = map(int,sys.stdin.readline().split())

print((N1+1)*(N2+1)//(N12+1) - 1)