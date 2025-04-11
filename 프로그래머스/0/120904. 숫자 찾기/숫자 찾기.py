def solution(num, k):
    num = str(num)
    k = str(k)
    if num.find(k) + 1:
        return num.find(k) +1
    else:
        return num.find(k)