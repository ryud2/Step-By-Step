import sys
N = int(input())
L = {}
for i in range(N):
    A , B = input().split()
    if B == "enter":
        L[A] = 0
    elif B == "leave":
        del L[A]
print('\n'.join(sorted(L.keys(), reverse=True)))