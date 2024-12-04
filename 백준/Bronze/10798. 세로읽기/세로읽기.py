A = [[0 for i in range(5)] for i in range(5)]
for i in range(5):
        A[i] = list(input())
B = [(len(A[i])) for i in range(5)]
for p in range(max(B)):
    for q in range(5):
        try:
            print(A[q][p],end="")
        except:
            continue