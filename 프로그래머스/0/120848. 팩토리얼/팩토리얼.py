def solution(n):
    i = 2
    while n >= i :
        n  = n // i
        i += 1
    return i - 1