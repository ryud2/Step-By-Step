import sys
A , B = map(int,sys.stdin.readline().split())
C , D = map(int,sys.stdin.readline().split())
J , M = A*D+C*B , B*D
JJ , MM = J , M
while J%M != 0 :
    J , M = M , J%M
print(JJ//M , MM//M)