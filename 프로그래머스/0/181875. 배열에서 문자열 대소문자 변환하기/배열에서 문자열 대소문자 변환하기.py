def solution(strArr):
    answer = []
    for i in range(0,len(strArr)):
        if i % 2 == 1:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer