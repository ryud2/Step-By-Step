N , X = map(int,input().split())
price = list(map(int,input().split()))
result = price[0] + price[1]
for i in range(1,N-1):
    result = (price[i] + price[i+1]) if result > (price[i] + price[i+1]) else result
print(result*X)