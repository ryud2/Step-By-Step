def solution(array, n):
    test = []
    array.sort()
    for i in array:
        test.append(abs(i-n))
    return array[test.index(min(test))]