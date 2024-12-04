while True:
    n = int(input())
    if n == -1 :
        break
    A = [k for k in range(1 , n) if n%k == 0]
    if sum(A) == n:
        print(n , '=' , end = ' ')
        print( *A , sep = ' + ')
    else :
        print("{0} is NOT perfect.".format(n))