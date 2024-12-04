A = []
for i in range(10):
    B = int(input())
    if (B % 42) not in A :
        A.append(B%42)
print(len(A))