def solution(A, B):
    answer = 0
    while answer != len(A):
        if A == B:
            return answer
            break
        A = A[-1] + A[:-1]
        answer += 1
    else:
        return -1