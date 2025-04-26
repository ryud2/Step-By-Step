def solution(a, b):
    for i in range(b,0,-1):
        if a % i == 0 and b % i == 0:
            b = b // i
            break

    soinsu = []

    for j in range(2,b+1):
        for k in range(2,j):
            if j % k == 0:
                break
        else:
            if b % j == 0:
                soinsu.append(j)

    if 2 in soinsu:
        soinsu.remove(2)
    if 5 in soinsu:
        soinsu.remove(5)

    if len(soinsu) == 0:
        return 1
    else:
        return 2