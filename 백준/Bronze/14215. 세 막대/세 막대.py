A , B , C = map(int,input().split())
M = max(A,B,C)
if M < A + B + C - M:
    print(A+B+C)
else:
    print(A+B+C - M*2 + (A+B+C -1))