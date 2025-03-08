def solution(sides):
    if max(sides)*2 < sum(sides):
        return 1
    else:
        return 2