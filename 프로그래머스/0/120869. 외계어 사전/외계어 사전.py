def solution(spell, dic):
    temp = dic.copy()
    for test1 in spell:
        for test2 in dic:
            if len(test2) != len(spell) or (test1 not in test2):
                temp.remove(test2)
        dic = temp.copy()
    if len(temp) == 0:
        return 2
    else:
        return 1
    