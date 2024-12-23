import sys

while True :
    A , B , C = map(int,sys.stdin.readline().split())
    
    if A == 0 and B == 0 and C == 0:
        break
    
    if max(A,B,C) == A:
        temp = A
        A = C
        C = temp
        
    if max(A,B,C) == B:
        temp = B
        B = C
        C = temp
    
    if A**2 + B**2 == C**2 :
        print("right")
    else :
        print("wrong")