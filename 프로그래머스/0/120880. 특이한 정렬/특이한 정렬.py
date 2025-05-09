def solution(numlist, n):
    answer = []
    cha = []
    cha_sort =[]
    numlist.sort(reverse=True)

    for i in numlist:
        cha.append(i-n)

    cha_sort = sorted(cha,key = lambda x : abs(x))


    for j in cha_sort:
        answer.append(numlist[cha.index(j)])
    return answer