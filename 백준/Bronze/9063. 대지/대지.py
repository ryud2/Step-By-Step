n = int(input())
O = [input().split() for i in range(n)]
X , Y = [] , []
for i in range(n) :
    X.append(int(O[i][0]))
for i in range(n) :
    Y.append(int(O[i][1]))
print((max(X)-min(X))* (max(Y)-min(Y)))