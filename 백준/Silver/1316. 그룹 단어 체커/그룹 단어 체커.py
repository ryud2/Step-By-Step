N = int(input())
C = 0
for p in range(N):
    L = []
    S = input()
    for k in S:
        if k in L:
            if L[-1] == k:
                pass
            else :
                C += 1
                break
        L.append(k)
print(N-C)