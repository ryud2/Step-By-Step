def solution(s):
    answer = ''
    s1 = sorted(list(set(s)))

    for i in s1:
        if s.count(i) == 1 :
            answer += i
    return answer