def solution(l, r):
    temp = []
    for i in range(l,r+1):
        for j in str(i):
            if j == "5" or j == "0":
                pass
            else:
                break
        else:
            temp.append(i)
    return temp if temp != [] else [-1]