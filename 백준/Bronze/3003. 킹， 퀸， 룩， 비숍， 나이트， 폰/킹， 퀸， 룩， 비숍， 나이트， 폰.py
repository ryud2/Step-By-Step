chess = list(input().split())
minus = [1,1,2,2,2,8]
result = []
for i in range(6):
    result.append(int(minus[i]) -int(chess[i]))
print(*result)