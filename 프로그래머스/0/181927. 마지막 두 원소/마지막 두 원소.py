def solution(num_list):
    return num_list + [num_list[-1] - num_list[-2] if num_list[-1] - num_list[-2] > 0 else num_list[-1]*2 ]