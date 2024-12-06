import sys
N = int(input())
L = []
for i in range(N):
    A , B = map(str,input().split())
    if B == "enter":
        L.append(A)
    elif B == "leave":
        L.remove(A)
L.sort(reverse=True)
print(*L, sep = "\n")