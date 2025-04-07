def solution(balls, share):
    bf = 1
    sf = 1
    bsf = 1
    for i in range(2,balls+1):
        bf *= i
    for i in range(2,share+1):
        sf *= i
    for i in range(2,balls-share+1):
        bsf *= i
        
        
        
    return bf/(sf*bsf)