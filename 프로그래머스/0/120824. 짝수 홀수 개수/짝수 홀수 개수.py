def solution(num_list):
    A = 0
    for i in num_list:
        if i % 2 == 0 :
            A += 1
    answer = [A, len(num_list)-A]
    return answer