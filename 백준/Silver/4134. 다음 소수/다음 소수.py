import sys

N = int(sys.stdin.readline())
for i in range(N):
    T = int(sys.stdin.readline())
    if T == 0 or T == 1 :
        print(2)
    else:
        while True:
            prime = True
            for i in range(2 ,int(T**(1/2))+1):
                if T % i == 0 :
                    prime = False
                    break
            if prime == True :
                print(T)
                break
            T += 1