def solution(rsp):
    A = list(rsp)
    B = ""
    for i in A:
        if i == "0" :
            B += "5"
        elif i == "2" :
            B += "0"
        elif i == "5" :
            B += "2"
    return B