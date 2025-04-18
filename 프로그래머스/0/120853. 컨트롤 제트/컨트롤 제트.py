def solution(s):
    answer = 0
    for i in s.split(" "):
        if i != "Z":
            i = int(i)
            answer += i
            temp = i
        else :
            answer -= temp
    return answer