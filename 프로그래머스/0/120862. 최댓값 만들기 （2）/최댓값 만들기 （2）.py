def solution(numbers):
    numbers.sort()
    A = numbers[0] * numbers[1]
    B = numbers[-2] * numbers[-1]
    return max(A,B)