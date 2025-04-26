def solution(dots):
    for i in range(4):
        for j in range(4):
            if dots[i][0] != dots[j][0] and dots[i][1] != dots[j][1]:
                answer = (dots[j][0] -dots[i][0]) * (dots[i][1] - dots[j][1])
    return answer if answer > 0 else -answer