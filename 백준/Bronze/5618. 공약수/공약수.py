import math 
n = int(input())
num = list(map(int,input().split()))
for i in range(n-1):
    num[i+1] = math.gcd(num[i],num[i+1])
for j in range(1,num[-1]+1):
    if num[-1] % j == 0 :
        print(j)
    else :
        pass