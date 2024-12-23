import sys

N = list(map(int,sys.stdin.readline().split()))

print((N[0]**2+N[1]**2+N[2]**2+N[3]**2+N[4]**2 )% 10)