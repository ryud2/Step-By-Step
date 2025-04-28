def solution(num, total):
    answer = []
    k = -num
    while True:
        answer = [k for k in range(k ,k + num)]
        if sum(answer) == total:
            break
        k += 1
    return answer