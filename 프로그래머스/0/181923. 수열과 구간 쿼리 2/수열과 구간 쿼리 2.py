def solution(arr, queries):
    answer = []
    for i in queries:
        temp = []
        for j in arr[i[0]:i[1]+1]:
            if i[2] < j:
                temp.append(j)
        temp.sort()
        if temp == []:
            answer.append(-1)
        else:
            answer.append(temp[0])
    return answer