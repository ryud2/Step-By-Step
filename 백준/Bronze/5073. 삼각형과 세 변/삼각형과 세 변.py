while True:
    A , B , C = map(int,input().split())
    if A + B + C == 0:
        break
    if max(A,B,C) < A + B + C - max(A,B,C):
        if A == B == C :
            print("Equilateral")
        elif A == B or B == C or A == C :
            print("Isosceles")
        else :
            print("Scalene")
    else:
        print("Invalid")