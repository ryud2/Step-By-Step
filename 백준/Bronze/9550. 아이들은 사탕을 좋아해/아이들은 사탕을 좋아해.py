T = int(input())
for i in range(T):
    N , K = map(int,input().split())
    People = 0
    Sa = list(map(int,input().split()))
    for j in range(N):
        People += Sa[j] // K
        
    print(People)