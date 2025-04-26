def solution(score):
    answer = []
    Sum = []
    for i in score:
        Sum.append(sum(i))
    Sum_sort = sorted(Sum , reverse=True)
    for i in Sum:
        answer.append(Sum_sort.index(i) + 1)
    return answer