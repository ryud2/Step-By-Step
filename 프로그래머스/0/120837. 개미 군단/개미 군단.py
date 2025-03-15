def solution(hp):
    count = 0
    count += hp // 5
    hp = hp % 5
    count += hp // 3
    count += hp % 3
    return count