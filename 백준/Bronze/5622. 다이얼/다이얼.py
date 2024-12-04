S = list(input())
Sum = 0
for i in range(len(S)):
    alpha = (ord(S[i])- 62)
    if alpha // 3 <= 6 :
        Sum += alpha //3  + 2
    else :
        Sum += (alpha -1) // 3 + 2
    if S[i] == "Z":
        Sum -= 1
print(Sum)