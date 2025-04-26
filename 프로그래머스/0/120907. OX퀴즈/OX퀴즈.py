def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i[:i.index("=")]) == int(i[i.index("=")+1 :]):
            answer.append("O")
        else:
            answer.append("X")
    return answer