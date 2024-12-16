import sys

N = int(sys.stdin.readline())

B_N = [i for i in range(1,N+1)]
B = list(map(int,sys.stdin.readline().split()))

temp = 0


for i in range(N-1):
    K = B_N.pop(temp)
    print(K , end = " ")
    if B[K-1] <0 :
        temp += 1
    temp = temp + B[K-1] -1
    
    temp = temp % len(B_N)
print(*B_N)