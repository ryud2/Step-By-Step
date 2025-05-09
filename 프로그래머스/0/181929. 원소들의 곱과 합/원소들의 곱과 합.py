def solution(num_list):
    gop = 1
    for i in num_list:
        gop *= i
    return 1 if sum(num_list)**2 > gop else 0