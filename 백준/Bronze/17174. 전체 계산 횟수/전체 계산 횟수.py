N , M = map(int,input().split())
Sum = N
while N:
    N //=M
    Sum += N
print(Sum)