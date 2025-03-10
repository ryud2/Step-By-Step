def solution(array):
    Max = 0
    for i in set(array):
        Temp = array.count(i)
        if Temp > Max :
            Max = Temp
            M = i
        elif Temp == Max:
            M = -1
    return M