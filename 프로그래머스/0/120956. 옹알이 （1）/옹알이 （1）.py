def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in can:
            if j in i:
                print(i , j)
                i = i.replace(j,".",1)
        if list(set(i)) == ["."]:
            answer += 1
    return answer