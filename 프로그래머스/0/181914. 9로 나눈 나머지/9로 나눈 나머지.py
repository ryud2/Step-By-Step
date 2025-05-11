def solution(number):
    Sum = 0
    for i in number:
        Sum += int(i)
    return Sum % 9 