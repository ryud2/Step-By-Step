def solution(ineq, eq, n, m):
    answer = str(n)+ineq+eq+str(m)
    answer = answer.replace("!","")
    return 1 if eval(answer) else 0