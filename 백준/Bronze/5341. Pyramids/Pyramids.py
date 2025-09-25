while(True):
    A = int(input())
    sum = 0
    if A == 0 :
        break
    for i in range(1,A+1):
        sum += i
    print(sum)