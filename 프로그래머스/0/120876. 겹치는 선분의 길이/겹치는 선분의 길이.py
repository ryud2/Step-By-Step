def solution(lines):
    answer = 0
    number = []

    for i in lines:
        for j in range(i[0],i[1]):
            number.append(j)

    for k in list(set(number)):
        if number.count(k) > 1 :
            answer += 1
    return answer