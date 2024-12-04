N , B = input().split()
J =['0', '1','2', '3', '4','5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N = list(N)
L = len(N)
S = 0
for k in N:
    L -= 1
    S += int(J.index(k))*(int(B)**L)
print(S)