N = int(input())
A = [i for i in range(2,N+1) if N % i == 0]
for i in A:
    while True:
        if N % i == 0:
            print(i)
            N = N // i
        else:
            break