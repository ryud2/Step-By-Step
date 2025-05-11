def solution(n, control):
    answer = str(n) + "+" + control
    answer = answer.replace("w","+1")
    answer = answer.replace("s","-1")
    answer = answer.replace("d","+10")
    answer = answer.replace("a","-10")
    return eval(answer)