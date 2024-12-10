import math
import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    A , B = map(int,sys.stdin.readline().split())
    print(math.lcm(A,B))


# import sys
# T = int(sys.stdin.readline())
# for i in range(T):
#     A , B = map(int,sys.stdin.readline().split())
#     a , b = A , B
#     if A < B :
#             A , B = B , A
#     while A%B != 0 :
#         if A < B :
#             A , B = B , A
#         A , B = B , A%B
#     print(a*b//B)
