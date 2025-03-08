def solution(my_string, n):
    A = ""
    for i in my_string:
        A = A + i*n
    return A