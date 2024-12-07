import math
import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    A , B = map(int,sys.stdin.readline().split())
    print(math.lcm(A,B))