def solution(dots):
    dots.sort()

    if abs((dots[1][1] -dots[0][1]) / (dots[1][0] -dots[0][0])) == abs((dots[3][1] -dots[2][1]) / (dots[3][0] -dots[2][0])):
        return 1
    elif ((dots[1][0] -dots[0][0])) == 0 and (dots[3][0] -dots[2][0]) == 0 :
        if abs((dots[1][1] -dots[0][1])) == abs((dots[3][1] -dots[2][1])):
            return 1
    else:
        return 0