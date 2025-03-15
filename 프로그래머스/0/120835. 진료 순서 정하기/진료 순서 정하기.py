def solution(emergency):
    A = sorted(emergency)
    A.reverse() 
    B = []
    for i in emergency:
        B.append(A.index(i) + 1)
    return B
