N = int(input())
A = []
for i in range(N//3 + 1):
    k = N -(5*i)
    if k%3 == 0 and k > 0:
        A.append(i+(k//3))
    elif k == 0 :
        A.append(i)
if A == []:
    print(-1)
else:
    print(min(A))