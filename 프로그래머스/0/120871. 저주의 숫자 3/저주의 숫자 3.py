def solution(n):
    i = 1
    while i <= n:
        if i % 3 == 0 or i % 10 == 3 or (i%100)//10 == 3:
            n += 1
        i += 1
    return n