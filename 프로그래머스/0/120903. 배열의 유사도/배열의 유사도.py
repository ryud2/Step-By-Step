def solution(s1, s2):
    
    A = 0
    
    for i in s1:
        if i in s2:
            A += 1
    return A