import sys
N = int(sys.stdin.readline())
L = {}
for i in range(N):
    A , B = sys.stdin.readline().split()
    if B == "enter":
        L[A] = 0
    elif B == "leave":
        del L[A]
print('\n'.join(sorted(L.keys(), reverse=True)))